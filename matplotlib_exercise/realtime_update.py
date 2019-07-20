# -*- coding:utf-8 -*-
# python2.7で動作確認

# matplotlib, Tkを使用したリアルタイムグラフ描画のサンプル
#
# 参考：
# http://d.hatena.ne.jp/saket/20111004/1317714358
# http://matplotlib.org/examples/user_interfaces/embedding_in_tk2.html

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

import datetime

REDRAW_CYCLE = 100          # msec 再描画間隔
DRAW_SEC = 10.0             # sec 何秒分表示するか
DRAW_SAMPLING_RATE = 1000   # 点  秒間あたりの表示点数

class SerialData:
    """ グラフに表示するデータを用意するクラスの雛形
        
        グラフに表示するデータを返す get_next(),
        グラフのy軸範囲を返す get_data_range(),
        そのデータが秒間何サンプリングかを返す get_sampling_rate()
        が必要。
    """
    def __init__(self):
        self.sampling_rate = 3000
        self.data_range = [0, 330]
    
    def get_sampling_rate(self):
        return self.sampling_rate
    
    def get_data_range(self):
        """ 返すデータの取りうる範囲を返す。
            グラフの値域に相当するため、余裕を持った値を返してもOK。
            @return [min, max]
        """
        return self.data_range
    
    def get_next(self):
        """ グラフ表示用のデータを返す。
            リアルタイムにデータを用意する場合は、呼び出された時点までに
            用意できたデータをそのまま返せば良い。
        """
        # テスト時は固定長のデータなので、REDRAW間隔とデータサンプリングレートに
        # 注意すること。今はREDRAW100ms, rate3000なので300個のデータを
        # サンプリングしたことにする
        return range(0, 300)

class View:
    """ グラフ表示用のGUI管理クラス
    """
    def __init__(self):
        self.t1 = datetime.datetime.now()
        
        self.root = Tk.Tk()
        self.root.wm_title("dynamic graph")
        
        # データ出力オブジェクトの準備
        self.serial = SerialData()
        self.data = []
        self.data_start_time = 0.0
        
        # 何秒分表示するか
        self.draw_sec = DRAW_SEC
        # 描画する点のレート(秒間何点使うか)
        self.draw_sampling_rate = DRAW_SAMPLING_RATE
        
        # インチ指定...
        self.f = Figure(figsize=(6,4), dpi=100)
        self.a = self.f.add_subplot(111)
        self.a.set_title('hogehoge data', size=12)

        self.plot_data = self.a.plot(
                self.data,
                linewidth=0.5,
                color=(1, 0, 0),
                )[0]
        
        self.canvas = FigureCanvasTkAgg(self.f, master=self.root)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        
        self.canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        
        self.button = Tk.Button(master=self.root, text='Quit', command=self._quit)
        self.button.pack(side=Tk.BOTTOM)
        
        self.on_redraw_timer()

        self.root.mainloop()
    
    def on_redraw_timer(self):
        self.t1 = datetime.datetime.now()
        self.add_draw_data(self.serial.get_next())
        self.draw_plot()
        
        self.t2 = datetime.datetime.now()
        tdelta = self.t2 - self.t1
        tofs = datetime.timedelta(microseconds = (REDRAW_CYCLE * 1000)) - tdelta
        
        # 描画処理にかかった時間だけ、afterにセットする時間を調節する。
        # wxPythonだとwx.Timer()が必ず定期的に起こしてくれる？
        # もっとスマートな方法があればいいなぁ...
        self.root.after(tofs.microseconds // 1000, self.on_redraw_timer)
    
    def add_draw_data(self, data):
        """ 描画対象のデータを追加する
            @param data データ配列。前回のデータから時系列的に連続しているのが前提。
            描画サンプリングレートとデータのサンプリングレートのずれ
            で描画単位ごとに境界がずれるが、微々たるものなので気にしない。
        """
        sampling_rate = self.serial.get_sampling_rate()
        sampling_sec = 1. / sampling_rate
        
        draw_sampling_rate = self.draw_sampling_rate
        draw_sampling_sec = 1. / draw_sampling_rate
        
        newdata = []
        time = 0.0
        
        # データサンプリングレートが描画サンプリングレートより充分大きくないと
        # 正しい位置にデータをプロットできない
        for s in data:
            time += sampling_sec
            
            # データサンプリング周期が描画サンプリング周期を超えたところで
            # データをnewdataに追加する
            if time >= draw_sampling_sec:
                time -= draw_sampling_sec
                newdata.append(s)
        
        # 1つ前のデータに今回のデータを付け加える
        self.data += newdata
        # 画面に表示する全ての描画点数
        remain_frame_length = int(self.draw_sec * draw_sampling_rate)
        
        # 描画点数が画面全体の点数より少ない場合の処理
        self.data_start_time += max((len(self.data) - remain_frame_length), 0) / float(draw_sampling_rate)
        
        self.data = self.data[-remain_frame_length:]
        
    def draw_plot(self):
        num_draw_frame = int(self.draw_sec * self.draw_sampling_rate)
        draw_sampling_rate = self.draw_sampling_rate
        
        xmin = self.data_start_time
        xmax = xmin + self.draw_sec
        
        data_range = self.serial.get_data_range()
        ymin = data_range[0]
        ymax = data_range[1]
        
        self.a.set_xbound(lower=xmin, upper=xmax)
        self.a.set_ybound(lower=ymin, upper=ymax)
        
        self.a.grid(True, color='gray')
        
        xaxis = [float(con) / self.draw_sampling_rate + self.data_start_time for con in range(len(self.data))]
        self.plot_data.set_xdata(xaxis)
        self.plot_data.set_ydata(np.array(self.data))
        self.canvas.draw()
        
    def _quit(self):
        self.root.quit()     # stops mainloop
        self.root.destroy()  # this is necessary on Windows to prevent

if __name__ == '__main__':
    v = View()