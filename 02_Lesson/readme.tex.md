# Lesson 2: 

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

* **Displacements**. As in Lesson 1, the vertical strain after Step 1 (gravity) is $\epsilon_{33} = -1.3\times10^{-4}$.

	In Step 2, the modulus $E$ is dropped from $1000$ to $1$ through field variable $\#1$. Therefore, at the end of Step 2, the vertical strain should be $1000$ times larger, at $\epsilon_{33} = -1.3\times10^{-1}$. 	
	Also, the lateral strain $\epsilon_{11} = \epsilon_{22}$ is:
	$$
	\begin{align}
	\epsilon_{22} &=& \dfrac{1}{E}\left[ \left(1+\nu\right) \sigma_{22} - \nu\left(\sigma_{11}+\sigma_{22}+\sigma_{33}\right) \right] = 0.039\\
	\end{align}
	$$
	
	where $E = 1$ and $\nu = 0.3$.	These values jibe with the contour plots below.
	
	![](./abaqus_input_files/1ElementTest_Lesson2Step_2_Frame3_E22.png	)
	
	In Step 3, the modulus $E=1$ is kept constant, while the Poisson's ratio $\nu$ is dropped from $0.3$ to $0.2$ through field variable $\#2$. Therefore, at the end of Step 3, the lateral strain is:
	
	$$
	\begin{align}
	\epsilon_{22} &=& \dfrac{1}{E}\left[ \left(1+\nu\right) \sigma_{22} - \nu\left(\sigma_{11}+\sigma_{22}+\sigma_{33}\right) \right] = 0.026\\
	\end{align}
	$$
			
	where $E = 1$ and $\nu = 0.2$.	These values jibe with the contour plots below.

	![](./abaqus_input_files/1ElementTest_Lesson2Step_3_Frame3_E22.png	)

## Exercise 

* The vertical strain $\epsilon_{33}$ did not change during Step 3. Why? Hint: Calculate $\epsilon_{33}$ using linear elasticity above.
