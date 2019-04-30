# Lesson 3: Contact Interactions

We build on the cube model described in [Lesson 1](./../01_Lesson). In this lesson, we will add a "table" of thickness 0.1 units on top of the cube (the cube will serve as "a table stand"). 

The following blocks in the inpur file need to be modified. The input file can be found in the "abaqus_input_files" folder above.

## Node definition

Under the <em> *NODE </em> block, we define these additional nodes for the mid-surface of table:

	****
	**** Nodes for mid-surface of "table"
	****
		   9,         -0.5,         -0.5,          1.05
		  10,          0.5,         -0.5,          1.05
		  11,          1.5,         -0.5,          1.05
		  12,         -0.5,          0.5,          1.05
		  13,          0.5,          0.5,          1.05
		  14,          1.5,          0.5,          1.05
		  15,         -0.5,          1.5,          1.05
		  16,          0.5,          1.5,          1.05
		  17,          1.5,          1.5,          1.05

## Element definition
		  
Next, we define the 4 elements using the keyword <em> *ELEMENT </em> to represent the table:

	*ELEMENT, TYPE=S4, ELSET=P2
		  2,      9,     10,     13,     12
		  3,     10,     11,     14,     13
		  4,     12,     13,     16,     15
		  5,     13,     14,     17,     16		  
		  
Here, we defined 4 shell elements of type <em> S4 </em>. In each line, the first integer refers to the element label ID (in this case, specified as 1). Subsequent integers specify the ordering of the nodes of the 4-noded shell element. As we define each element, it is grouped into an element set <em> ELSET </em> called <em> P2 </em>.

## Element property

The required element property is the one that describes a shell-type stress-state. For the <em> S4 </em> hex element, this is specified using keyword <em> *SHELL SECTION </em>. The next required line is the specified shell thickness:

	*SHELL SECTION, ELSET=P2, MATERIAL=M2
	0.1	

## Material definition

The material for the shell elements is defined using the keyword <em> *MATERIAL </em>:

	*MATERIAL, NAME=M2
	*ELASTIC
	1000.,0.3

The material is linear elastic, defined using the keyword <em> *ELASTIC </em>. The elastic modulus is $E = 1000$ and Poisson's ratio is $\nu = 0.3$. We must specify a name for this material (<em> M2 </em>).

## Surface definition

Surfaces are used in contact interactions. Here, we will define the bottom and top surfaces of the table:

	**********************************************************************
	** Define bottom surface of table
	**********************************************************************
	*SURFACE,NAME=BotSurfTable,TYPE=ELEMENT
	P2,SNEG
	**********************************************************************
	** Define top surface of table
	**********************************************************************
	*SURFACE,NAME=TopSurfTable,TYPE=ELEMENT
	P2,SPOS	
	
The top surface will be used for load application, and the bottom surface will be contacting the table top (the top surface of the cube).	

## Contact surface interaction properties

Contact interaction properties for surfaces are needed to define the frictional properties<sup>[a](#myfootnote1)</sup>. We define the contact interaction friction of 0.3 using the keyword <em> *SURFACE INTERACTION </em> and option <em> *FRICTION </em>:

	**********************************************************************
	** Define contact interaction properties
	**********************************************************************
	*SURFACE INTERACTION, NAME=SurfInterProps
	*FRICTION
	0.3
	
This interaction is named <em> SurfInterProps </em> , which will be used in the contact pair definition:
 
	**********************************************************************
	** Define contact pair
	** slave, master
	**********************************************************************
	*CONTACT PAIR, TYPE=SURFACE TO SURFACE, INTERACTION=SurfInterProps, ADJUST=1.e-3
	TopSurfCube,BotSurfTable
 
The slave surface is specified, followed by the master. Note: TopSurfCube was defined and used in Lesson 1.

## Analysis step definition

The unsymmetric solver must be used<sup>[b](#myfootnote1)</sup>:

	**********************************************************************
	** Load Step 1
	** Note: must use unsymmetric solver because of friction
	**********************************************************************
	*STEP, NLGEOM=NO, INC=99999999, UNSYMM=YES
	
We implement the following boundary conditions and loads:

	*************************
	** Boundary conditions
	*************************
	*BOUNDARY
		1,    1,3
		2,    1,3
		3,    1,3
		4,    1,3
	***
	13,1,2
	*********************************************
	** Apply pressure on top surface of table
	*********************************************
	*DSLOAD
	TopSurfTable,P,0.13	

Here, the base of the cube is fixed against all 3 translations, and the pressure load is applied on the table top surface.
	
## Exercise 

What happens when you swap the master and contact surfaces? Do you get convergence? If not, why?

---
## Footnotes

<a name="myfootnote1">a</a>) The <em> *SURFACE INTERACTION </em> is a required keyword for contact definition, even if you are considering frictionless contact. In this case, there is <em> *FRICTION </em> line and associated coefficient of friction is not required.

<a name="myfootnote1">b</a>) Why we need an unsymmetric solver for frictional problems?
 


