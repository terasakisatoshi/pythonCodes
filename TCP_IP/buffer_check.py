import numpy as np


def floating_point():
    arr_float = np.array([1., 2., 3.]).astype(float)
    arr_float32 = np.array([1., 2., 3.]).astype(np.float32)
    arr_float64 = np.array([1., 2., 3.]).astype(np.float64)

    print(arr_float.tobytes(), arr_float.nbytes)
    print(arr_float32.tobytes(), arr_float32.nbytes)
    print(arr_float64.tobytes(), arr_float64.nbytes)

    print(arr_float.dtype.byteorder)
    print(arr_float32.dtype.byteorder)
    print(arr_float64.dtype.byteorder)

    print(arr_float.dtype.char)
    print(arr_float32.dtype.char)
    print(arr_float64.dtype.char)


def integer():
    arr_int = np.array([1, 2, 3]).astype(int)
    arr_int32 = np.array([1, 2, 3]).astype(np.int32)
    arr_int64 = np.array([1, 2, 3]).astype(np.int64)

    print(arr_int.tobytes(), arr_int.nbytes)
    print(arr_int32.tobytes(), arr_int32.nbytes)
    print(arr_int64.tobytes(), arr_int64.nbytes)

    print(arr_int.dtype.byteorder)
    print(arr_int32.dtype.byteorder)
    print(arr_int64.dtype.byteorder)

    print(arr_int.dtype.char)
    print(arr_int32.dtype.char)
    print(arr_int64.dtype.char)


def main():
    integer()
if __name__ == '__main__':
    main()
