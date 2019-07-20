#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import sys  
import os  
import Tkinter as Tk
import commands as com
import ScrolledText as St 
import tkFileDialog as dlg
import tkMessageBox as msb

root=Tk.Tk()
root.title("Python GUI Sample")
histfile="py_hist"  #ヒストリファイル
#str= com.getoutput("ls -la")

#-------------------------------------------------------------------------------
#ボタン１の処理    コマンド実行（イベントで呼ばれるようにするため（ｅｖｅｎｔ）をつける）
#-------------------------------------------------------------------------------
def button1(event):
    cmd=inTex.get(Tk.SEL_FIRST, Tk.SEL_LAST).encode('utf-8')    #選択範囲の文字を渡す
    print cmd           #標準出力
    str= com.getoutput(cmd)     #システムのコマンドを実行
    text.delete("1.0","end")    #１行目の０文字目から最後までを削除
    text.insert("end",str)      #最後の行にインサートする
    hist()              #履歴更新の処理
#-------------------------------------------------------------------------------
def button0():
    cmd=inTex.get(Tk.SEL_FIRST, Tk.SEL_LAST).encode('utf-8')    #選択範囲の文字を渡す
    print cmd           #標準出力
    str= com.getoutput(cmd)     #システムのコマンドを実行
    text.delete("1.0","end")    #１行目の０文字目から最後までを削除
    text.insert("end",str)      #最後の行にインサートする
    hist()              #履歴更新の処理
#-------------------------------------------------------------------------------
#ボタン２の処理　　表示エリアを削除
#-------------------------------------------------------------------------------
def button2():
    text.delete("1.0","end")    #１行目の０文字目から最後までを削除
#-------------------------------------------------------------------------------
#ボタン3の処理　　コマンドエリアを削除
#-------------------------------------------------------------------------------
def button3():
    inTex.delete("1.0","end")   #１行目の０文字目から最後までを削除
#-------------------------------------------------------------------------------
#ボタン4の処理　　履歴表示
#-------------------------------------------------------------------------------
def button4():
    if os.path.isfile(histfile):                #ファイルの存在確認  
        for line in open(histfile,"r"):         #ファイルオープン＆読込
            inTex.insert("end",line)            #最後の行にインサートする
    else:
        msb.showinfo("履歴なし","今んとこ履歴は無いよ！")  #メッセージボックス表示
#-------------------------------------------------------------------------------
#ボタン5の処理　　履歴削除
#-------------------------------------------------------------------------------
def hisdel():
    if os.path.isfile(histfile):                    #ファイルの存在確認
        ret = msb.askquestion("履歴削除","履歴を削除しちゃうよ！") #問い合わせダイアログ表示
        if ret == 'yes':
            os.remove(histfile)             #ファイル削除
    else:
        msb.showinfo("履歴なし","今んとこ履歴は無いよ！")      #メッセージボックス表示
#-------------------------------------------------------------------------------
#ボタン6の処理　　結果保存
#-------------------------------------------------------------------------------
def saveas():
    #asksaveasfilename 保存場所を選択する。
    filename=dlg.asksaveasfilename()            #保存先選択のダイアログ表示
    if filename != '':
        f = open(filename,"w")              #ファイルオープン＆書込    
        f.write(text.get("1.0","end").encode('utf-8'))  #１行目の０文字目から最後まで
        f.close()                   #ファイルクローズ
#-------------------------------------------------------------------------------
#履歴更新の処理
#-------------------------------------------------------------------------------
def hist():
    f = open(histfile,"a")                  #ファイルオープン＆書込
    f.write(inTex.get(Tk.SEL_FIRST, Tk.SEL_LAST) + "\n")    #選択範囲の文字を渡す
    f.close()
#-------------------------------------------------------------------------------

#バインディング
root.bind("<Button-3>",button1) #マウスの右クリックのイベントでbutton1を実行
root.bind("<F1>",button1)   #F1キーでbutton1を実行

#ラベル
lbl = Tk.Label(root, text="brokendish.org", font=('Times', '12'),anchor=Tk.E,width=20)
lbl.grid(row=0,column=1,columnspan=5,sticky=Tk.E,padx=5, pady=5)

#テキストエリア
text=St.ScrolledText(root, font=('Times', '10'))
text.grid(row=1,column=0,columnspan=5,sticky=Tk.W+Tk.E,padx=5, pady=5)

#ラベル（コメント）
msg="コマンドを入力し、選択した部分を実行します。実行は「F1」、「右クリック」、「実行ボタン」"
lblm = Tk.Label(root, text=msg, font=('Times', '10'),anchor=Tk.W)
lblm.grid(row=2,column=0,columnspan=5,sticky=Tk.W+Tk.E,padx=5, pady=5)

#ボタン6
btn6 = Tk.Button(root, text="保存", font=('Times', '12'),anchor=Tk.CENTER,width=10,command=saveas)
btn6.grid(row=2,column=1,columnspan=5,sticky=Tk.E,padx=5, pady=5)

#テキストエリア（入力用）
inTex = St.ScrolledText(root, font=('Times', '12'),height=10)
inTex.grid(row=3,column=0,columnspan=5,sticky=Tk.W+Tk.E,padx=5, pady=5)

#ボタン1
btn1 = Tk.Button(root, text="コマンド実行", font=('Times', '12'),anchor=Tk.CENTER,command=button0)
btn1.grid(row=4,column=0,padx=5, pady=5)

#ボタン２
btn2 = Tk.Button(root, text="表示エリアを削除", font=('Times', '12'),anchor=Tk.CENTER,command=button2)
btn2.grid(row=4,column=1,padx=5, pady=5)

#ボタン3
btn3 = Tk.Button(root, text="コマンドエリアを削除", font=('Times', '12'),anchor=Tk.CENTER,command=button3)
btn3.grid(row=4,column=2,padx=5, pady=5)

#ボタン4
btn4 = Tk.Button(root, text="履歴表示", font=('Times', '12'),anchor=Tk.CENTER,command=button4)
btn4.grid(row=4,column=3,padx=5, pady=5)

#ボタン5
btn5 = Tk.Button(root, text="履歴削除", font=('Times', '12'),anchor=Tk.CENTER,command=hisdel)
btn5.grid(row=4,column=4,padx=5, pady=5)

root.mainloop()