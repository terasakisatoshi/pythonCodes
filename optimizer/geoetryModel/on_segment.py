from myopenopt import Model, GRB

EPS=1e-4
def add_cond_on_segment(optimizer, b, e, x, y):
    optimizer.addConstr((e[0]-b[0])*(y-b[1])-(e[1]-b[1])*(x-b[0]) <= EPS)
    optimizer.addConstr((e[0]-b[0])*(y-b[1])-(e[1]-b[1])*(x-b[0]) >= -EPS)
    optimizer.addConstr(min(b[0], e[0]) <= x)
    optimizer.addConstr(max(b[0], e[0]) >= x)
    optimizer.addConstr(min(b[1], e[1]) <= y)
    optimizer.addConstr(max(b[1], e[1]) >= y)

def main():
    b=[0,0]
    e=[2,2]
    model=Model()
    x=model.addVar(name='x')
    y=model.addVar(name='y')
    add_cond_on_segment(model,b,e,x,y)
    model.setObjective(x,GRB.MAXIMIZE)
    print(model)
    model.optimize()
    print(model.getVars())
    for v in model.getVars():
        print(v.VarName, v.X)

if __name__ == '__main__':
    main()