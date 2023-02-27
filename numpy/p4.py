import numpy as np 
import matplotlib.pyplot as plt
mu,sigma=2,0.5
v=np.random.normal(mu,sigma,10000)
(n,bins)=np.histogram(v,bins=50,density=0)
plt.plot(.5*(bins[1:]+bins[:-1]),n)
plt.show()