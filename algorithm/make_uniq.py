#https://github.com/numpy/numpy/issues/2871
#numpy-1.12.1だとバグで動作しない
import numpy as np
uniq_arr = np.unique(arr, axis=0)
print(uniq_arr)
#https://www.reddit.com/r/learnpython/comments/3v9y8u/how_can_i_find_unique_elements_along_one_axis_of/
import pandas as pd
arr = [[0, 0], [1, 1], [1, 0], [1, 1], [0, 1], [0, 0]]
df = pd.DataFrame(arr)
unique_arr = df.drop_duplicates().values
print(unique_arr)
