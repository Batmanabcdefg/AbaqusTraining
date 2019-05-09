import numpy as np
E = 1000.
nu = 0.3
sig=np.zeros(3)
sig[0] = 0.
sig[1] = 0.
sig[2] = -0.13

U3 = ( (1+nu)*sig[2] - nu*( sig.sum() ) )/E
print("U3 = %f\n"%U3)

