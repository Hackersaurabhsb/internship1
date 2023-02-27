import numpy as np  
from io import StringIO
data=u"@,6,!!\n@,&&&,5"
names=("a,b,c")
kwargs=dict(names=names,delimiter=",",dtype=int,missing_values={0:"@",'b':"***",2:"!!"},filling_values={0:0,'b':1,2:2})
print(np.genfromtxt(StringIO(data),**kwargs))
print(np.genfromtxt(StringIO(data),names=names,dtype=int,delimiter=",",missing_values={0:"@",'b':"***",2:"!!"},filling_values={0:0,'b':1,2:2}))