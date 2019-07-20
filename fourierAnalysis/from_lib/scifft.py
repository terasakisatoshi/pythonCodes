""" 
1次元 離散フーリエ変換
"""
import numpy as np
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt


# 時系列のサンプルデータの作成
N = 120                      # データ数
T=10            # サンプリング幅
del_t= T/N   #  サンプリング間隔

del_w=2*np.pi/T # 離散フーリエ変換の振動数の間隔
#

# 離散点　生成
xs = np.arange(0,T-del_t,del_t)
w=np.arange(2*np.pi/T, 2*np.pi*N/T, del_w)

#
f1,f2=3,4
f=np.sin(2*np.pi*f1*xs)+np.sin(2*np.pi*f2*xs)
#
g = fft(f)
# パワースペクトルの表示

plt.plot(w,np.abs(g)**2,marker='o',markersize=4,label='|g(w)|^2')

plt.xlabel('w', fontsize=24)
plt.ylabel('Power spectrum |g(w)|^2', fontsize=24)
plt.legend(loc='best')

plt.show()