# Lesson 1: Overview of a Model

We will build a model a single element subjected to a 1D compression loading.

The boundary conditions are such that the 


## Node definition

The size of the element is 1 x 1 x 1, i.e., a unit cube. The nodes are located at the corners of the cube and can be defined using the keyword <em> *NODE </em> as follows:

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

## Element connectivity

We will be using a single hex finite element. The element is defined using the nodes through the keyword <em> *ELEMENT </em> as follows:

	*ELEMENT, TYPE=C3D8, ELSET=P1
	1,      1,      2,      3,      4,      5,      6,      7,      8

The element <em> TYPE </em> is <em> C3D8 </em>. The first integer refers to the element label ID (in this case, specified as 1). Subsequent integers specify the ordering of the nodes of the hex element. As we define the element, it is grouped into an element set <em> ELSET </em> called <em> P1 </em>. 


