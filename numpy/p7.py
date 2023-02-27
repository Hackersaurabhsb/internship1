import numpy as np 
from io import StringIO
data="""#
#skip me
#skip me tooo
#consider me
1,2,4,5 
23,4,3,4 
"""
print(np.genfromtxt(StringIO(data),comments="#",delimiter=",",dtype="int64"))

