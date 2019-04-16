# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2018 replay file
# Internal Version: 2017_11_07-09.21.41 127140
# Run by klim on Mon Apr 15 18:02:56 2019
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
execfile('post_process_plots.py', __main__.__dict__)
#: Model: C:/Users/klim/Desktop/SGH/GITHUB/AbaqusTraining/01_Lesson/abaqus_input_files/1ElementTest_Lesson1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          2
#: Number of Steps:              1
#* Exit code: 0
#* File "post_process_plots.py", line 134, in <module>
#*     sys.exit()
