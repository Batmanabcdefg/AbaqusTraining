import numpy as np
E = 1.
nu = 0.2
sig=np.zeros(3)
sig[0] = 0.
sig[1] = 0.
sig[2] = -0.13

U1 = ( (1.+nu)*sig[0] - nu*( sig.sum() ) )/E
U2 = ( (1.+nu)*sig[1] - nu*( sig.sum() ) )/E
U3 = ( (1.+nu)*sig[2] - nu*( sig.sum() ) )/E
print("U1 = %f\n"%U1)
print("U2 = %f\n"%U2)
print("U3 = %f\n"%U3)

