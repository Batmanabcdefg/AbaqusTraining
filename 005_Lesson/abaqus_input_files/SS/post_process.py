# To use this file
#  abaqus python post_process.py
#
from odbAccess import *
from odbMaterial import *
from odbSection import *
from abaqusConstants import *
import numpy as np

odbName='Lesson005_1Element_TXC.odb'
step_vec = [1,2]

odb = openOdb(odbName)
assembly = odb.rootAssembly

elementSet = odb.rootAssembly.instances['PART-1-1'].elementSets['P1']

store_E11 = []
store_E22 = []
store_E33 = []
store_S11 = []
store_S22 = []
store_S33 = []
store_Q = []
store_P = []

	
integ_point=0

for step in step_vec:
	
	step_name = 'Step-'+str(step)
	print 'Processing Step:', odb.steps[step_name].number
		
	for frame in odb.steps[step_name].frames:

		print('Frame: %f'%frame.frameValue)
		StrainSet = frame.fieldOutputs['E']
		StressSet = frame.fieldOutputs['S']
		E11 = StrainSet.values[integ_point].data[0] # E11
		E22 = StrainSet.values[integ_point].data[1] # E22
		E33 = StrainSet.values[integ_point].data[2] # E33
		
		S11 = StressSet.values[integ_point].data[0] # S11
		S22 = StressSet.values[integ_point].data[1] # S22
		S33 = StressSet.values[integ_point].data[2] # S33
		
		#print S1,S3
		P = (S11+S22+S33)/3.0
		Q = sqrt( 0.5*( (S11-S22)**2+(S22-S33)**2+(S33-S11)**2 ) )
		print('p = %f, q = %f'%(P,Q))
		
		store_E11.append(E11) 
		store_E22.append(E22) 
		store_E33.append(E33) 		
		store_S11.append(S11) 
		store_S22.append(S22) 
		store_S33.append(S33) 
		store_Q.append(Q) 
		store_P.append(P) 
		
		
	# end frame

# end step
		


		
	
# Close the output database before exiting the program
odb.close()

numdata = len(store_E11)

# offset
#S0  = store_shear_stress[0]
#E0  = store_strain_major[0]
#EV0 = store_strain_volumetric[0]
#for i in range(0,numdata):
#	store_strain_major[i]      = store_strain_major[i]-E0
#	store_strain_volumetric[i] = store_strain_volumetric[i]-EV0
#	store_shear_stress[i]      = store_shear_stress[i]-S0
	

f = open('results.dat', 'w')
for i in range(0,numdata):
	f.write('%d, %20.8e, %20.8e, %20.8e, %20.8e, %20.8e, %20.8e, %20.8e, %20.8e\n'
			%(i,store_E11[i],store_E22[i],store_E33[i],
			  store_S11[i],store_S22[i],store_S33[i],
			  store_Q[i],store_P[i]))
	
f.close()
