#coding: utf-8
"""
reference:
http://aidiary.hatenablog.com/entry/20140205/1391601418
"""
import numpy as np
import pylab
from sklearn.datasets import fetch_mldata

# mnistの手書き数字データをロード
# カレントディレクトリ（.）にない場合は、
# Webから自動的にダウンロードされる（時間がかかるので注意！）
# 70000サンプル、28x28ピクセル
mnist = fetch_mldata('MNIST original', data_home=".")

# ランダムに25サンプルを描画
# digits.images[i] : i番目の画像データ（8x8ピクセル）
# digits.target[i] : i番目の画像データのクラス（数字なので0-9）
p = list(np.random.random_integers(0, min(len(mnist.data),len(mnist.target)), 25))
index=0
data=mnist.data[p]
target=mnist.target[p]
for data,label in zip(data,target):
    pylab.subplot(5, 5, index + 1)
    pylab.axis('off')
    pylab.imshow(data.reshape(28, 28), cmap=pylab.cm.gray_r, interpolation='nearest')
    pylab.title('%i' % label)
    index+=1
pylab.show()