import numpy as np
a=np.arange(20)
a.shape=4,-1
print(a.shape)
print(np.atleast_3d(a))
b=np.arange(15)
print(b)
print(np.atleast_1d(b))
print(np.atleast_2d(b))
print(np.atleast_3d(b))
