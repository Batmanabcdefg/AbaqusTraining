#
# Project XXXX
#
# Revision History
# 000: New Script
#
# Use: abaqus viewer script=post_process_plots.py
#
#

from abaqus import *
from abaqusConstants import *
from viewerModules import *
from driverUtils import executeOnCaeStartup
import sys
#executeOnCaeStartup()

#create viewport
v=session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=300, height=150)
v.makeCurrent()
v.restore()
#v.maximize()

# ====================================================================
Jobname     = '1ElementTest_Lesson1'
ODBFile     = Jobname+'.odb'
StepNo      = 1
# ====================================================================

#open ODB
odb  = session.openOdb(name=ODBFile)

# view options
v.setValues(displayedObject=odb)
v.enableMultipleColors()
v.setColor(initialColor='#BDBDBD')
cmap=v.colorMappings['Section']
cmap.updateOverrides(overrides={'PART-1-1.PDD_1MM.Section-PDD_1MM':(True, '#999999', 'Default', '#999999')})
v.disableMultipleColors()
v.viewportAnnotationOptions.setValues(titleBackgroundStyle=MATCH, stateBackgroundStyle=MATCH, legendBackgroundStyle=MATCH,compass=OFF)
v.odbDisplay.basicOptions.setValues(connectorDisplay=OFF)
session.printOptions.setValues(reduceColors=False)
session.printOptions.setValues(vpDecorations=OFF)
v.odbDisplay.commonOptions.setValues(visibleEdges=FREE) 

# paralel projection view
v.view.setProjection(projection=PARALLEL)

# fit view
session.viewports['Viewport: 1'].view.fitView()

# rotate model so that vertical Z is up
session.viewports['Viewport: 1'].view.rotate(xAngle=-90, yAngle=0, zAngle=0, mode=MODEL)
	
StepName = 'Step-'+str(StepNo)
frames = odb.steps[StepName].frames
nframes = len(frames)

#output frame numbers 
fNum = [nframes]
fLabel = ['Step'+str(StepNo)]

for i in range(0,len(fNum)):
	
	# set frame
	session.viewports[session.currentViewportName].odbDisplay.setFrame(step=StepName, frame=fNum[i])
	
	# view element
	leaf = dgo.LeafFromElementSets(elementSets=("PART-1-1.P1", ))
	session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)	
	
	# title block
	session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(titleBackgroundStyle=TRANSPARENT)
	
	# state block
	session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(stateBackgroundStyle=TRANSPARENT)	
	
	#v.odbDisplay.commonOptions.setValues(edgeLineThickness=VERY_THIN)
	session.printOptions.setValues(vpBackground=OFF)
	
	# no title
	session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(title=OFF)
	
	# deformation scale factor
	session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(deformationScaling=UNIFORM, uniformScaleFactor=1)
	
	# set legend font size
	session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(legendFont='-*-verdana-medium-r-normal-*-*-120-*-*-p-*-*-*')

	# legend - no bounding box
	session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(legendBox=OFF)
	
	# ========================================
	# plot stress q
	# ========================================
	v.odbDisplay.setPrimaryVariable(variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 'Mises'), )
	v.odbDisplay.display.setValues(plotState=CONTOURS_ON_DEF)
	v.odbDisplay.contourOptions.setValues(spectrum='Rainbow', maxAutoCompute=ON, maxValue=0, minAutoCompute=ON, minValue=0, showMinLocation=OFF, showMaxLocation=OFF)
	
	# output to TIFF file
	session.printToFile(fileName=Jobname+'_'+fLabel[i]+'_VMS', format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))
	
	# ========================================
	# plot stress S33
	# ========================================
	v.odbDisplay.setPrimaryVariable(variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 'S33'))
	v.odbDisplay.display.setValues(plotState=CONTOURS_ON_DEF)
	v.odbDisplay.contourOptions.setValues(spectrum='Rainbow', maxAutoCompute=ON, maxValue=0, minAutoCompute=ON, minValue=0, showMinLocation=OFF, showMaxLocation=OFF)
	
	# output to TIFF file
	session.printToFile(fileName=Jobname+'_'+fLabel[i]+'_S33', format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))
	
	# ========================================
	# plot reaction force
	# ========================================
	v.odbDisplay.setPrimaryVariable(variableLabel='RF', outputPosition=NODAL, refinement=(COMPONENT, 'RF3'))
	v.odbDisplay.display.setValues(plotState=CONTOURS_ON_DEF)
	v.odbDisplay.contourOptions.setValues(spectrum='Rainbow', maxAutoCompute=ON, maxValue=0, minAutoCompute=ON, minValue=0, showMinLocation=OFF, showMaxLocation=OFF)
	
	# output to TIFF file
	session.printToFile(fileName=Jobname+'_'+fLabel[i]+'_RF3', format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))
	
	# ========================================
	# plot displacement
	# ========================================
	v.odbDisplay.setPrimaryVariable(variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'))
	v.odbDisplay.display.setValues(plotState=CONTOURS_ON_DEF)
	v.odbDisplay.contourOptions.setValues(spectrum='Rainbow', maxAutoCompute=ON, maxValue=0, minAutoCompute=ON, minValue=0, showMinLocation=OFF, showMaxLocation=OFF)
	
	# output to TIFF file
	session.printToFile(fileName=Jobname+'_'+fLabel[i]+'_U3', format=PNG, canvasObjects=(session.viewports['Viewport: 1'], ))
	
	

odb.close()

sys.exit()