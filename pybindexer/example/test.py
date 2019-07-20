import numpy as np

import example

tensor = np.arange(30 * 30).reshape(30, 30).astype(np.float32)

ret = example.get_tensor(tensor.ravel())
# print(ret)
