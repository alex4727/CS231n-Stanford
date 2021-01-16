import numpy as np

a = np.array([1.5, 0.2, 4.2, 2.5])
s=a.argsort()
print(s)
print(a[s])


b = np.array([1.5, 0.2, 4.2, 2.5])
print(s[0:2])


print(np.argsort(b)[0:2])

