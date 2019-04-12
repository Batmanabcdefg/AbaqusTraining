# Lesson 1: Overview of a Model

We will build a model of a single element subjected to a 1D compression loading.

## Node definition

The size of the element is 1 x 1 x 1, i.e., a unit cube. The nodes are located at the corners of the cube and can be defined using the keyword <em> *NODE </em>:

	*NODE, NSET=GLOBAL_NSET
	1,          0.,          0.,          0.
	2,          1.,          0.,          0.
	3,          1.,          1.,          0.
	4,          0.,          1.,          0.
	5,          0.,          0.,          1.
	6,          1.,          0.,          1.
	7,          1.,          1.,          1.
	8,          0.,          1.,          1.

The first integer of each line refers to the node label ID. The subsequent real numbers define the X, Y, Z coordinates. As we define the nodes, these are grouped into a node set <em> NSET </em> called <em> GLOBAL_NSET </em>.

## Element type

We will be using a single hex finite element. The element is defined using the nodes through the keyword <em> *ELEMENT </em>:

	*ELEMENT, TYPE=C3D8, ELSET=P1
	1,      1,      2,      3,      4,      5,      6,      7,      8

The element <em> TYPE </em> refers to the element formulation, which in this case is <em> C3D8 </em><sup>[1](#myfootnote1)</sup>.  

The first integer refers to the element label ID (in this case, specified as 1). Subsequent integers specify the ordering of the nodes of the hex element. As we define the element, it is grouped into an element set <em> ELSET </em> called <em> P1 </em>. 

## Element property

An element property needs to be assigned. There is a distiction between <em> element type </em> and <em> element property </em> (specified by <em> TYPE </em> above). The element property determines whether you are describing a continuum, or some other structural-type stress-state (e.g., shell, beam, etc.). For the C3D8 hex element, we would need a continuum description, which is specified using keyword <em> *SOLID SECTION </em>

	*SOLID SECTION, ELSET=P1, MATERIAL=M1

We have to specify the group of elements <em> ELSET </em> associated with this property, and also the material name <em> MATERIAL </em> (see below).

## Material definition

For this example, we will use a linear elastic material with elastic modulus of 1000 and Poisson's ratio of 0.3. The material is defined using the keyword <em> *MATERIAL </em>:

	**MATERIAL, NAME=M1
	*ELASTIC
	1000.,0.3

We have to specify a name for this material, which we have called <em> M1 </em>

## Boundary conditions

The boundary conditions are such that the plane X = 0, Y = 0, Z = 0

---
<a name="myfootnote1">1</a>: The C3D8 describes a selectively-reduced integration solid element
