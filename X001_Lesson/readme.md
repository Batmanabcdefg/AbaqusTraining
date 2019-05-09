# Lesson 4: Heat Transfer

**In progress and incomplete**

This is a transient heat transfer analysis 


a block of material, with top edge prescribed with a distributed flux, prescribed temperature on bottom edge, and all other edges insulated 

A steady-state heat transfer analysis of a unit block is performed. The block is composed of three 8-node brick elements (DC3D8). The block is split into top and bottom halves, which are meshed separately and tied together. Ties are typicalled used to transition ...

The block has 1 element at the top half and 2 elements at the bottom half. The base of the block (side A) is prescribed a temperature, which is ramped from 0 to 300 within duration of 1.0. The opposite side (top; side B) of the block has a uniform distributed flux <img src="/04_Lesson/tex/d5c18a8ca1894fd3a7d25f242cbe8890.svg?invert_in_darkmode&sanitize=true" align=middle width=7.928106449999989pt height=14.15524440000002pt/>, which is prescribed using the keyword *DSFLUX 


and ramped from 0 to 10 using the keyword *AMPLITUDE. 


The thermal conductivity of the block material is 1.0. A thermal energy balance gives (derive this, provide link):

<img src="/04_Lesson/tex/0f68de1a0af52c3967a54b6662de23dd.svg?invert_in_darkmode&sanitize=true" align=middle width=199.30623899999998pt height=45.072403200000004pt/>

which gives <img src="/04_Lesson/tex/c4640865a1c45f7c31e717d540c63b88.svg?invert_in_darkmode&sanitize=true" align=middle width=87.39303209999999pt height=22.831056599999986pt/>. 

The tie is achieved using the keyword *CONTACT PAIR, and a large thermal conductivity (<img src="/04_Lesson/tex/876fd957d8cc6f84f8dc48ba76a1a494.svg?invert_in_darkmode&sanitize=true" align=middle width=24.09255749999999pt height=21.18721440000001pt/>) of the tied surface is prescribed under the keyword *GAP CONDUCTANCE. In the *CONTACT PAIR, the slave surface is associated with the bottom half and the master surface is associated with the top half of the block.


## Viewing results	
	
## Exercise 


---
## Footnotes

---
## Additional Comments on This Lesson (Links to Milo)
None
