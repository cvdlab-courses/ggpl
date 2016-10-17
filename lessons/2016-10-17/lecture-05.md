% Geometric \& Graphics Programming Lab: Lecture 5
% Alberto Paoluzzi
% \today


## Outline: larlib

\tableofcontents



## Simplices and simplicial complexes 


*	A. Paoluzzi, F. Bernardini, C. Cattani and V. Ferrucci: [Dimension-Independent Modeling with Simplicial Complexes. \emph{ACM Transactions on Graphics}](http://dl.acm.org/citation.cfm?id=169719). 12(1): 56-102 (1993)



# Simplicial complexes


## Examples
\framesubtitle{Digital Terrain model}

\centering
\includegraphics[width=0.6\linewidth]{images/mesh5}

[\emph{Enhanced 3D Model of Mars Crater Edge Shows Ups and Downs}](http://spacefellowship.com/news/art18621/enhanced-3d-model-of-mars-crater-edge-shows-ups-and-downs.html)

## Examples
\framesubtitle{Typical graphical model}

\centering
\includegraphics[width=0.5\linewidth]{images/mesh1}

[\emph{Stanford bunny, by Marc Levoy}](https://graphics.stanford.edu/data/3Dscanrep/)

## Examples
\framesubtitle{Typical engineering model mesh}

\centering
\includegraphics[width=0.6\linewidth]{images/mesh4}

[\emph{COMSOL Multiphysics Software Product Suite}](https://www.comsol.com/products)



## First definitions 

\includegraphics[width=\linewidth]{images/lez04-2}



## Simplicial complex 

\includegraphics[width=\linewidth]{images/lez04-3}


## Order and skeleton 

\includegraphics[width=\linewidth]{images/lez04-4}


## Polyhedra 

\includegraphics[width=\linewidth]{images/lez04-5}


## Boundary of a polyhedron 

\includegraphics[width=\linewidth]{images/lez04-6}

\includegraphics[width=\linewidth]{images/lez04-7}


## Coherent orientation of faces 

\includegraphics[width=\linewidth]{images/lez04-8}


## Extraction of facets 

\includegraphics[width=\linewidth]{images/lez04-9}


## Simplicial meshes 

\includegraphics[width=\linewidth]{images/lez04-10}


## Extrusion of a triangle 

\includegraphics[width=\linewidth]{images/lez04-11}


## Winged representation 

\includegraphics[width=\linewidth]{images/lez04-12}


## Winged representation of the boundary 

\includegraphics[width=\linewidth]{images/lez04-13}


## Sweeping and extrusion 

\includegraphics[width=\linewidth]{images/lez04-14}


## Sweeping vs extrusion 

\includegraphics[width=\linewidth]{images/lez04-15}


## Extrusion of simplices 

\includegraphics[width=\linewidth]{images/lez04-16}


## Extrusion of a simplex 

\includegraphics[width=\linewidth]{images/lez04-17}



# Introduction to `larlib`


## LAR Basics 


*	A. DiCarlo, V. Shapiro, and A. Paoluzzi, [Linear Algebraic Representation for Topological Structures, \emph{Computer-Aided Design}](http://www.sciencedirect.com/science/article/pii/S001044851300184X), Volume 46, Issue 1 , January 2014, Pages 269-274



## `Larlib` project 

\href{https://github.com/cvdlab/lar-cc/}{\emph{https://github.com/cvdlab/lar-cc/}}

\vfill

\centering
\href{https://github.com/cvdlab/lar-cc/}{\includegraphics[width=\linewidth]{lar-cc.pdf}}


## Import the Stanford "Bunny" in `larlib`  (1/3)


Play with the model:

\scriptsize
\vfill

```{.python}
from larlib import *
batches = []
batches+=Batch.openObj("bunny.obj")
octree = Octree(batches)
glcanvas = GLCanvas()
glcanvas.setOctree(octree)
glcanvas.runLoop()
```
\vfill

The original Stanford Bunny model is in `.ply` format (repo: [_https://graphics.stanford.edu/data/3Dscanrep/_](https://graphics.stanford.edu/data/3Dscanrep/)) and contains almost 70,000 polygons.


## Import the Stanford "Bunny" in `larlib`  (1/3)


\centering
\includegraphics[width=\linewidth]{bunny.pdf}



## Import the Stanford "Bunny" in `larlib`  (2/3)

Look at the [_`bunny.obj`_](http://graphics.stanford.edu/~mdfisher/Data/Meshes/bunny.obj) data:

\scriptsize
\vfill

```{.python}
# OBJ file format with ext .obj
# vertex count = 2503
# face count = 4968
v -3.4101800e-003 1.3031957e-001 2.1754370e-002
v -8.1719160e-002 1.5250145e-001 2.9656090e-002
v -3.0543480e-002 1.2477885e-001 1.0983400e-003
   ...
v -6.9413000e-002 1.5121847e-001 -4.4538540e-002
v -5.5039800e-002 5.7309700e-002 1.6990900e-002
f 1069 1647 1578
f 1058 909 939
  ...
f 1487 1318 2503
f 1318 1320 2503
f 1320 2443 2503
```



## Assignment

\framesubtitle{Import the Stanford "Bunny" in `larlib`}


**Convert `bunny.obj` to _`larlib`_ data**

\vfill

To test the conversion, import other _`PLY`_ models from Stanford repository,
and convert to _`OBJ`_, using  [_http://meshlab.sourceforge.net/_](http://meshlab.sourceforge.net/).


## References

[Python Scientific Lecture Notes](http://scipy-lectures.github.io/index.html)

