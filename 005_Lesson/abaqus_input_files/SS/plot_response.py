import numpy as np
import matplotlib.pyplot as plt


jobname = 'Lesson005_1Element_TXC'
fh = open(jobname+'_results.dat', 'r')
lines = fh.readlines()
fh.close()

store_E11=[]
store_E22=[]
store_E33=[]
store_S11=[]
store_S22=[]
store_S33=[]
store_Q=[]
store_P=[]

for line in lines:
    line = line.replace(" ", "")
    line = line.split(',')
    print(line)
    E11 = float(line[1])
    E22 = float(line[2])
    E33 = float(line[3])
    S11 = float(line[4])
    S22 = float(line[5])
    S33 = float(line[6])
    Q   = float(line[7])
    P   = float(line[8])
    
    store_E11.append(E11)
    store_E22.append(E22)
    store_E33.append(E33)
    store_S11.append(S11)
    store_S22.append(S22)
    store_S33.append(S33)
    store_Q.append(Q)
    store_P.append(P)
    
    
# convert to numpy arrays
store_E11=np.asarray(store_E11)
store_E22=np.asarray(store_E22)
store_E33=np.asarray(store_E33)
store_S11=np.asarray(store_S11)
store_S22=np.asarray(store_S22)
store_S33=np.asarray(store_S33)
store_Q=np.asarray(store_Q)
store_P=np.asarray(store_P)

store_V = store_E11+store_E22+store_E33

# ==========
# Plot
# ==========
plt.rc('font',size = 20)
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)
scale=1.2
min_strain = -0.04
max_strain = 0.15

fig = plt.figure(figsize=(20/scale,12/scale))
ax  = plt.subplot(231)
ax.plot(-store_E33,-store_S33,'k-o')
ax.set_xlabel('Vertical Strain')
ax.set_ylabel('Vertical Stress',rotation=90)
ax.set_xlim((min_strain,max_strain))
ax.set_ylim((-1,10))

ax  = plt.subplot(232)
ax.plot(-store_E11,-store_S11,'k-o')
ax.set_xlabel('$\epsilon_{11}$')
ax.set_ylabel('$\sigma_{11}$',rotation=90)
ax.set_xlim((min_strain,max_strain))
ax.set_ylim((-1,10))

ax  = plt.subplot(233)
ax.plot(-store_E22,-store_S22,'k-o')
ax.set_xlabel('$\epsilon_{22}$')
ax.set_ylabel('$\sigma_{22}$',rotation=90)
ax.set_xlim((min_strain,max_strain))
ax.set_ylim((-1,10))

ax  = plt.subplot(234)
ax.plot(-store_E33,store_Q,'k-o')
ax.set_xlabel('Vertical Strain')
ax.set_ylabel('$q$',rotation=0)
ax.set_xlim((min_strain,max_strain))

ax  = plt.subplot(235)
ax.plot(-store_P,store_Q,'k-o')
ax.set_xlabel('$p$')
ax.set_ylabel('$q$',rotation=0)

ax  = plt.subplot(236)
ax.plot(-store_E33,store_V,'k-o')
ax.set_xlabel('Vertical Strain')
ax.set_ylabel('Volumetric Strain',rotation=90)
ax.set_xlim((min_strain,max_strain))


#
#plt.suptitle('Constitutive Model Driver')
#
#fig.subplots_adjust(top=0.94)
##plt.tight_layout()
plt.tight_layout(pad=0, w_pad=0, h_pad=2)
plt.savefig(jobname+'_plot.png', dpi=300)