import numpy as np

a = np.array([1,2,3,3,3,3,3,3])
print(a.shape)
print(np.bincount(a).argmax())