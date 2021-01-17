import numpy as np

a = [1,2,3,4,5,6,7,8,9]
a_split = np.array_split(a,4)
print([x for num,x in enumerate(a_split) if num != 1])