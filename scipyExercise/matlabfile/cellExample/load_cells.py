from scipy.io import loadmat, savemat, whosmat


def load_naive(mfile):
    mat = loadmat(mfile)
    my_cells = mat['my_cells']
    print(my_cells)


def load_with_squeeze_me(mfile):
    mat = loadmat(mfile, struct_as_record=False, squeeze_me=True)
    my_cells = mat['my_cells']
    print(my_cells)

mfile = 'octave_cells.mat'

load_naive(mfile)
load_with_squeeze_me(mfile)
