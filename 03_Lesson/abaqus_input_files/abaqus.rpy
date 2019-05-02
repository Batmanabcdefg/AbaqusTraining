# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2018 replay file
# Internal Version: 2017_11_07-09.21.41 127140
# Run by klim on Thu May  2 16:44:09 2019
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=339.333343505859, 
    height=180.603713989258)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o1 = session.openOdb(
    name='C:/Users/klim/Desktop/SGH/GITHUB/AbaqusTraining/03_Lesson/abaqus_input_files/ContactInteractions.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: C:/Users/klim/Desktop/SGH/GITHUB/AbaqusTraining/03_Lesson/abaqus_input_files/ContactInteractions.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          2
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.6206, 
    farPlane=8.20836, width=5.39508, height=2.21331, cameraPosition=(6.45459, 
    -1.8701, 0.140507), cameraUpVector=(-0.119601, 0.487993, 0.864614), 
    cameraTarget=(0.575097, 0.401033, 0.478803))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.56009, 
    farPlane=8.29215, width=5.32442, height=2.18432, cameraPosition=(5.86088, 
    -3.01866, -0.00517243), cameraUpVector=(-0.0216828, 0.459055, 0.888143), 
    cameraTarget=(0.565609, 0.382677, 0.476475))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.65866, 
    farPlane=8.19359, width=3.99208, height=1.63773, viewOffsetX=0.0331668, 
    viewOffsetY=0.0828265)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.81093, 
    farPlane=8.03307, width=4.12256, height=1.69126, cameraPosition=(6.62634, 
    -1.20569, -0.475854), cameraUpVector=(-0.0926737, 0.433207, 0.896517), 
    cameraTarget=(0.596394, 0.40196, 0.470842), viewOffsetX=0.0342509, 
    viewOffsetY=0.0855337)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='RF', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='RF', outputPosition=NODAL, refinement=(COMPONENT, 'RF3'))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.85031, 
    farPlane=7.94927, width=4.1563, height=1.7051, cameraPosition=(6.53443, 
    -0.3842, -1.51654), cameraUpVector=(0.00212787, 0.302571, 0.953124), 
    cameraTarget=(0.590534, 0.423906, 0.447663), viewOffsetX=0.0345313, 
    viewOffsetY=0.0862338)
