import numpy as np
from io import StringIO
data=u"1,2.21%,3\n4,5.22%,6"
c=lambda x:float(x.strip(b"%"))/100
print(np.genfromtxt(StringIO(data),delimiter=",",converters={0:c}))

