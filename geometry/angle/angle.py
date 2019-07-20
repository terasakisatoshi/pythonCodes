import numpy as np
from numpy.linalg import norm
from numba import jit


def main():
    vertices = [np.array([0.0, 0.0]),
                np.array([0.0, 10.0]),
                np.array([10.0, 10.0]),
                np.array([10.0, 0.0]),
                np.array([0.0, 0.0])]
    p = np.array([5, 5])

    tot = 0.0
    for i in range(len(vertices)-1):
        v = vertices[i]
        v_next = vertices[i+1]
        v_p = v-p
        v_next_p = v_next-p
        dot = np.dot(v_p, v_next_p)
        cross = np.cross(v_p, v_next_p)
        cos_theta = dot/(norm(v_p)*norm(v_next_p))
        theta = np.arccos(cos_theta)
        sgn = cross/abs(cross)
        tot += sgn*theta
    deg = tot*180/np.pi
    print('tot=', deg)

if __name__ == '__main__':
    main()
