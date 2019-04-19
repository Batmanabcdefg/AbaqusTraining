# Lesson 2: Predefined Field Variables

Field variables are typically used to: 

* Indirectly model some prescribed response 
* Control the response of the model in some way to get desired effect

The problem setup (geometry and loading) is identical to that in Lesson 1, with the following exceptions:

## Material definition

The material is defined using the keyword <em> *MATERIAL </em> but this time, ...

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

## Initial conditions on field variables

	Initialize field variables #1 and #2. Note that the field variables are initialized at the nodes; each element will then perform an interpolation of the nodal values to obtain the field variable value at the integration points.

	*INITIAL CONDITIONS, TYPE=FIELD, VARIABLE=1
	GLOBAL_NSET,1.0   
	*INITIAL CONDITIONS, TYPE=FIELD, VARIABLE=2
	GLOBAL_NSET,1.0  	   

	
## Analysis steps

	There are a total of 3 steps in this analysis. Step 1 is identical to that in Lesson 1. We define two additional steps to demonstrate how the field variables are used to affect the response of the model.
	
	**********************************************************************
	** Load Step 2
	** Hold displacement and change field Variable #1 from 1.0 to 4.0
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
	** Hold displacement and change field Variable #2 from 1.0 to 2.0
	**********************************************************************
	*STEP, NLGEOM=NO, INC=99999999
	Change field variable #2
	*STATIC
	0.5,1.0,1.e-12,0.5
	*FIELD, VARIABLE=2
	GLOBAL_NSET,2.0
	*END STEP

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

	The second line is the same as in Lesson 1. In the third line, 
	We define the output request in step 1. This request will be propagated into the following steps.
	
## Viewing results	

* **Field variables**. We can check that the field variables are properly initialized and modified through the steps.

* **Displacements**. As in Lesson 1, the vertical strain after Step 1 (gravity) is <img src="/02_Lesson/tex/fcf8c1f48d1ea620135c53b35a252ef2.svg?invert_in_darkmode&sanitize=true" align=middle width=129.66327825pt height=26.76175259999998pt/>.

	In Step 2, the modulus <img src="/02_Lesson/tex/84df98c65d88c6adf15d4645ffa25e47.svg?invert_in_darkmode&sanitize=true" align=middle width=13.08219659999999pt height=22.465723500000017pt/> is dropped from <img src="/02_Lesson/tex/675eeb554f7b336873729327dab98036.svg?invert_in_darkmode&sanitize=true" align=middle width=32.876837399999985pt height=21.18721440000001pt/> to <img src="/02_Lesson/tex/034d0a6be0424bffe9a6e7ac9236c0f5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.219209349999991pt height=21.18721440000001pt/> through field variable <img src="/02_Lesson/tex/8c26e6655aab9ae92411073abc805918.svg?invert_in_darkmode&sanitize=true" align=middle width=21.91788224999999pt height=22.831056599999986pt/>. Therefore, at the end of Step 2, the vertical strain should be <img src="/02_Lesson/tex/675eeb554f7b336873729327dab98036.svg?invert_in_darkmode&sanitize=true" align=middle width=32.876837399999985pt height=21.18721440000001pt/> times larger, at <img src="/02_Lesson/tex/50858148d0f2ac739951de79bb4782ef.svg?invert_in_darkmode&sanitize=true" align=middle width=129.66327825pt height=26.76175259999998pt/>. 	
	Also, the lateral strain <img src="/02_Lesson/tex/a16f48844ce61fa0ca5324a6b58cc2a7.svg?invert_in_darkmode&sanitize=true" align=middle width=62.29450919999999pt height=14.15524440000002pt/> is:
	<p align="center"><img src="/02_Lesson/tex/9a664cf78ef0b558bcc327c9244fbf3b.svg?invert_in_darkmode&sanitize=true" align=middle width=373.89721049999997pt height=32.990165999999995pt/></p>
	
	where <img src="/02_Lesson/tex/9be2903ee179a35a7fad437ee97c1c1f.svg?invert_in_darkmode&sanitize=true" align=middle width=43.219017599999994pt height=22.465723500000017pt/> and <img src="/02_Lesson/tex/15c1721523b4a6c9de5c6579ea380fdd.svg?invert_in_darkmode&sanitize=true" align=middle width=52.088957249999986pt height=21.18721440000001pt/>.	These values jibe with the contour plots below.
	
	![](./abaqus_input_files/1ElementTest_Lesson2Step_2_Frame3_E22.png	)
	
	In Step 3, the modulus <img src="/02_Lesson/tex/1a4fb486f854c2b4efad46a2f5ed93c6.svg?invert_in_darkmode&sanitize=true" align=middle width=43.219017599999994pt height=22.465723500000017pt/> is kept constant, while the Poisson's ratio <img src="/02_Lesson/tex/b49211c7e49541e500c32b4d56d354dc.svg?invert_in_darkmode&sanitize=true" align=middle width=9.16670204999999pt height=14.15524440000002pt/> is dropped from <img src="/02_Lesson/tex/5a2912de5997e53d19e8044db54d76e3.svg?invert_in_darkmode&sanitize=true" align=middle width=21.00464354999999pt height=21.18721440000001pt/> to <img src="/02_Lesson/tex/358d4d0949e47523757b4bc797ab597e.svg?invert_in_darkmode&sanitize=true" align=middle width=21.00464354999999pt height=21.18721440000001pt/> through field variable <img src="/02_Lesson/tex/fb19066311f84c5909400aa479652a43.svg?invert_in_darkmode&sanitize=true" align=middle width=21.91788224999999pt height=22.831056599999986pt/>. Therefore, at the end of Step 3, the lateral strain is:
	
	<p align="center"><img src="/02_Lesson/tex/fd7bce942625b3c8ca160aa45fc30f29.svg?invert_in_darkmode&sanitize=true" align=middle width=373.89721049999997pt height=32.990165999999995pt/></p>
			
	where <img src="/02_Lesson/tex/9be2903ee179a35a7fad437ee97c1c1f.svg?invert_in_darkmode&sanitize=true" align=middle width=43.219017599999994pt height=22.465723500000017pt/> and <img src="/02_Lesson/tex/a30bb2b6b987e9176d707426add7226a.svg?invert_in_darkmode&sanitize=true" align=middle width=52.088957249999986pt height=21.18721440000001pt/>.	These values jibe with the contour plots below.

	![](./abaqus_input_files/1ElementTest_Lesson2Step_3_Frame3_E22.png	)

## Exercise 

* The vertical strain <img src="/02_Lesson/tex/fb693681620c7d77e353de0fea217589.svg?invert_in_darkmode&sanitize=true" align=middle width=19.777485749999993pt height=14.15524440000002pt/> did not change during Step 3. Why? Hint: Calculate <img src="/02_Lesson/tex/fb693681620c7d77e353de0fea217589.svg?invert_in_darkmode&sanitize=true" align=middle width=19.777485749999993pt height=14.15524440000002pt/> using linear elasticity above.
