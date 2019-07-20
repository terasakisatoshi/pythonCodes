# -*- coding: utf-8 -*-
import xlwt as xw
import matplotlib.pyplot as plt

# Excel New Bookを作成
wb = xw.Workbook()

# セルに値をセットする
xw.Range('A1').value = 'Foo 1'

# 値を取得する
str = xw.Range('A1').value
print(str)

# 指定したセルを基準に表データをセットする
xw.Range('A1').value = [['Foo1','Foo2', 'Foo3'], [10, 20, 30]]

# 指定したセルを基準に表データを取得する
table = xw.Range('A1').table.value
print(table)

# 指定した範囲のデータを取得する
table2 = xw.Range('A1:C2').value
print(table2)

# ワークブックやシートを指定する
table3 = xw.Range('Shett1', 'A1:C2', wkb=wb).value
print(table3)

# matplotlibのグラフを追加する(エクセルのグラフを作成できるけど)
fig = plt.figure()
plt.plot([1,2,3,4,5])
plot = xw.Plot(fig)
plot.show('Plot1', left=xw.Range('D3').left, top=xw.Range('D3').top)

# 保存
file_name = "xlwings_sample.xlsx"
wb.save(file_name)