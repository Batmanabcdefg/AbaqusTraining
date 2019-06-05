# To use this file
#  abaqus python post_process.py
#
from odbAccess import *
from odbMaterial import *
from odbSection import *
from abaqusConstants import *
import numpy as np

odbName='1Element_TXC_StrainControl_HSMXilin_Mat2.odb'

odb = openOdb(odbName)
assembly = odb.rootAssembly

elementSet = odb.rootAssembly.instances['PART-1-1'].elementSets['P1']

store_strain_major      = []
store_strain_volumetric = []
store_press_stress = []
store_shear_stress = []
store_stress_ratio = []
store_min_detA = []
store_N1 = []
store_N2 = []
store_N3 = []

	
print 'Processing Step:', odb.steps['Step-2'].number

index=0
integ_point=0

for frame in odb.steps['Step-2'].frames:

    print 'Frame:', index
    StrainSet = frame.fieldOutputs['E']
    StressSet = frame.fieldOutputs['S']
    
    E1 = StrainSet.values[integ_point].data[0] # E11
    E2 = StrainSet.values[integ_point].data[1] # E22
    E3 = StrainSet.values[integ_point].data[2] # E33
    
    EV = E1+E2+E3
	
    S1 = StressSet.values[integ_point].data[0] # S11
    S2 = StressSet.values[integ_point].data[1] # S22
    S3 = StressSet.values[integ_point].data[2] # S33
    #print S1,S3
    StressRatio = S1/S3
    P = (S1+S2+S3)/3.0
    Q = sqrt( 0.5*( (S1-S2)**2+(S2-S3)**2+(S3-S1)**2 ) )
    print Q
    
    store_strain_major.append(-E1*100) # make percent and make compression as +ve
    store_strain_volumetric.append(EV*100) # make percent, +ve is dilation
    store_stress_ratio.append(StressRatio)
    store_shear_stress.append(Q)
    store_press_stress.append(P)
    
    index=index+1


# history output	
# index=0
# integ_point=0	
# key = odb.steps['Step-2'].historyRegions.keys()[integ_point]
# min_detA_data = odb.steps['Step-2'].historyRegions[key].historyOutputs['SDV9'].data
# N1_data = odb.steps['Step-2'].historyRegions[key].historyOutputs['SDV10'].data
# N2_data = odb.steps['Step-2'].historyRegions[key].historyOutputs['SDV11'].data
# N3_data = odb.steps['Step-2'].historyRegions[key].historyOutputs['SDV12'].data
# for i in range(0,len(min_detA_data)):
    # store_min_detA.append(min_detA_data[i][1])
    # store_N1.append(N1_data[i][1])
    # store_N2.append(N2_data[i][1])
    # store_N3.append(N3_data[i][1])
	
	
# Close the output database before exiting the program
odb.close()

numdata = len(store_strain_major)

# offset
S0 = store_shear_stress[0]
E0 = store_strain_major[0]
EV0 = store_strain_volumetric[0]

for i in range(0,numdata):
	store_strain_major[i] = store_strain_major[i]-E0
	store_strain_volumetric[i] = store_strain_volumetric[i]-EV0
	store_shear_stress[i] = store_shear_stress[i]-S0
	

f = open('results.dat', 'w')
#f.write('Convention: axial strains are positive in compression, volumetric strain is positive for dilation\n')
#f.write('Step    Major Strain E11(%)  Volumetric Strain Ev(%)    Shear Q\n')
for i in range(0,numdata):
#	f.write('%d %20.8e %20.8e %20.8e %20.8e %20.8e %20.8e %20.8e %20.8e\n'%(i,store_strain_major[i],store_strain_volumetric[i],store_shear_stress[i],store_stress_ratio[i],store_min_detA[i],store_N1[i],store_N2[i],store_N3[i]))
	f.write('%d %20.8e %20.8e %20.8e %20.8e\n'%(i,store_strain_major[i],store_strain_volumetric[i],store_shear_stress[i],store_press_stress[i]))
	
f.close()
