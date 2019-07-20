import sympy as sy
from sympy import init_printing
from sympy import pprint
init_printing()

def main():
    problem=[sy.Matrix([3,0,1]),sy.Matrix([-1,1,2]),sy.Matrix([2,-1,-2])]
    result=sy.GramSchmidt(problem,True)
    u1=result[0]
    u2=result[1]
    u3=result[2]


    print("result")
    print("u1"),pprint(u1),pprint(sy.N(u1))
    print("u2"),pprint(u2),pprint(sy.N(u2))
    print("u3"),pprint(u3),pprint(sy.N(u3))
    print("check norm ")
    print("norm u1",u1.norm(),)
    print("norm u2",u2.norm())
    print("norm u3",u3.norm())
    print("check inner prod")
    print("u1.dot(u2)",u1.dot(u2))
    print("u1.dot(u3)",u1.dot(u3))
    print("u2.dot(u3)",u2.dot(u3))
if __name__ == '__main__':
    main()