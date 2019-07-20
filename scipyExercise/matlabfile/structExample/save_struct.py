from scipy.io import loadmat, savemat, whosmat

a_dict = {'field1': [0.5, 0.1], 'field2': 'a string'}
savemat('saved_struct.mat', {'a_dict': a_dict})
mat = loadmat('saved_struct.mat', struct_as_record=False, squeeze_me=True)
print(mat['a_dict'].field1)
print(mat['a_dict'].field2)
