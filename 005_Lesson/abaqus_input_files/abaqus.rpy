# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2018 replay file
# Internal Version: 2017_11_07-09.21.41 127140
# Run by klim on Wed Jun  5 14:28:27 2019
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=317.594787597656, 
    height=180.603713989258)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o1 = session.openOdb(
    name='C:/Users/klim/Desktop/SGH/GITHUB/AbaqusTraining/005_Lesson/abaqus_input_files/Lesson005_1Element_TXC.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: C:/Users/klim/Desktop/SGH/GITHUB/AbaqusTraining/005_Lesson/abaqus_input_files/Lesson005_1Element_TXC.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          5
#: Number of Steps:              2
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1)
session.odbs['C:/Users/klim/Desktop/SGH/GITHUB/AbaqusTraining/005_Lesson/abaqus_input_files/Lesson005_1Element_TXC.odb'].close(
    )
