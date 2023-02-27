import numpy as np
import matplotlib.pyplot as plt
mu=2
sigma=0.5
v=np.random.normal(mu,sigma,10000)
plt.hist(v,bins=50,density=1)
plt.show()
print(v)
