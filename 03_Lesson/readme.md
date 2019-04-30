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

The material is linear elastic, defined using the keyword <em> *ELASTIC </em>. The elastic modulus is <img src="/03_Lesson/tex/57edfc49eca3237d9614cdfaa86fd48a.svg?invert_in_darkmode&sanitize=true" align=middle width=67.87664564999999pt height=22.465723500000017pt/> and Poisson's ratio is <img src="/03_Lesson/tex/15c1721523b4a6c9de5c6579ea380fdd.svg?invert_in_darkmode&sanitize=true" align=middle width=52.088957249999986pt height=21.18721440000001pt/>. We must specify a name for this material (<em> M2 </em>).

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
	
## Contact pair definition

The contact pair is defined using using the keyword <em> *CONTACT PAIR </em>:
 
	**********************************************************************
	** Define contact pair
	** slave, master
	**********************************************************************
	*CONTACT PAIR, TYPE=SURFACE TO SURFACE, INTERACTION=SurfInterProps, ADJUST=1.e-3
	TopSurfCube,BotSurfTable
 
Here, the <em> TYPE=SURFACE TO SURFACE </em> option is used. For this type of contact, the thickness of shell elements, if used in the contact pair definition, will be relevant. The interaction <em> SurfInterProps </em>, which was defined earlier, is referenced in the contact pair definition. 

The next line specifies the two surfaces in contact. The slave surface is first specified, followed by the master. Some general guidance on the selection of the slave and master surfaces are given in the footnotes:

## Analysis step definition

The unsymmetric solver must be used<sup>[b](#myfootnote1)</sup>. This is specified using the option <em> UNSYMM=YES </em> on the <em> *STEP </em> line:

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

Here, the base of the cube is fixed against all 3 translations. Furthermore, the middle of the table (node <img src="/03_Lesson/tex/058144136c51a2587e0014f0855b972a.svg?invert_in_darkmode&sanitize=true" align=middle width=16.438418699999993pt height=21.18721440000001pt/>) is fixed against translations in <img src="/03_Lesson/tex/cbfb1b2a33b28eab8a3e59464768e810.svg?invert_in_darkmode&sanitize=true" align=middle width=14.908688849999992pt height=22.465723500000017pt/> and <img src="/03_Lesson/tex/91aac9730317276af725abd8cef04ca9.svg?invert_in_darkmode&sanitize=true" align=middle width=13.19638649999999pt height=22.465723500000017pt/>; this is to prevent rigid body motion of the table. The pressure load of <img src="/03_Lesson/tex/e4879cca02caa03e5ba578d1f3f0e24a.svg?invert_in_darkmode&sanitize=true" align=middle width=59.41204994999998pt height=21.18721440000001pt/> is applied on the table top surface.
	
## Exercise 

What happens when you swap the master and contact surfaces? Do you get convergence? If not, why?

Try tieing the surfaces ....


Try changing the contact pair option to <em> TYPE=NODE TO SURFACE </em>. What are the things that you need to change in the input file to make the contact work? Hint: for this contact type, the shell thickness is not used.

---
## Footnotes

<a name="myfootnote1">a</a>) The <em> *SURFACE INTERACTION </em> is a required keyword for contact definition, even if you are considering frictionless contact. In this case, there is <em> *FRICTION </em> line and associated coefficient of friction is not required.

<a name="myfootnote1">b</a>) Why do we need an unsymmetric solver for frictional problems?
 
<a name="myfootnote1">c</a>) General guidelines on the selection of slave and master surfaces (taken from https://www.quora.com/What-are-the-three-main-criteria-to-determine-the-slave-and-master-surfaces-in-ABAQUS):



If you have a combination of Rigid and deformable bodies, the rigid body should be the master and the deformable should be the slave.

If both surfaces in a contact definition are deformable, then the softer of the two is the slave and the more stronger is the master.

The densely meshed body should be the slave. This is because, ABAQUS allows master to penetrate into the slave. To avoid too much penetration, the slave meshing must be denser. If densely meshed, the element size of slave is small which allows the nodes to effectively prevent penetration into their sphere of influence. The coarser mesh is the master.

The longer of the two surfaces should be the master. This will prevent sliding slave nodes from sliding off from the surface and falling behind. If a slave node falls behind a master, excessive convergence issues occur.

The more smoother of the two surfaces should be the master. This is because non smooth surfaces can have gaps or peaks in the mesh or cracks in the mesh. A slave node sliding on such non smooth surface can fall through this crack causing convergence issues.
If an assembly consists or two identical surfaces, one which was created and meshed in ABAQUS and the other one being imported from a third party , then it is better for the one meshed and created in ABAQUS to be the master. This is because imported geometries and meshes are prone to sudden changes in mesh, cracks or gaps in the mesh.
