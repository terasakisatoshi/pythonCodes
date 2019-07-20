from myopenopt import *
model = Model("sample", mtype='NLP')
x1 = model.addVar(vtype="C", name="x1")
x2 = model.addVar(vtype="C", name="x2")
x3 = model.addVar(vtype="C", ub=10, name="x3")
model.update()
c1 = model.addConstr(x1**2 + 2*x2**2 <= x3**2, name="C1")
c2 = model.addConstr(x3 <= 30, name="C2")
c3 = model.addConstr(quicksum([x1, x2, x3]) <= 20, name="C3" )
model.setObjective(15*x1 + 18*x2 + 30*x3, GRB.MAXIMIZE)
print(model)
model.optimize(solver="ralg")
print("Result =", model.Status)
for v in model.getVars():
    print(v.VarName, v.X)

