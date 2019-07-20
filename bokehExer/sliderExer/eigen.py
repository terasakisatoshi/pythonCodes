import numpy as np

mat = np.array([[1, -1],
                [1, 1]])

evals, evecs = np.linalg.eig(mat)
ev1,ev2=evals
evec1=evecs.T[0]
evec2=evecs.T[1]
print(np.isreal(ev1))
print(ev1, mat@evec1, ev1*evec1)
print(ev2, mat@evec2, ev2*evec2)