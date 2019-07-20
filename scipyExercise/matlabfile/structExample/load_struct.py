from scipy.io import loadmat, savemat, whosmat

print(whosmat('octave_struct.mat'))


def loadnaive(mfile):
    mat = loadmat(mfile)
    my_struct = mat['my_struct'][0, 0]
    print(my_struct.dtype)
    print(my_struct['field1'][0, 0])
    print(my_struct['field2'][0, 0])


def load_with_squeeze_me(mfile):
    mat = loadmat(mfile, squeeze_me=True)
    my_struct = mat['my_struct']
    print(my_struct.dtype)
    print(my_struct['field1'])
    print(my_struct['field2'])


def load_with_struct_as_record_false(mfile):
    mat = loadmat(mfile, struct_as_record=False, squeeze_me=True)
    my_struct = mat['my_struct']
    print(my_struct.field1)
    print(my_struct.field2)
    mat = loadmat(mfile, struct_as_record=False)
    my_struct = mat['my_struct'][0, 0]
    print(my_struct.field1[0, 0])
    print(my_struct.field2[0, 0])

mfile = 'octave_struct.mat'
# loadnaive(mfile)
# load_with_squeeze_me(mfile)
load_with_struct_as_record_false(mfile)
