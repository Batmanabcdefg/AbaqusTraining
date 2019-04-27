# Lesson 3: Contact Interactions

Start from input file for Lesson 1

We will add a "table" of thickness 0.1 units on top of the cube (the cube will serve as "a table stand"). 

Define additional nodes for the mid-surface of table.

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
		  
Define the 4 elements representing the table:

	*ELEMENT, TYPE=S4, ELSET=P2
		  2,      9,     10,     13,     12
		  3,     10,     11,     14,     13
		  4,     12,     13,     16,     15
		  5,     13,     14,     17,     16		  
		  
These are shell elements of type S4, and these elements are grouped into the element set P2. The shell section properties are defined by specifying the thickness:

	*SHELL SECTION, ELSET=P2, MATERIAL=M2
	0.1
	
The material for the table is M2, specified as follows:

	*MATERIAL, NAME=M2
	*ELASTIC
	1000.,0.3
	
Next, we will define the bottom and top surfaces of the table:

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

We define the contact interaction friction of 0.3 using the keyword *SURFACE INTERACTION and option *FRICTION.

	**********************************************************************
	** Define contact interaction properties
	**********************************************************************
	*SURFACE INTERACTION, NAME=SurfInterProps
	*FRICTION
	0.3
	
This interaction is named SurfInterProps, which will be used in the contact pair definition:
 
	**********************************************************************
	** Define contact pair
	** slave, master
	**********************************************************************
	*CONTACT PAIR, TYPE=SURFACE TO SURFACE, INTERACTION=SurfInterProps, ADJUST=1.e-3
	TopSurfCube,BotSurfTable
 
The slave surface is specified, followed by the master. Note: TopSurfCube was defined and used in Lesson 1.

The unsymmetric solver must be used<sup>[a](#myfootnote1)</sup>:

	**********************************************************************
	** Load Step 1
	** Note: must use unsymmetric solver because of friction
	**********************************************************************
	*STEP, NLGEOM=NO, INC=99999999, UNSYMM=YES

	
Changes in the boundary conditions and loads

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
	
## Exercise 

What happens when you swap the master and contact surfaces? Do you get convergence? If not, why?

---
## Footnotes
<a name="myfootnote1">a</a>) Why we need an unsymmetric solver for frictional problems?
 


