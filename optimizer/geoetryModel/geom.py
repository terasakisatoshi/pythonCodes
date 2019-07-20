from z3 import Real, Solver, Or, And

p0 = [0, 0]
p1 = [0, 1]
p2 = [2, 1]
p3 = [2, 0]
p4 = p0

t1 = Real('t1')
t2 = Real('t2')
t3 = Real('t3')
t4 = Real('t4')

q1x = p0[0]+t1*(p1[0]-p0[0])
q1y = p0[1]+t1*(p1[1]-p0[1])

q2x = p1[0]+t2*(p2[0]-p1[0])
q2y = p1[1]+t2*(p2[1]-p1[1])

q3x = p2[0]+t3*(p3[0]-p2[0])
q3y = p2[1]+t3*(p3[1]-p2[1])

q4x = p3[0]+t4*(p4[0]-p3[0])
q4y = p3[1]+t4*(p4[1]-p3[1])

solver = Solver()

solver.add(t1 >= 0, t2 >= 0, t3 >= 0, t4 >= 0)
solver.add(t1 <= 1, t2 <= 1, t3 <= 1, t4 <= 1)


def orthogonal(px, py, qx, qy, rx, ry):
    return (px-qx)*(rx-qx)+(py-qy)*(ry-qy) == 0

solver.add(orthogonal(q1x, q1y, q2x, q2y, q3x, q3y))
solver.add(orthogonal(q2x, q2y, q3x, q4y, q4x, q4y))
solver.add(orthogonal(q3x, q3y, q4x, q4y, q1x, q1y))
solver.add(orthogonal(q4x, q4y, q1x, q1y, q2x, q2y))
solver.add((q2x-q1x)**2+(q2y-q1y)**2 == (q4x-q3x)**2+(q4y-q3y)**2)
solver.add((q3x-q2x)**2+(q3y-q2y)**2 == (q4x-q1x)**2+(q4y-q1y)**2)
solver.add()


solver.check()
print(solver.model())
