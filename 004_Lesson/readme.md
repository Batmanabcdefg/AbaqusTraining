# Lesson 4: Heat Transfer

**In progress and incomplete**

## Background

A steady-state heat transfer analysis of a unit block is performed. The top edge (B) of the block is prescribed with a distributed flux, while the bottom edge (A) has a prescribed temperature. All other edges are insulated. The thermal conductivity of the block material is 1.0. 

The flux associated with conduction across a surface is given by<sup>[a](#myfootnote1)</sup>: 

<img src="/004_Lesson/tex/ae408535435f2a09ffe3f2fa5136a230.svg?invert_in_darkmode&sanitize=true" align=middle width=114.88108664999999pt height=45.072403200000004pt/>

where <img src="/004_Lesson/tex/2f128f854fd9ff3109e6b9c75fa629a0.svg?invert_in_darkmode&sanitize=true" align=middle width=13.54268354999999pt height=14.15524440000002pt/> is the surface flux, <img src="/004_Lesson/tex/c2e026b8a86e00d5c521886fb6a64d89.svg?invert_in_darkmode&sanitize=true" align=middle width=10.502226899999991pt height=14.611878600000017pt/> is the surface normal, <img src="/004_Lesson/tex/4d05b05c2efa8462d93f554065731f8f.svg?invert_in_darkmode&sanitize=true" align=middle width=9.97711604999999pt height=22.831056599999986pt/> is the conductivity tensor, and <img src="/004_Lesson/tex/27e556cf3caa0673ac49a8f0de3c73ca.svg?invert_in_darkmode&sanitize=true" align=middle width=8.17352744999999pt height=22.831056599999986pt/> is the temperature. For our 1-dimensional problem, the above can be reduced to a scale equation:

<img src="/004_Lesson/tex/97f0a98c672fd59814696638bd7a99ef.svg?invert_in_darkmode&sanitize=true" align=middle width=175.60577264999998pt height=45.072403200000004pt/>

since <img src="/004_Lesson/tex/417e9d7f078cdb8c16592aee5f8c7687.svg?invert_in_darkmode&sanitize=true" align=middle width=39.21220214999999pt height=22.831056599999986pt/> and <img src="/004_Lesson/tex/e937ba1d3e4f9e2abb84171f9ab72a0d.svg?invert_in_darkmode&sanitize=true" align=middle width=53.23049984999998pt height=22.465723500000017pt/>. This gives:

<img src="/004_Lesson/tex/24f88f149536bd362616cb16039705a9.svg?invert_in_darkmode&sanitize=true" align=middle width=93.00760919999999pt height=22.831056599999986pt/>. 

which can be used to check the accuracy of the thermal conduction procedure.

## Node definition


## Element definition

The block is composed of three 8-node brick elements (DC3D8). 



## Element property

	*SOLID SECTION,ELSET=ELALL,MATERIAL=EQUIL	

## Material definition

The sole material property associated with these elements is the thermal conductivity.

	*MATERIAL,NAME=EQUIL
	*CONDUCTIVITY
	1., 

To make things more interested, we also test the use of a non-conforming mesh where the block is split into top and bottom halves, which are meshed separately and tied together<sup>[b](#myfootnote1)</sup>. 

## Surface interaction

For the interaction properties of the tied surface is specified using *SURFACE INTERACTION:

	*Surface Interaction, name=Thermal_Contact	
	*Gap Conductance
	 1e+06,   0.
		0., 0.05

The conductance properties of the surface is prescribed using the keyword *GAP CONDUCTANCE. Here, a large thermal conductivity (<img src="/004_Lesson/tex/876fd957d8cc6f84f8dc48ba76a1a494.svg?invert_in_darkmode&sanitize=true" align=middle width=24.09255749999999pt height=21.18721440000001pt/>) of the tied surface is specified.

		
## Thermal surfaces

	*Surface, type=ELEMENT, name=TOP_BLOCK_TopSurf
	TOP_BLOCK, S5
	*Surface, type=ELEMENT, name=TOP_BLOCK_BotSurf
	TOP_BLOCK, S3
	*Surface, type=ELEMENT, name=BOT_BLOCK_TopSurf
	BOT_BLOCK, S5

## Thermal contact
		
The top and bottom blocks are tied together using *CONTACT PAIR:
	
	*Contact Pair, interaction=Thermal_Contact, type=SURFACE TO SURFACE
	BOT_BLOCK_TopSurf, TOP_BLOCK_BotSurf
		
The slave surface is associated with the bottom half and the master surface is associated with the top half of the block.

The block has 1 element at the top half and 2 elements at the bottom half. The base of the block (side A) is prescribed a temperature, which is ramped from 0 to 300 within duration of 1.0. The opposite side (top; side B) of the block has a uniform distributed flux <img src="/004_Lesson/tex/2f128f854fd9ff3109e6b9c75fa629a0.svg?invert_in_darkmode&sanitize=true" align=middle width=13.54268354999999pt height=14.15524440000002pt/>, which is prescribed using the keyword *DSFLUX and ramped from 0 to 10 using the keyword *AMPLITUDE.

## Analysis step

## Viewing results	

TODO

## Exercise 

None

---
## Footnotes

<a name="myfootnote1">a</a>) Abaqus Theory Manual > Procedures > Heat Transfer > Convection/Diffusion

<a name="myfootnote2">b</a>) Ties are typically used to as a convenient means to transition between fine and coarse meshes. 

---
## Additional Comments on This Lesson (Links to Milo)
None
