import numpy as np

#行列Cの定義
C=np.array( [[1,2,3,-4],[2,5,4,0],[3,4,1,1],[-4,0,10,2]])

indices=np.argwhere(C == C.min())

print(indices)