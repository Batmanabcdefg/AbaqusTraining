# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2018 replay file
# Internal Version: 2017_11_07-09.21.41 127140
# Run by klim on Mon Apr 22 12:07:26 2019
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=230.66667175293, 
    height=122.507400512695)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execfile('post_process_plots.py', __main__.__dict__)
#: Model: C:/Users/klim/Desktop/SGH/GITHUB/AbaqusTraining/02_Lesson/abaqus_input_files/1ElementTest_Lesson2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          2
#: Number of Steps:              3
#* Exit code: 0
#* File "post_process_plots.py", line 169, in <module>
#*     sys.exit()
