#skip header and footer
import numpy as np 
from io import StringIO
data=u"\n".join(str(i) for i in range(10))
print(np.genfromtxt(StringIO(data),skip_header=1,skip_footer=7))
print("complete")
print("next topic")