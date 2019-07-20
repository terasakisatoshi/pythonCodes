from myopenopt import *
model = Model("sample", mtype='NLP')
x1 = model.addVar(vtype="C", name="x1")
x2 = model.addVar(vtype="C", name="x2")
model.update()
c1 = model.addConstr(-1e-4<=x1**2 + x2**2 - 1.0<=1e-4, name="C1")
model.setObjective(x1+x2, GRB.MAXIMIZE)
print(model)
model.optimize(plot=False)
print("Result =", model.Status)
for v in model.getVars():
    print(v.VarName, v.X)
