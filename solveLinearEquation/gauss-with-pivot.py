import numpy as np

# Example1
a = np.matrix([[0, 4, 5, 2],
               [1, 0, 2, -6],
               [4, 1, 0, -2],
               [1, 7, 1, 0]], dtype='float64')
b = np.matrix([9, -3, 1, -3], dtype='float64').T
x = np.matrix([None]*4, dtype='float64').T

# Example2
a = np.matrix([[2, 4, 6],
               [1, -1, 5],
               [4, 1, -2]], dtype='float64')
b = np.matrix([28, 7, 21], dtype='float64').T
x = np.matrix([None]*3, dtype='float64').T

# for check sum
ori_a = a
# define extended coefficient matrix of eq ax=b
a = np.concatenate([a, b], axis=1)
(row, col) = a.shape
for j in range(row):
    # search pivot
    max_idx = j+np.argmax(abs(a[j:, j]))
    # swap!
    a[[j, max_idx]] = a[[max_idx, j]]
    # push forward
    for i in range(j+1, row):
        p = -a[i, j] / a[j, j]
        a[i] += p*a[j]
print('extended coefficient matrix applied gauss method \n a={}'.format(a))
# back forward
for i in range(row)[::-1]:
    x[i] = (a[i, -1]-np.dot(a[i, i+1:row], x[i+1:row]))/a[i, i]
print('x={}'.format(x))
# confirm
print("ax-b\n={}".format(ori_a@x-b))
