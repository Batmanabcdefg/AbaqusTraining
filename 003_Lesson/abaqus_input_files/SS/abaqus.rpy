# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2018 replay file
# Internal Version: 2017_11_07-09.21.41 127140
# Run by klim on Thu May  2 15:16:53 2019
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
    name='C:/Users/klim/Desktop/SGH/GITHUB/AbaqusTraining/03_Lesson/abaqus_input_files/ContactInteractions2.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: C:/Users/klim/Desktop/SGH/GITHUB/AbaqusTraining/03_Lesson/abaqus_input_files/ContactInteractions2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          2
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.65264, 
    farPlane=8.18611, width=5.43249, height=2.22865, cameraPosition=(6.57656, 
    -1.33103, 1.39546), cameraUpVector=(-0.182028, 0.844758, 0.50324), 
    cameraTarget=(0.57619, 0.405946, 0.490189))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.65945, 
    farPlane=8.26894, width=5.44045, height=2.23191, cameraPosition=(3.10394, 
    -5.40759, 0.0868086), cameraUpVector=(0.0520309, 0.326972, 0.943601), 
    cameraTarget=(0.518091, 0.337743, 0.468295))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.84629, 
    farPlane=8.14791, width=5.65861, height=2.32141, cameraPosition=(1.20856, 
    -5.63857, 2.43388), cameraUpVector=(-0.112323, 0.593519, 0.796943), 
    cameraTarget=(0.473457, 0.332304, 0.523565))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.80604, 
    farPlane=8.16189, width=5.61162, height=2.30213, cameraPosition=(1.66582, 
    -5.85444, 0.982702), cameraUpVector=(-0.0944529, 0.396346, 0.91323), 
    cameraTarget=(0.486486, 0.326153, 0.482216))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.79903, 
    farPlane=8.19056, width=5.60344, height=2.29877, cameraPosition=(1.44486, 
    -5.61769, 2.3924), cameraUpVector=(-0.117438, 0.586751, 0.801206), 
    cameraTarget=(0.480625, 0.332433, 0.519608))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.80673, 
    farPlane=8.18633, width=5.61243, height=2.30246, cameraPosition=(1.38244, 
    -5.56154, 2.59088), cameraUpVector=(-0.117426, 0.612714, 0.781533), 
    cameraTarget=(0.478868, 0.334013, 0.525195))
session.Viewport(name='Viewport: 2', origin=(6.36250019073486, 
    -4.50185203552246), width=405.079193115234, height=178.75)
session.viewports['Viewport: 2'].makeCurrent()
session.viewports['Viewport: 2'].maximize()
session.viewports['Viewport: 1'].restore()
session.viewports['Viewport: 2'].restore()
session.viewports['Viewport: 1'].setValues(origin=(0.0, -4.50184631347656), 
    width=225.603652954102, height=185.105560302734)
session.viewports['Viewport: 2'].setValues(origin=(225.603652954102, 
    -4.50184631347656), width=225.603652954102, height=185.105560302734)
session.viewports['Viewport: 1'].makeCurrent()
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
session.odbs['C:/Users/klim/Desktop/SGH/GITHUB/AbaqusTraining/03_Lesson/abaqus_input_files/ContactInteractions.odb'].close(
    )
odb = session.odbs['C:/Users/klim/Desktop/SGH/GITHUB/AbaqusTraining/03_Lesson/abaqus_input_files/ContactInteractions2.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
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
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.71608, 
    farPlane=7.95771, width=2.8472, height=2.25904, cameraPosition=(2.15041, 
    -2.2946, 5.96807), cameraUpVector=(-0.0292802, 0.991981, 0.122946), 
    cameraTarget=(0.554658, 0.455123, 0.515219))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.73168, 
    farPlane=7.99374, width=2.85662, height=2.26651, cameraPosition=(-0.179227, 
    -5.81132, 0.965199), cameraUpVector=(0.118942, 0.391258, 0.912563), 
    cameraTarget=(0.545495, 0.441291, 0.495542))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.80826, 
    farPlane=7.91716, width=2.2664, height=1.79822, viewOffsetX=-0.000378384, 
    viewOffsetY=0.130024)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.92841, 
    farPlane=7.80833, width=2.32303, height=1.84315, cameraPosition=(0.422991, 
    -5.85476, 0.937333), cameraUpVector=(0.141467, 0.395135, 0.907665), 
    cameraTarget=(0.540413, 0.440698, 0.496449), viewOffsetX=-0.00038784, 
    viewOffsetY=0.133274)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.96388, 
    farPlane=7.77286, width=1.94336, height=1.54191, viewOffsetX=-0.0124096, 
    viewOffsetY=0.198265)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.94754, 
    farPlane=7.77805, width=1.93696, height=1.53683, cameraPosition=(0.182131, 
    -5.84704, 0.844932), cameraUpVector=(0.135334, 0.37757, 0.916038), 
    cameraTarget=(0.543383, 0.444858, 0.495019), viewOffsetX=-0.0123688, 
    viewOffsetY=0.197612)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.76315, 
    farPlane=8.02617, width=1.86477, height=1.47956, cameraPosition=(-0.900557, 
    -5.54733, 2.06331), cameraUpVector=(0.135469, 0.538032, 0.831967), 
    cameraTarget=(0.54977, 0.396678, 0.512099), viewOffsetX=-0.0119078, 
    viewOffsetY=0.190247)
session.odbs['C:/Users/klim/Desktop/SGH/GITHUB/AbaqusTraining/03_Lesson/abaqus_input_files/ContactInteractions.odb'].close(
    )
odb = session.odbs['C:/Users/klim/Desktop/SGH/GITHUB/AbaqusTraining/03_Lesson/abaqus_input_files/ContactInteractions2.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.82626, 
    farPlane=7.71483, width=2.91372, height=2.31182, cameraPosition=(1.74137, 
    -1.05984, 6.51404), cameraUpVector=(0.0345198, 0.994093, -0.102899), 
    cameraTarget=(0.564417, 0.47561, 0.505869))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.38753, 
    farPlane=8.16227, width=2.64885, height=2.10167, cameraPosition=(-2.01478, 
    -5.185, -0.290783), cameraUpVector=(0.135146, 0.163436, 0.977253), 
    cameraTarget=(0.58923, 0.502861, 0.550822))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.40898, 
    farPlane=8.12201, width=2.6618, height=2.11195, cameraPosition=(-2.29441, 
    -5.06566, 1.25961), cameraUpVector=(0.178594, 0.401182, 0.898419), 
    cameraTarget=(0.590882, 0.502156, 0.541663))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.28849, 
    farPlane=8.24251, width=3.54224, height=2.8105, viewOffsetX=-0.086703, 
    viewOffsetY=-0.0566068)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.15502, 
    farPlane=8.29551, width=3.43199, height=2.72303, cameraPosition=(-2.09128, 
    -4.275, 3.60842), cameraUpVector=(0.201627, 0.737134, 0.644966), 
    cameraTarget=(0.594103, 0.537396, 0.530998), viewOffsetX=-0.0840045, 
    viewOffsetY=-0.054845)
session.viewports['Viewport: 2'].view.setValues(nearPlane=4.77033, 
    farPlane=8.22273, width=2.82004, height=2.2375, viewOffsetX=0.247313, 
    viewOffsetY=-0.0513187)
session.viewports['Viewport: 2'].view.setValues(nearPlane=4.78191, 
    farPlane=8.31109, width=2.82689, height=2.24293, cameraPosition=(2.42455, 
    -5.73761, 0.9276), cameraUpVector=(-0.138502, 0.374616, 0.916777), 
    cameraTarget=(0.521978, 0.264325, 0.482628), viewOffsetX=0.247913, 
    viewOffsetY=-0.0514433)
session.viewports['Viewport: 2'].view.setValues(nearPlane=4.77247, 
    farPlane=8.2667, width=2.82131, height=2.2385, cameraPosition=(1.86016, 
    -5.68258, 1.98666), cameraUpVector=(-0.140754, 0.525271, 0.839213), 
    cameraTarget=(0.492721, 0.302048, 0.518569), viewOffsetX=0.247424, 
    viewOffsetY=-0.0513417)
session.odbs['C:/Users/klim/Desktop/SGH/GITHUB/AbaqusTraining/03_Lesson/abaqus_input_files/ContactInteractions.odb'].close(
    )
odb = session.odbs['C:/Users/klim/Desktop/SGH/GITHUB/AbaqusTraining/03_Lesson/abaqus_input_files/ContactInteractions2.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.40268, 
    farPlane=8.1303, width=2.658, height=2.10892, cameraPosition=(-1.35145, 
    -4.27596, 4.17906), cameraUpVector=(0.130482, 0.818769, 0.5591), 
    cameraTarget=(0.576698, 0.488381, 0.515141))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.66544, 
    farPlane=7.93272, width=2.81664, height=2.23479, cameraPosition=(0.775067, 
    -5.2293, 3.17278), cameraUpVector=(0.0021206, 0.698789, 0.715325), 
    cameraTarget=(0.561264, 0.4953, 0.522445))
session.viewports['Viewport: 2'].makeCurrent()
session.odbs['C:/Users/klim/Desktop/SGH/GITHUB/AbaqusTraining/03_Lesson/abaqus_input_files/ContactInteractions.odb'].close(
    )
session.viewports['Viewport: 1'].makeCurrent()
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
session.animationController.setValues(animationType=SCALE_FACTOR, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.animationController.setValues(animationType=NONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.97384, 
    farPlane=7.50865, width=3.00282, height=2.38251, cameraPosition=(-0.369106, 
    -0.0629154, 6.7234), cameraUpVector=(0.221593, 0.949255, -0.223183), 
    cameraTarget=(0.572797, 0.471651, 0.505038))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.32422, 
    farPlane=8.16515, width=2.61063, height=2.07134, cameraPosition=(-2.05435, 
    -5.10147, -0.480586), cameraUpVector=(0.217093, 0.0873657, 0.972234), 
    cameraTarget=(0.591894, 0.528748, 0.586673))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.29042, 
    farPlane=8.17304, width=2.59022, height=2.05515, cameraPosition=(-2.58494, 
    -4.028, -2.40156), cameraUpVector=(0.0980955, -0.244414, 0.964696), 
    cameraTarget=(0.597611, 0.517181, 0.607372))
session.odbs['C:/Users/klim/Desktop/SGH/GITHUB/AbaqusTraining/03_Lesson/abaqus_input_files/ContactInteractions2.odb'].close(
    )
session.odbs['C:/Users/klim/Desktop/SGH/GITHUB/AbaqusTraining/03_Lesson/abaqus_input_files/ContactInteractions.odb'].close(
    )
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
session.odbs['C:/Users/klim/Desktop/SGH/GITHUB/AbaqusTraining/03_Lesson/abaqus_input_files/ContactInteractions.odb'].close(
    )
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.64509, 
    farPlane=7.90919, width=2.80434, height=2.22503, cameraPosition=(1.59138, 
    -2.76755, 5.8197), cameraUpVector=(0.208308, 0.965713, 0.154941), 
    cameraTarget=(0.565835, 0.484559, 0.508102))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.48396, 
    farPlane=8.08059, width=2.70706, height=2.14785, cameraPosition=(-0.812284, 
    -5.36751, 2.395), cameraUpVector=(0.295195, 0.539665, 0.78843), 
    cameraTarget=(0.579174, 0.498988, 0.527107))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.35002, 
    farPlane=8.10268, width=2.6262, height=2.08369, cameraPosition=(-4.95652, 
    -2.37942, 1.4125), cameraUpVector=(0.428254, 0.176481, 0.886258), 
    cameraTarget=(0.598763, 0.484864, 0.531751))
session.animationController.setValues(animationType=SCALE_FACTOR, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.animationController.setValues(animationType=NONE)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=UNIFORM, uniformScaleFactor=1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.74504, 
    farPlane=7.23329, width=2.86468, height=2.27291, cameraPosition=(0.640404, 
    0.325703, 6.74496), cameraUpVector=(0.776486, 0.529406, -0.341759), 
    cameraTarget=(0.497801, 0.436067, 0.43556))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3.92576, 
    farPlane=7.94849, width=2.37006, height=1.88047, cameraPosition=(-3.69179, 
    4.58341, 1.76271), cameraUpVector=(0.45533, -0.228684, 0.860452), 
    cameraTarget=(0.731302, 0.20658, 0.704099))
