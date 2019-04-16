# Lesson 1: Overview of a Model

We will build a single-element model subjected to 1D compression loading. The input file can be found in the "abaqus_input_files" folder above.

## Node definition

The size of the element is 1 x 1 x 1 (a unit cube). The nodes are located at the corners of the cube and can be defined using the keyword <em> *NODE </em>:

	*NODE, NSET=GLOBAL_NSET
	1,          0.,          0.,          0.
	2,          1.,          0.,          0.
	3,          1.,          1.,          0.
	4,          0.,          1.,          0.
	5,          0.,          0.,          1.
	6,          1.,          0.,          1.
	7,          1.,          1.,          1.
	8,          0.,          1.,          1.

The first integer of each line refers to the node label ID. The subsequent real numbers define the <img src="/01_Lesson/tex/cbfb1b2a33b28eab8a3e59464768e810.svg?invert_in_darkmode&sanitize=true" align=middle width=14.908688849999992pt height=22.465723500000017pt/>, <img src="/01_Lesson/tex/91aac9730317276af725abd8cef04ca9.svg?invert_in_darkmode&sanitize=true" align=middle width=13.19638649999999pt height=22.465723500000017pt/>, <img src="/01_Lesson/tex/5b51bd2e6f329245d425b8002d7cf942.svg?invert_in_darkmode&sanitize=true" align=middle width=12.397274999999992pt height=22.465723500000017pt/> coordinates. As we define the nodes, these are grouped into a node set <em> NSET </em> called <em> GLOBAL_NSET </em>.

## Element type

We will be using a single hex finite element. The element is defined using the nodes through the keyword <em> *ELEMENT </em>:

	*ELEMENT, TYPE=C3D8, ELSET=P1
	1,      1,      2,      3,      4,      5,      6,      7,      8

The element <em> TYPE </em> refers to the element formulation, which in this case is <em> C3D8 </em><sup>[a](#myfootnote1)</sup>.  

The first integer refers to the element label ID (in this case, specified as 1). Subsequent integers specify the ordering of the nodes of the hex element. As we define the element, it is grouped into an element set <em> ELSET </em> called <em> P1 </em>. 

## Element property

Each element must have an element (section) property<sup>[b](#myfootnote1)</sup> assigned to it. The element property determines whether you are describing a continuum, or some other structural-type stress-state (e.g., shell, beam, etc.). For the C3D8 hex element, we would need a continuum description, which is specified using keyword <em> *SOLID SECTION </em>

	*SOLID SECTION, ELSET=P1, MATERIAL=M1

We must specify the group of elements <em> ELSET </em> associated with this property, and also the material name <em> MATERIAL </em> (see below).

## Material definition

The material is defined using the keyword <em> *MATERIAL </em>:

	*MATERIAL, NAME=M1
	*ELASTIC
	1000.,0.3

The material is linear elastic, defined using the keyword <em> *ELASTIC </em>. The elastic modulus is <img src="/01_Lesson/tex/57edfc49eca3237d9614cdfaa86fd48a.svg?invert_in_darkmode&sanitize=true" align=middle width=67.87664564999999pt height=22.465723500000017pt/> and Poisson's ratio is <img src="/01_Lesson/tex/15c1721523b4a6c9de5c6579ea380fdd.svg?invert_in_darkmode&sanitize=true" align=middle width=52.088957249999986pt height=21.18721440000001pt/>. We must specify a name for this material (<em> M1 </em>).

## Surface definition
For the purpose of defining a pressure loading on a face of the hex element, we need to first define a surface

	*SURFACE,NAME=TopSurf,TYPE=ELEMENT
	1,S2

Refer to the Abaqus Elements Guide<sup>[c](#myfootnote1)</sup> to identify the surface ID for the hex element.

## Analysis step definition

We define the analysis step as follows:

	*STEP, NLGEOM=NO, INC=99999999
	Uniaxial compression
	*STATIC
	0.5,1.0,1.e-12,1.0
		...
	*END
	
The option <em> NLGEOM=NO </em> ensures that we are using small-strain formulation, and the number of increments for the entire step <em> INC </em> is set to a very large value (in general, this is to prevent premature termination).

A title of the analysis step is given: <em> Uniaxial compression </em>

We specify a static analysis using the keyword <em> *STATIC </em>. The following line defines the time-stepping characteristics of the analysis step:

	initial time step, total duration of the step, minimum allowable time step, maximum allowable time step

In addition, within the analysis step, we specify:
	
### Boundary conditions

The boundary conditions are such that we have symmetry boundary conditions on the planes <img src="/01_Lesson/tex/b6903d0bfe9fdb18f618c3811752bda9.svg?invert_in_darkmode&sanitize=true" align=middle width=45.04550654999999pt height=22.465723500000017pt/>, <img src="/01_Lesson/tex/5e00215a538a57a8b3eae1a769cd34d6.svg?invert_in_darkmode&sanitize=true" align=middle width=43.33321904999999pt height=22.465723500000017pt/> and <img src="/01_Lesson/tex/e51463e7c08e166a5ffb970655d2d909.svg?invert_in_darkmode&sanitize=true" align=middle width=42.53410919999999pt height=22.465723500000017pt/>.

	*BOUNDARY
	1,    1
	1,    2
	1,    3
	2,    2
	2,    3
	3,    3
	4,    1
	4,    3
	5,    1
	5,    2
	6,    2
	8,    1	

### Loads

We specify the pressure load of <img src="/01_Lesson/tex/619592087e8219141eb96df340222866.svg?invert_in_darkmode&sanitize=true" align=middle width=29.22385289999999pt height=21.18721440000001pt/> on the surface <em> TopSurf </em> defined earlier. Positive pressure is in the direction opposite to the surface normal.

	*DSLOAD
	TopSurf,P,0.13

### Output request

We specify the output we require from the analysis:

	*OUTPUT, FIELD
	*NODE OUTPUT
	U,RF
	*ELEMENT OUTPUT
	E,S

In the above, we requested nodal field quantities (displacements <em> U </em>, reactions <em> RF </em>) and elemental field quantities (strains <em> E </em>, stresses <em> S </em>).

## Viewing results

After running the analysis as described in [Lesson 0](./../00_Lesson), we are ready to view the results using Abaqus Viewer. In this lesson, we will verify:

* **Stresses**. The first obvious check that we can make is to confirm that we applied the correct stress value <img src="/01_Lesson/tex/619592087e8219141eb96df340222866.svg?invert_in_darkmode&sanitize=true" align=middle width=29.22385289999999pt height=21.18721440000001pt/>. This can be confirmed by visualizing the stress in the (vertical) <img src="/01_Lesson/tex/5b51bd2e6f329245d425b8002d7cf942.svg?invert_in_darkmode&sanitize=true" align=middle width=12.397274999999992pt height=22.465723500000017pt/> direction <img src="/01_Lesson/tex/8f372bf5cff388edf2a30074c7f27736.svg?invert_in_darkmode&sanitize=true" align=middle width=23.18501789999999pt height=22.465723500000017pt/>, which should be -0.13 (compressive).

	![](./abaqus_input_files/1ElementTest_Lesson1_Step1_S33.png)
	
	Other stress quantities can also be checked. For e.g., the von Mises shear stress <img src="/01_Lesson/tex/d5c18a8ca1894fd3a7d25f242cbe8890.svg?invert_in_darkmode&sanitize=true" align=middle width=7.928106449999989pt height=14.15524440000002pt/> should be <img src="/01_Lesson/tex/619592087e8219141eb96df340222866.svg?invert_in_darkmode&sanitize=true" align=middle width=29.22385289999999pt height=21.18721440000001pt/> since <img src="/01_Lesson/tex/a03c0cdcd2a4f14d3fa3e52fa13ad35a.svg?invert_in_darkmode&sanitize=true" align=middle width=92.60449109999998pt height=24.65753399999998pt/> where <img src="/01_Lesson/tex/e03c67b59d1405f92aed6a4c7eb4deca.svg?invert_in_darkmode&sanitize=true" align=middle width=46.90440644999998pt height=21.18721440000001pt/> is the maximum principal stress and <img src="/01_Lesson/tex/87913464a94d6d2e461966c0b3c99095.svg?invert_in_darkmode&sanitize=true" align=middle width=61.87021499999999pt height=22.465723500000017pt/> is the minimum principal stress; the lateral stress <img src="/01_Lesson/tex/0d1356111d3a14163216612043294f2e.svg?invert_in_darkmode&sanitize=true" align=middle width=54.63085154999999pt height=14.15524440000002pt/> is zero.
	
	![](./abaqus_input_files/1ElementTest_Lesson1_Step1_VMS.png	)

* **Reactions**. The reactions at the four base nodes are equal to <img src="/01_Lesson/tex/6a295b2e0ddef468a1bf686a71ef7080.svg?invert_in_darkmode&sanitize=true" align=middle width=113.242173pt height=24.65753399999998pt/>.
	
	![](./abaqus_input_files/1ElementTest_Lesson1_Step1_RF3.png	)
	
* **Displacements**. Since we have a simple linear elastic material and the stress state is homogeneous throughout the element, we can also check the displacements. Since the cube has unit dimensions, the displacement would be equal to the strain. From [linear elasticty](https://en.wikipedia.org/wiki/Linear_elasticity), the vertical strain/displacement is:
		
	<p align="center"><img src="/01_Lesson/tex/bfd725bb8e9573ebfe78ef13dc374abc.svg?invert_in_darkmode&sanitize=true" align=middle width=314.53656794999995pt height=32.990165999999995pt/></p>
	
	A trite calculation would show that <img src="/01_Lesson/tex/fcf8c1f48d1ea620135c53b35a252ef2.svg?invert_in_darkmode&sanitize=true" align=middle width=129.66327825pt height=26.76175259999998pt/>, which agrees with the contour plot below.
	
	![](./abaqus_input_files/1ElementTest_Lesson1_Step1_U3.png	)
	


## Exercise 

* Define the same 1D compression loading by prescribing displacements on the nodes of the top face. Hint: modify the boundary condition.

* Define the same 1D compression loading using point loads. Hint: use the keyword <em> *CLOAD </em>.

---
## Footnotes
<a name="myfootnote1">a</a>) It is a common misunderstanding that the C3D8 is a fully-integrated element. It uses a selectively-reduced integration scheme to prevent locking. 

<a name="myfootnote1">b</a>) There is a distiction between <em> element type </em> (specified by <em> TYPE </em>) and <em> element property </em> (e.g., specified by <em> *SOLID SECTION </em>). 

<a name="myfootnote1">c</a>) Reference Library > Abaqus > Elements > Continuum Elements > General-purpose continuum elements > Three-dimensional solid element library   