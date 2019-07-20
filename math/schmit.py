import numpy as np


def normalize(v):
    return v / np.linalg.norm(v)


def main():
    a1 = np.array([3, 0, 1])
    a2 = np.array([-1, 1, 2])
    a3 = np.array([2, -1, -2])

    us = []

    u1 = a1 / np.linalg.norm(a1)
    u2 = normalize(a2 - np.dot(a2, u1) * u1)
    u3 = normalize(a3 - np.dot(a3, u1) * u1 - np.dot(a3, u2) * u2)

    print(u1)
    print(u2)
    print(u3)
    print("confirm")
    print(np.dot(u1, u2))
    print(np.dot(u1, u3))
    print(np.dot(u2, u3))


if __name__ == '__main__':
    main()
