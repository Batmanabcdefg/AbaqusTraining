import numpy as np
import matplotlib.pyplot as plt


jobname = 'Lesson006_1Element_TXC2'
remove_consolidation_step = True

# ================================================================
last_consolidation_frame = False
fh = open(jobname+'_results.dat', 'r')
lines = fh.readlines()
fh.close()

step_start=[]
step_end=[]
color_vec=['g','r']
store_step=[]
store_E11=[]
store_E22=[]
store_E33=[]
#store_EV=[]

store_S11=[]
store_S22=[]
store_S33=[]
store_Q=[]
store_P=[]


offset_E11 = 0.
offset_E22 = 0.
offset_E33 = 0.
offset_S11 = 0.
offset_S22 = 0.
offset_S33 = 0.
offset_Q = 0.
offset_P = 0.
offset_EV = 0.

color_vec=['g','r']

step_prev = 0
for line_counter,line in enumerate(lines):
    
    line = line.replace(" ", "")
    line = line.split(',')
    
    step = int(line[0])
    E11 = float(line[1])
    E22 = float(line[2])
    E33 = float(line[3])
    S11 = float(line[4])
    S22 = float(line[5])
    S33 = float(line[6])
    Q   = float(line[7])
    P   = float(line[8])
    
    
    if ( remove_consolidation_step ):
        
        
        if ( step > 1 ):
            
            if ( not last_consolidation_frame ):
                step_start.append(line_counter)        
                offset_E11 = E11
                offset_E22 = E22
                offset_E33 = E33
                offset_S11 = S11
                offset_S22 = S22
                offset_S33 = S33
                offset_Q = Q
                offset_P = P
                offset_EV = E11+E22+E33
                last_consolidation_frame = True
            # end if
            
            store_step.append(step)
            store_E11.append(E11)
            store_E22.append(E22)
            store_E33.append(E33)
            #store_EV.append(E11+E22+E33)
            store_S11.append(S11)
            store_S22.append(S22)
            store_S33.append(S33)
            store_Q.append(Q)
            store_P.append(P)
            
            
            
        #end if
    else:
        
        if ( step > step_prev ):
            step_start.append(line_counter)
        
        store_step.append(step)
        store_E11.append(E11)
        store_E22.append(E22)
        store_E33.append(E33)
        store_S11.append(S11)
        store_S22.append(S22)
        store_S33.append(S33)
        store_Q.append(Q)
        store_P.append(P)
        
        
    # end if
                
    step_prev = step
        
if ( not remove_consolidation_step ):
    step_end.append(step_start[-1]-1)    
    
step_end.append(line_counter)    


if ( remove_consolidation_step ):
    offset = step_start[0]
    step_start[0] -= offset
    step_end[0] -= offset
    
    color_vec = np.delete(color_vec, 0)
    
# convert to numpy arrays
store_step=np.asarray(store_step)    
store_E11=np.asarray(store_E11)
store_E22=np.asarray(store_E22)
store_E33=np.asarray(store_E33)
#store_EV=np.asarray(store_EV)
store_S11=np.asarray(store_S11)
store_S22=np.asarray(store_S22)
store_S33=np.asarray(store_S33)
store_Q=np.asarray(store_Q)
store_P=np.asarray(store_P)

store_EV= store_E11+store_E22+store_E33

# offset strain
if ( remove_consolidation_step ):
    store_E11 -= offset_E11
    store_E22 -= offset_E22
    store_E33 -= offset_E33
    store_EV  -= offset_EV
    




# ==========
# Plot
# ==========
line_width=4
plt.rc('font',size = 20)
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)
scale=1.2
min_strain = -0.04
max_strain = 0.15

fig = plt.figure(figsize=(20/scale,12/scale))
ax  = plt.subplot(231)
for i in range(0,len(step_start)):
    start_index=step_start[i]
    end_index=step_end[i]
    ax.plot(-store_E33[start_index:end_index],-store_S33[start_index:end_index],'-',
            color=color_vec[i],linewidth=line_width)
    
ax.set_xlabel('Vertical Strain $\epsilon_{33}$')
ax.set_ylabel('Vertical Stress $\sigma_{33}$',rotation=90)
ax.set_xlim((min_strain,max_strain))
ax.set_ylim((-1,12))

ax  = plt.subplot(232)
for i in range(0,len(step_start)):
    start_index=step_start[i]
    end_index=step_end[i]
    ax.plot(-store_E11[start_index:end_index],-store_S11[start_index:end_index],'-',
            color=color_vec[i],linewidth=line_width)
    
ax.set_xlabel('Lateral Strain $\epsilon_{11}$')
ax.set_ylabel('Lateral Stress $\sigma_{11}$',rotation=90)
ax.set_xlim((min_strain,max_strain))
ax.set_ylim((-1,12))

ax  = plt.subplot(233)
for i in range(0,len(step_start)):
    start_index=step_start[i]
    end_index=step_end[i]
    ax.plot(-store_E22[start_index:end_index],-store_S22[start_index:end_index],'-',
            color=color_vec[i],linewidth=line_width)
    
ax.set_xlabel('Lateral Strain $\epsilon_{22}$')
ax.set_ylabel('Lateral Stress $\sigma_{22}$',rotation=90)
ax.set_xlim((min_strain,max_strain))
ax.set_ylim((-1,12))

ax  = plt.subplot(234)
for i in range(0,len(step_start)):
    start_index=step_start[i]
    end_index=step_end[i]
    ax.plot(-store_E33[start_index:end_index],store_Q[start_index:end_index],'-',
            color=color_vec[i],linewidth=line_width)
    
ax.set_xlabel('Vertical Strain $\epsilon_{33}$')
ax.set_ylabel('Shear $q$',rotation=90)
ax.set_xlim((min_strain,max_strain))
ax.set_ylim((-1,10))

ax  = plt.subplot(235)
for i in range(0,len(step_start)):
    start_index=step_start[i]
    end_index=step_end[i]
    ax.plot(-store_P[start_index:end_index],store_Q[start_index:end_index],'-',
            color=color_vec[i],linewidth=line_width)
    
ax.set_xlabel('Pressure $p$')
ax.set_ylabel('Shear $q$',rotation=90)
ax.set_xlim((0,8))
ax.set_ylim((-1,10))

ax  = plt.subplot(236)
for i in range(0,len(step_start)):
    start_index=step_start[i]
    end_index=step_end[i]
    ax.plot(-store_E33[start_index:end_index],store_EV[start_index:end_index],'-',
            color=color_vec[i],linewidth=line_width)
    
ax.set_xlabel('Vertical Strain $\epsilon_{33}$')
ax.set_ylabel('Volumetric Strain $\epsilon_v$',rotation=90)
ax.set_xlim((min_strain,max_strain))
ax.set_xlim((0,0.15))
ax.set_ylim((-0.12,0))

#
#plt.suptitle('Constitutive Model Driver')
#
#fig.subplots_adjust(top=0.94)
##plt.tight_layout()
plt.tight_layout(pad=0, w_pad=0, h_pad=2)
plt.savefig(jobname+'_plot.png', dpi=300)