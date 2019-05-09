# Lesson 2: Predefined Field Variables

Field variables are typically used to: 

* Change the properties of a material because we know <em> a-priori </em> that this change is going to happen. This change could be due to a chemical or some other process, but we are not modeling this process in Abaqus. Rather, we are specifying the <em> effect </em> of this process on the material properties.

* Control the model to a get desired effect, e.g., turn on or off the effects of certain materials.

The model setup for this lesson is identical to that in [Lesson 1](./../01_Lesson), except we now make the following changes. The input file can be found in the "abaqus_input_files" folder above.

## Material definition

The material is defined using the keyword <em> *MATERIAL </em> but <img src="/02_Lesson/tex/84df98c65d88c6adf15d4645ffa25e47.svg?invert_in_darkmode&sanitize=true" align=middle width=13.08219659999999pt height=22.465723500000017pt/> and <img src="/02_Lesson/tex/b49211c7e49541e500c32b4d56d354dc.svg?invert_in_darkmode&sanitize=true" align=middle width=9.16670204999999pt height=14.15524440000002pt/> are now made to vary using field variables.

	*MATERIAL, NAME=M1
	*ELASTIC,DEPENDENCIES=2
	1000.,0.3,,1.0,1.0
	 100.,0.3,,2.0,1.0
	  10.,0.3,,3.0,1.0
	   1.,0.3,,4.0,1.0
	1000.,0.2,,1.0,2.0
	 100.,0.2,,2.0,2.0
	  10.,0.2,,3.0,2.0
	   1.,0.2,,4.0,2.0

The number of field variables is specified using the option <em>DEPENDENCIES</em>. The last two columns of the input correspond to the values of field variables #1 and #2, respectively<sup>[a](#myfootnote1)</sup>. 
	
## Initial conditions on field variables

Field variables #1 and #2 need to be initialized since these do not start from zero. Note that the field variables are initialized at the nodes; each element will then perform an interpolation of the nodal values to obtain the field variable value at the integration points.

	*INITIAL CONDITIONS, TYPE=FIELD, VARIABLE=1
	GLOBAL_NSET,1.0   
	*INITIAL CONDITIONS, TYPE=FIELD, VARIABLE=2
	GLOBAL_NSET,1.0  	   
	
## Analysis steps

There are a total of 3 steps in this analysis. Step 1 is identical to that in [Lesson 1](./../01_Lesson). We define two additional steps to demonstrate how the field variables are used to affect the response of the model.
	
	**********************************************************************
	** Load Step 2
	** Change field variable #1 from 1.0 to 4.0
	**********************************************************************
	*STEP, NLGEOM=NO, INC=99999999
	Change field variable #1
	*STATIC
	0.5,1.0,1.e-12,0.5
	*FIELD, VARIABLE=1
	GLOBAL_NSET,4.0
	*END STEP
	**********************************************************************
	** Load Step 3
	** Change field variable #2 from 1.0 to 2.0
	**********************************************************************
	*STEP, NLGEOM=NO, INC=99999999
	Change field variable #2
	*STATIC
	0.5,1.0,1.e-12,0.5
	*FIELD, VARIABLE=2
	GLOBAL_NSET,2.0
	*END STEP

In Step 2, we change field value of field variable #1 from 1.0 to 4.0. In Step 3, we change field value of field variable #2 from 1.0 to 2.0. As you might guess, these changes will affect the strains or displacements; recall that the (gravity) load is constant.

### Output request

Add output for field variable values:
	
	**********************************************************************
	** Load Step 1 - 1D Compression
	**********************************************************************
	*STEP, NLGEOM=NO, INC=99999999
		...
		...
	*ELEMENT OUTPUT
	E,S
	FV1,FV2	

The input line <em> E,S </em> is the same as in Lesson 1. In the following line, we request that the values of field variables #1 and #2 (<em>FV1</em>, <em>FV2</em>) be made available.
	
We define the output request in Step 1. This output request is then propagated into the following steps. 
	
## Viewing results	

* **Field variables**. We can check that the field variables are correctly initialized and modified through the steps.

| End of Step | Field Variable #1 | Field Variable #2 | 
| :---: | --- | --- | 
| 1 | ![](./abaqus_input_files/1ElementTest_Lesson2_Step1_Frame3_VF1.png) | ![](./abaqus_input_files/1ElementTest_Lesson2_Step1_Frame3_VF2.png) | 
| 2 | ![](./abaqus_input_files/1ElementTest_Lesson2_Step2_Frame3_VF1.png) | ![](./abaqus_input_files/1ElementTest_Lesson2_Step2_Frame3_VF2.png) | 
| 3 | ![](./abaqus_input_files/1ElementTest_Lesson2_Step3_Frame3_VF1.png) | ![](./abaqus_input_files/1ElementTest_Lesson2_Step3_Frame3_VF2.png) | 

* **Displacements**. As in Lesson 1, the vertical strain after Step 1 (gravity) is <img src="/02_Lesson/tex/fcf8c1f48d1ea620135c53b35a252ef2.svg?invert_in_darkmode&sanitize=true" align=middle width=129.66327825pt height=26.76175259999998pt/>.

	In Step 2, the modulus <img src="/02_Lesson/tex/84df98c65d88c6adf15d4645ffa25e47.svg?invert_in_darkmode&sanitize=true" align=middle width=13.08219659999999pt height=22.465723500000017pt/> is dropped from <img src="/02_Lesson/tex/675eeb554f7b336873729327dab98036.svg?invert_in_darkmode&sanitize=true" align=middle width=32.876837399999985pt height=21.18721440000001pt/> to <img src="/02_Lesson/tex/034d0a6be0424bffe9a6e7ac9236c0f5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.219209349999991pt height=21.18721440000001pt/> through field variable <img src="/02_Lesson/tex/8c26e6655aab9ae92411073abc805918.svg?invert_in_darkmode&sanitize=true" align=middle width=21.91788224999999pt height=22.831056599999986pt/>. Therefore, at the end of Step 2, the vertical strain should be <img src="/02_Lesson/tex/675eeb554f7b336873729327dab98036.svg?invert_in_darkmode&sanitize=true" align=middle width=32.876837399999985pt height=21.18721440000001pt/> times larger, at <img src="/02_Lesson/tex/50858148d0f2ac739951de79bb4782ef.svg?invert_in_darkmode&sanitize=true" align=middle width=129.66327825pt height=26.76175259999998pt/>. 	
	Also, the lateral strain <img src="/02_Lesson/tex/a16f48844ce61fa0ca5324a6b58cc2a7.svg?invert_in_darkmode&sanitize=true" align=middle width=62.29450919999999pt height=14.15524440000002pt/> is:
	<p align="center"><img src="/02_Lesson/tex/9a664cf78ef0b558bcc327c9244fbf3b.svg?invert_in_darkmode&sanitize=true" align=middle width=373.89721049999997pt height=32.990165999999995pt/></p>
	
	where <img src="/02_Lesson/tex/9be2903ee179a35a7fad437ee97c1c1f.svg?invert_in_darkmode&sanitize=true" align=middle width=43.219017599999994pt height=22.465723500000017pt/> and <img src="/02_Lesson/tex/2b8463a74b5bbe47c21a0584da185544.svg?invert_in_darkmode&sanitize=true" align=middle width=486.81089820000005pt height=85.29681270000002pt/>E=1<img src="/02_Lesson/tex/8fbae802a2aa6aace902d63bffecd077.svg?invert_in_darkmode&sanitize=true" align=middle width=286.14298184999996pt height=24.7161288pt/>\nu<img src="/02_Lesson/tex/31f2327237f7b31ed37c6f01d2df61c2.svg?invert_in_darkmode&sanitize=true" align=middle width=107.86869554999998pt height=22.831056599999986pt/>0.3<img src="/02_Lesson/tex/5b7ce0b11756ea13938668594c96a288.svg?invert_in_darkmode&sanitize=true" align=middle width=13.90414904999999pt height=20.221802699999984pt/>0.2<img src="/02_Lesson/tex/dbc92bd3fde78a06f5be289e3c35088b.svg?invert_in_darkmode&sanitize=true" align=middle width=154.88865975pt height=22.831056599999986pt/>\#2<img src="/02_Lesson/tex/cb12151c03ada6d8e7b3cd409f6a6495.svg?invert_in_darkmode&sanitize=true" align=middle width=360.2829944999999pt height=22.831056599999986pt/><img src="/02_Lesson/tex/8bfb08a9f927d62a8451584e32e86d54.svg?invert_in_darkmode&sanitize=true" align=middle width=8.21920935pt height=14.15524440000002pt/><img src="/02_Lesson/tex/616d4c00d60a668183b23782fa41cbe8.svg?invert_in_darkmode&sanitize=true" align=middle width=30.182742149999992pt height=39.45205439999997pt/>E = 1<img src="/02_Lesson/tex/fd92a53167b3c6ae9574071613d555dc.svg?invert_in_darkmode&sanitize=true" align=middle width=27.11199479999999pt height=22.831056599999986pt/>\nu = 0.2<img src="/02_Lesson/tex/bdb86e7267672cfac6fcec66fef3bdd7.svg?invert_in_darkmode&sanitize=true" align=middle width=486.81089820000005pt height=118.35616650000001pt/>\epsilon_{33}<img src="/02_Lesson/tex/19efe8c03ad1a17b7f19b5b086069707.svg?invert_in_darkmode&sanitize=true" align=middle width=357.97459994999997pt height=22.831056599999986pt/>\epsilon_{33}<img src="/02_Lesson/tex/7a54972854c0eaec7d41e45bc156c747.svg?invert_in_darkmode&sanitize=true" align=middle width=700.2745645499999pt height=282.55708469999996pt/>N_1,\hdots,N_{nv}<img src="/02_Lesson/tex/9e204235bccb82794e0e97f50e41640c.svg?invert_in_darkmode&sanitize=true" align=middle width=273.7524339pt height=22.831056599999986pt/>nv<img src="/02_Lesson/tex/a32bee6e910695da6e2a2ce2e1bb1893.svg?invert_in_darkmode&sanitize=true" align=middle width=247.66845675000002pt height=22.831056599999986pt/>N_1 \times N_2 \times N_{nv}<img src="/02_Lesson/tex/b879b2028552ba040d64509809b6ff7c.svg?invert_in_darkmode&sanitize=true" align=middle width=51.46135334999998pt height=22.831056599999986pt/>N_{nv}$ columns. Therefore, if the number of field variables is large, this table becomes quite big. It may be more convenient to actually write a subroutine to vary the field variables (not covered in this training). In most cases, however, one or two field variables are used.

---
## Additional Comments on This Lesson (Links to Milo)
None

