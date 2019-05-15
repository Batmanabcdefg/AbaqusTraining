# Lesson 4: Heat Transfer

**In progress and incomplete**

## Background

A steady-state heat transfer analysis of a unit block is performed. The top edge (B) of the block is prescribed with a distributed flux, while the bottom edge (A) has a prescribed temperature. All other edges are insulated. The thermal conductivity of the block material is 1.0. 

The flux associated with conduction across a surface is given by<sup>[a](#myfootnote1)</sup>: 

$q_s = -\bold{n} \dot \bold{k} \dot \dfrac{\partial \theta}{\partial \bold{x}}$

which in this case can be reduced to the 1-dimensional problem:

$q_s = -k \dfrac{\Delta\theta}{\Delta x} - \left(\theta_A - \theta_B\right)$

since $k = 1$ and $\Delta x = 1$. This gives:

$\theta_B = \theta_A + q_s$. 

which can be used to check the accuracy of the thermal conduction procedure.

## Modeling

The block is composed of three 8-node brick elements (DC3D8). To make things more interested, we also test the use of a non-conforming mesh where the block is split into top and bottom halves, which are meshed separately and tied together<sup>[b](#myfootnote1)</sup>. The tie is achieved using the keyword *CONTACT PAIR, and a large thermal conductivity ($1e6$) of the tied surface is prescribed under the keyword *GAP CONDUCTANCE. In the *CONTACT PAIR, the slave surface is associated with the bottom half and the master surface is associated with the top half of the block.

The block has 1 element at the top half and 2 elements at the bottom half. The base of the block (side A) is prescribed a temperature, which is ramped from 0 to 300 within duration of 1.0. The opposite side (top; side B) of the block has a uniform distributed flux $q_s$, which is prescribed using the keyword *DSFLUX and ramped from 0 to 10 using the keyword *AMPLITUDE.

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
