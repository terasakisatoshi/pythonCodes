import numpy as np 
from matplotlib import pyplot as plt 
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist 

X=np.array([[1,2],[2,1],[3,4],[4,3]])
Z=linkage(X,'ward')
dendrogram(Z)
plt.show()