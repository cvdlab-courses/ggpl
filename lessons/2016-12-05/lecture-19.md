% Geometric \& Graphics Programming Lab: Lecture 19
% Alberto Paoluzzi
% \today

## Outline: Hierarchical structures

\tableofcontents

# Introduction

## Curves

Curves as \emph{point loci} with a specific shape are often identified
by a proper name, such as \emph{circle}, \emph{parabola},
\emph{hyperbola}, \emph{spiral}, \emph{helix}, etc.  

\vfill
For applications
of computer-aided design, some classes of \emph{free-form curves}
are more interesting, because they are able to satisfy both geometric
and  esthetic constraints set by designers, depending on the shape
design problem at hand.  

\vfill

Even more useful, \emph{splines} are
piecewise-continuous composite curves used to either interpolate or
approximate a discrete set of points. 



## Curve representations

Curves may be represented by using different kinds of equations. 
In particular, it is possible to distinguish representations:
\begin{enumerate}
\item
\emph{explicit} or Cartesian, where the curve is given as the graph of
a function;
\item
\emph{implicit}, as the zero set of one or more global
algebraic equations;
\item
\emph{parametric}, associated with a vector function of one parameter;
\item
\emph{intrinsic}, where points locally satisfy differential equations.
\end{enumerate}


## Explicit representation

An explicit or _Cartesian representation_ of a plane curve is the graph
$(x, f(x))$ of a function $f:\R\rightarrow\R$.  We may also write, in 
this case:
$$
y = f(x).
$$

*	This representation is _not diffuse nor useful_ in
**geometric modeling**, because it is unusable for closed curves

*	more in general, is unusable for curves where more than one value of the dependent
variable $y$ is associated with the same value of the independent
variable x$ 

*	it does not easily support affine
transformations.


## Explicit representation example

A simple example of _explicit representation_ in the 2D
plane is the well-known Cartesian equation of the line:
$$
y = mx + c,
$$
where $m$ is called the \emph{angular coefficient} and coincides with the
tangent of the angle that the line creates with the $x$ axis, and $c$
is the ordinate of the intersection point between the line and the $y$
axis.  

*	this representation cannot
be used for _vertical lines_, for which we must conversely use the
equation $x = a$.


## Implicit representation

The _implicit representation_ denotes a plane curve as 
the **locus of points** that _satisfy an equation_, usually algebraic, of 
type:
$$
f(x,y) = 0.
$$
The simplest example of a plane curve is given by the implicit
representation of the 2D line:
$$
ax + by + c = 0.
$$

## Parametric representation

With a \emph{parametric representation}, a curve $\p{c}$ is given as a
\alert{point-valued map} of a single real parameter:
$$
\p{c}: D \rightarrow \E^{n}\quad\mbox{such that}\quad \p{c}(u) = 
\p{o} +
\vet{ x_{1}(u) & \ldots& x_{n}(u) }^{T}
$$

where $\p{o}$ is the origin of the reference frame, and $D\subset\R$
often coincides with the standard real interval $[0,1]$.  

*	When $n=2,3$ the curve is said to be a _plane_ or a _space curve_,
respectively.  

*	The **component functions** $x_{i}:\R\rightarrow\R$,
$i=1,\ldots,n$, are called the \emph{coordinate maps} of the curve. 

*	The curve as a _locus of points_ should be properly called the
\emph{image} of the curve. 

# Polynomial parametric curves

## Parametric curves in graphics and CAD

The use of parametric curves in graphics and CAD started at the end of
the 1960s, first within the _aerospatial and automotive industries_,
both in Europe and in the USA, and _later in academia_, where applied
mathematicians were studying mathematical methods for **computer-aided
geometric design**, actually by simulating the hand-crafting of
physically modeled curves and surfaces.  

\vfill

Previously, various
instruments were used in the industry for this purpose, and in
particular some mechanical and graphical _"ad hoc"_ tools, from
_pantograph_ to a flexible ruler called a \emph{spline}, whose name was
soon extrapolated to denote the **mathematical
interpolation/approximation of sequences of points**

## Properties of parametric curves

*	Control handles

*	Multiple points

*	Affine and projective invariance

*	Local and global control

*	Variation diminishing

# Linear curves

## Algebraic form

In general, let consider the polynomial curve of first degree, said
\emph{in algebraic form}:
$$
\p{C}(u)  = \v{a} u + \v{b} 
$$
and write it as a product of matrices:
\begin{equation}
\p{C}(u) = \vet{u & 1} \vet{\v{a} \\ \v{b}} = \T{U}_1\ \T{M}_1
\label{eq:curve1}
\end{equation}


## Geometric form (1/2)

The matrix equation~(\ref{eq:curve1}) contains two vector degrees of
freedom, i.e.~two ``free" vector coefficients $\v{a}$ and $\v{b}$. 
In order to specify a given curve, we may specify two vector
constraints to be satisfied by $\v{a}$ and $\v{b}$.  

\begin{eqnarray*}
\p{C}(0) &=& \p{p}_1;\\
\p{C}(1) &=& \p{p}_2.
\end{eqnarray*}
By substituting $0$ and $1$ for $u$ in equation~\ref {eq:curve1}, we 
get, respectively:
$$
\p{p}_1 = \vet{0 & 1}\ \T{M}_1
$$
$$
\p{p}_2 = \vet{1 & 1}\ \T{M}_1
$$


## Geometric form (2/2)

The above vector equations can be collected into the following matrix 
equation:
$$
\vet{\p{p}_1 \\ \p{p}_2} =
\mat{0 & 1 \\ 1 & 1}\ \T{M}_1,
$$
from which we have
$$
\T{M}_1 = \mat{0 & 1 \\ 1 & 1}^{-1} \vet{\p{p}_1 \\ \p{p}_2}
= \mat{-1 & 1 \\ 1 & 0} \vet{\p{p}_1 \\ \p{p}_2},
$$
and, by substitution into equation~\ref{eq:curve1}, we get
\begin{equation}
\p{C}(u) = \vet{u & 1} \mat{-1 & 1 \\ 1 & 0} \vet{\p{p}_1 \\ 
\p{p}_2} = \T{U}_1\ \T{B}_1\ \T{G}_1.
\label{eq:fgeom1}
\end{equation}


## Terminology

Equation~\ref{eq:curve1} is called the _
algebraic form_ of the curve.  

Conversely, equation~\ref{eq:fgeom1} is
called the _geometric form_ **of passage through two given points** 

The matrix $\T{B}_{1}$ is called the **basis matrix**,
whereas the vector of points $\v{G}_{1}$ is called the **geometry
tensor** or tensor of _control handles_ of the geometric form. 

Finally, the vector of polynomial functions given by
$$
\T{U}_{1} \T{B}_{1} = \vet{u & 1} \mat{-1 & 1 \\ 1 & 0} = \vet{1 - u & u} = 
\vet{b_{1}(u) & b_{2}(u)}
$$
defines the **polynomial basis** of the geometric form, i.e.~its basis
functions, called also _blending functions_ of the curve.  


## Blending functions

The generic
curve point $\p{C}(u)$ is written as a _combination_ of **blending function**
with **control handles**, i.e.~as a sort of ``blend" of such data:
$$
\p{C}(u) = \sum_{i=0}^{1} b_{i}(u)\ \p{p}_{i}.
$$





<!-- 

A geometric \emph{model} is a pair (\emph{geometry}, \emph{topology}) in a given coordinate system, 

\pause

\emph{topology} is the LAR specification of highest dimensional cells of a cellular decomposition of the model space, 

\emph{geometry} is specified by the coordinates of \emph{vertices}, the spatial embedding of 0-cells of the cellular decomposition of space. 

\pause

*	A model is either an instance of the \texttt{Model} class, or simply a pair (\texttt{vertices}, \texttt{cells}), 
where 

*	\texttt{vertices} is a two-dimensional array of floats arranged by rows

*	\texttt{cells} is a list of lists of vertex indices


## Structures


A \emph{structure} is the LAR representation of a hierarchical organisation of spaces into substructures, 
where each part \emph{may} be  specified in a \emph{local coordinate system}. 

A structure is given as an \emph{(ordered) list of substructures and transformations} of coordinates, 
that apply to all the substructures following in the same list. 

\pause

*	A structure gives a \alert{graph of the scene}, since a substructure may be given a name, 
and referenced within other structures.  


*	The \emph{structure network}, including references, can be seen as an **acyclic directed multigraph**


*	\emph{Struct} class, whose parameter is a list of either other structures, or models, 
or transformations of coordinates, or references to structures or models.
 


## Assemblies

An assembly is an \emph{(unordered) list of models} all \emph{embedded in the same coordinate space}, 
i.e. all using the same coordinate system (the \emph{world coordinate system}, WCS)

*	An assembly may be either defined by the user as a list of models, or automatically generated 
by the \emph{traversal} of a structure network. 

*	At traversal time, all the structures and models are transformed from local coordinate systems to the world coordinates, 
that correspond to the coordinate frame of the root of the traversed network. 

*	An assembly is the linearised version of the traversed structure network, 
where all the models are using the world coordinate system.
 


# Affine transformations [`larlib`](https://github.com/cvdlab/lar-cc/)

## Design decision [_`larlib`_](https://github.com/cvdlab/lar-cc)

*     assume `scipy`'s `ndarray` as type of vertices, stored in row-major order;

*     use the last coordinate as homogeneous coordinate of vertices, but do not store it explicitly;

*     store explicitly the homogeneous coordinate of transformation matrices.

*     use labels `verts` and `mat` to distinguish between vertices and transformation matrices.

*     transformation matrices are dimension-independent

*	  `mat` dimension is computed as the length of parameter vector passed to the generating function.
 

## Elementary transformations: Translation matrices

```{.python}
def t(*args): 
    d = len(args)
    mat = scipy.identity(d+1)
    for k in range(d): 
        mat[k,d] = args[k]
    return mat.view(Mat)
```

## Elementary transformations: Scaling matrices

```{.python}
def s(*args): 
    d = len(args)
    mat = scipy.identity(d+1)
    for k in range(d): 
        mat[k,k] = args[k]
    return mat.view(Mat)
```

## Elementary transformations: Rotation matrices

```{.python}
def r(*args): 
    args = list(args)
    n = len(args)
    @< plane rotation (in 2D) @>
    @< space rotation (in 3D) @>
    return mat.view(Mat)
```

plane rotation (in 2D)

```{.python}
if n == 1: # rotation in 2D
    angle = args[0]; cos = COS(angle); sin = SIN(angle)
    mat = scipy.identity(3)
    mat[0,0] = cos;    mat[0,1] = -sin;
    mat[1,0] = sin;    mat[1,1] = cos;
```

## Elementary transformations: rotation matrices

\scriptsize

space rotation (in 3D)

```{.python}
if n == 3: # rotation in 3D
    mat = scipy.identity(4)
    angle = VECTNORM(args); axis = UNITVECT(args)
    cos = COS(angle); sin = SIN(angle)
    @< elementary rotations (in 3D) @>
    @< general rotations (in 3D) @>
```

elementary rotations (in 3D)

```{.python}
if axis[1]==axis[2]==0.0:    # rotation about x
    mat[1,1] = cos;    mat[1,2] = -sin;
    mat[2,1] = sin;    mat[2,2] = cos;
elif axis[0]==axis[2]==0.0:    # rotation about y
    mat[0,0] = cos;    mat[0,2] = sin;
    mat[2,0] = -sin;    mat[2,2] = cos;
elif axis[0]==axis[1]==0.0:    # rotation about z
    mat[0,0] = cos;    mat[0,1] = -sin;
    mat[1,0] = sin;    mat[1,1] = cos;
```

## Elementary transformations: rotation matrices

general rotations (in 3D)

```{.python}
else:  # general 3D rotation (Rodrigues' rotation formula)    
    I = scipy.identity(3) 
    u = axis
    
    Ux = scipy.array([
        [0,        -u[2],      u[1]],
        [u[2],        0,     -u[0]],
        [-u[1],     u[0],         0]])
    UU = scipy.array([
        [u[0]*u[0],    u[0]*u[1],    u[0]*u[2]],
        [u[1]*u[0],    u[1]*u[1],    u[1]*u[2]],
        [u[2]*u[0],    u[2]*u[1],    u[2]*u[2]]])
    mat[:3,:3] = cos*I + sin*Ux + (1.0-cos)*UU
```

## Hierarchical complexes

*Hierarchical models* of **assemblies** are generated by an aggregation
of *subassemblies*

each one defined in a **local coordinate system**, and
relocated by affine transformations of coordinates


+	each elementary part and each assembly, at every hierarchical level, 
	are *defined independently from each other*, using a local coordinate frame, 
	suitably chosen to make its definition easier
	
+	*only one copy* of each component *is stored* in the memory, 
	and may be instanced in different locations and orientations how many times it is needed.

# Traversal algorithm
## Emulation of scene multigraph traversal

use two types of nodes:

*	\emph{numbers} (think of vertices)
*	\emph{strings} (think of transformation matrices)

. . .

any structure list may contain:

*	any combination of \alert{numbers}, \alert{strings}, and \alert{structure lists} ( either explicit, or via python references to structure lists, i.e. through names of structure \alert{variables} )


. . . 

### Design goal

All components of any structure are (recursively) transformed to the coordinate frame of the first element of the structure


## Emulation of scene multigraph traversal

```{.python}
from pyplasm import *
def __traverse(CTM, stack, o):
    for i in range(len(o)):
        if ISNUM(o[i]): print CTM, o[i]
        elif ISSTRING(o[i]): 
            CTM.append(o[i])
        elif ISSEQ(o[i]):
            stack.append(o[i])             # push the stack
            __traverse(CTM, stack, o[i])
            CTM = CTM[:-len(stack)]        # pop the stack

def algorithm(data):
    CTM,stack = ["I"],[]
    __traverse(CTM, stack, data)  
```
## Examples of multigraph traversal

\scriptsize

```{.python}
data = [1,"A", 2, 3, "B", [4, "C", 5], [6,"D", "E", 7, 8], 9]  
print algorithm(data)
>>>	['I'] 1
	['I', 'A'] 2
	['I', 'A'] 3
	['I', 'A', 'B'] 4
	['I', 'A', 'B', 'C'] 5
	['I', 'A', 'B'] 6
	['I', 'A', 'B', 'D', 'E'] 7
	['I', 'A', 'B', 'D', 'E'] 8
	['I', 'A', 'B'] 9

data = [1,"A", [2, 3, "B", 4, "C", 5, 6,"D"], "E", 7, 8, 9]  
print algorithm(data)
>>>	['I'] 1
	['I', 'A'] 2
	['I', 'A'] 3
	['I', 'A', 'B'] 4
	['I', 'A', 'B', 'C'] 5
	['I', 'A', 'B', 'C'] 6
	['I', 'A', 'B', 'C', 'E'] 7
	['I', 'A', 'B', 'C', 'E'] 8
	['I', 'A', 'B', 'C', 'E'] 9
```
## Examples of multigraph traversal

\scriptsize

```{.python}
dat = [2, 3, "B", 4, "C", 5, 6,"D"]
print algorithm(dat)
>>>	['I'] 2
	['I'] 3
	['I', 'B'] 4
	['I', 'B', 'C'] 5
	['I', 'B', 'C'] 6

data = [1,"A", dat, "E", 7, 8, 9]
print algorithm(data)
>>>	['I'] 1
	['I', 'A'] 2
	['I', 'A'] 3
	['I', 'A', 'B'] 4
	['I', 'A', 'B', 'C'] 5
	['I', 'A', 'B', 'C'] 6
	['I', 'A', 'B', 'C', 'E'] 7
	['I', 'A', 'B', 'C', 'E'] 8
	['I', 'A', 'B', 'C', 'E'] 9
```
## Algorithm: geometric structure traversal


\begin{figure}[htbp] %  figure placement: here, top, bottom, or page
   \centering
   \includegraphics[width=0.8\linewidth]{traversal} 
   \caption{Traversal algorithm of an acyclic multigraph.}
   \label{fig:traversal}
\end{figure}


# LAR-CC implementation
## Algorithm: geometric structure traversal
\framesubtitle{decides between  different cases, depending on the type of the current object}

\scriptsize 

```{.python}
def traversal(CTM, stack, obj, scene=[]):
    for i in range(len(obj)):
        if isinstance(obj[i],Model): 
            scene += [larApply(CTM)(obj[i])]
        elif (isinstance(obj[i],tuple) or isinstance(obj[i],list)) and (
                len(obj[i])==2 or len(obj[i])==3):
            scene += [larApply(CTM)(obj[i])]
        elif isinstance(obj[i],Mat): 
            CTM = scipy.dot(CTM, obj[i])
        elif isinstance(obj[i],Struct):
            stack.append(CTM) 
            traversal(CTM, stack, obj[i], scene)
            CTM = stack.pop()
    return scene
```

*  If the object is a \texttt{Model} instance, then applies to it the \texttt{CTM} matrix; 
*  else if the object is a \texttt{Mat} instance, then the \texttt{CTM} matrix is updated by (right) product with it; 
*  else if the object is a \texttt{Struct} instance, then the \texttt{CTM} is pushed on the stack, initially empty, 
*  then the \texttt{traversal} is called (recursion), 
*  and finally, at (each) return from recursion, the \texttt{CTM} is recovered by popping the stack.


# Examples
## 

We start with a simple 2D example of a non-nested list of translated 2D object instances and rotation about the origin.

\scriptsize

```{.python}
""" Example of non-nested structure with translation and rotations """
import sys; sys.path.insert(0, 'lib/py/')
from larlib import *

square = larCuboids([1,1])
table = larApply( t(-.5,-.5) )(square)
chair = larApply( s(.35,.35) )(table)
chair1 = larApply( t(.75, 0) )(chair)
chair2 = larApply( r(PI/2) )(chair1)
chair3 = larApply( r(PI/2) )(chair2)
chair4 = larApply( r(PI/2) )(chair3)
scene = Struct([table,chair1,chair2,chair3,chair4])
VIEW(SKEL_1(STRUCT(MKPOLS(struct2lar(scene)))))
```
## Example:  Table and chairs

\begin{figure}[htbp] %  figure placement: here, top, bottom, or page
   \centering
   \includegraphics[width=0.5\linewidth]{table1} 
   \caption{Table and chairs: non-nested list}
   \label{fig:traversal}
\end{figure}

## 

A different composition of transformations, from local to global coordinate frames, is used in the following example.

\scriptsize

```{.python}
""" Example of non-nested structure with translation and rotations """
import sys; sys.path.insert(0, 'lib/py/')
from larlib import *

square = larCuboids([1,1])
table = larApply( t(-.5,-.5) )(square)
chair = larApply( s(.35,.35) )(table)
chair = larApply( t(.75, 0) )(chair)
struct = Struct([table] + 4*[chair, r(PI/2)])
scene = evalStruct(struct)
VIEW(SKEL_1(STRUCT(CAT(AA(MKPOLS)(scene)))))
```
## 
Finally, a similar 2D example is given, by nesting one (or more) structures via separate definition and call by reference from the interior. 
\scriptsize

```{.python}
""" Example of nested structures with translation and rotations """
import sys; sys.path.insert(0, 'lib/py/')
from larlib import *

square = larCuboids([1,1])
table = larApply( t(-.5,-.5) )(square)
chair = Struct([ t(.75, 0), s(.35,.35), table ])
struct = Struct( [t(2,1)] + [table] + 4*[r(PI/2), chair])
struct = Struct(10*[struct,t(0,2.5)])
scene = Struct(10*[struct,t(3,0)])
VIEW(SKEL_1(STRUCT(MKPOLS(struct2lar(scene)))))
```
## Example:  Table and chairs

\begin{figure}[htbp] %  figure placement: here, top, bottom, or page
   \centering
   \includegraphics[width=0.5\linewidth]{table2} 
   \caption{Table and chairs: nesting one (or more) structures}
   \label{fig:traversal}
\end{figure}


# 2D  robot arm
## Example:  2D  robot arm (\texttt{lar-cc} package)

\scriptsize

```{.python}
from larlib import *

link = Struct([t(-1,-19),s(2,20),larCuboids([1,1])])
def joint(a): return [t(0,-18),r(a*PI/180)]
def arm(a1,a2,a3):
    return Struct([s(.1,.1)] + [link] + joint(a1) + [link] + joint(a2)
                        + [link] + joint(a3) + [link])

hpcs = MKPOLS(struct2lar(arm(30,60,90)))
VIEW(STRUCT(hpcs)) 
```
## Example:  2D  robot arm (\texttt{lar-cc} package)

\begin{figure}[htbp] %  figure placement: here, top, bottom, or page
   \centering
   \includegraphics[width=0.5\linewidth]{robot1} 
   \caption{2D  robot arm (\texttt{lar-cc} package)}
   \label{fig:traversal}
\end{figure}

## Example:  2D  robot arm  (\texttt{pyplasm} package)

\scriptsize

```{.python}
from pyplasm import *

link = T([1,2])([-1,-19])(CUBOID([2,20]))

def joint(a):
	return COMP([T(2)(-18), R([1,2])(a*PI/180)])
	
def arm(a1,a2,a3):
	return STRUCT([ S([1,2])([.1,.1]), link, joint(a1), COLOR(RED)(link),
				 joint(a2), COLOR(GREEN)(link),
				 joint(a3), COLOR(BLUE)(link) ])
	
VIEW(arm(30,60,90))
```
## Example:  2D  robot arm (\texttt{pyplasm} package)

\begin{figure}[htbp] %  figure placement: here, top, bottom, or page
   \centering
   \includegraphics[width=0.5\linewidth]{robot2} 
   \caption{2D  robot arm (\texttt{pyplasm} package)}
   \label{fig:traversal}
\end{figure}
 -->

