# Lesson 4: Heat Transfer

In progress and incomplete

This is a transient heat transfer analysis 


a block of material, with top edge prescribed with a distributed flux, prescribed temperature on bottom edge, and all other edges insulated 

A steady-state heat transfer analysis of a unit block is performed. The block is composed of three 8-node brick elements (DC3D8). The block is split into top and bottom halves, which are meshed separately and tied together. Ties are typicalled used to transition ...

The block has 1 element at the top half and 2 elements at the bottom half. The base of the block (side A) is prescribed a temperature, which is ramped from 0 to 300 within duration of 1.0. The opposite side (top; side B) of the block has a uniform distributed flux $q$, which is prescribed using the keyword *DSFLUX 


and ramped from 0 to 10 using the keyword *AMPLITUDE. 


The thermal conductivity of the block material is 1.0. A thermal energy balance gives (derive this, provide link):

$-k \dfrac{\Delta\theta}{\Delta x} = - \left(\theta_A - \theta_B\right) = -q$

which gives $\theta_B = \theta_A + q$. 

The tie is achieved using the keyword *CONTACT PAIR, and a large thermal conductivity ($1e6$) of the tied surface is prescribed under the keyword *GAP CONDUCTANCE. In the *CONTACT PAIR, the slave surface is associated with the bottom half and the master surface is associated with the top half of the block.


## Viewing results	
	
## Exercise 


---
## Footnotes

---
## Additional Comments on This Lesson (Links to Milo)
None
