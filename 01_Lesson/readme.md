# Lesson 1: Overview of a Model

We will build a model a single element subjected to a 1D compression loading.

The boundary conditions are such that the 


## Node definition

The size of the element is 1 x 1 x 1, i.e., a unit cube. The nodes are located at the corners of the cube and can be defined using the keyword *NODE as follows:

	*NODE, NSET=GLOBAL_NSET
	1,          0.,          0.,          0.
	2,          1.,          0.,          0.
	3,          1.,          1.,          0.
	4,          0.,          1.,          0.
	5,          0.,          0.,          1.
	6,          1.,          0.,          1.
	7,          1.,          1.,          1.
	8,          0.,          1.,          1.

As we define the nodes, these are also grouped into a node set <em> NSET </em> called <em> GLOBAL_NSET </em>.

## Element connectivity

We will be using a single hex finite element. The element is defined using the nodes through the keyword *ELEMENT as follows:

	*ELEMENT, TYPE=C3D8, ELSET=P1
	1,      1,      2,      3,      4,      5,      6,      7,      8

The element TYPE is C3D8. 

The first integer refers to the element label ID (in this case, specified as 1). 

Subsequent integers specified the ordering of the nodes of the hex element. 


