% Computational Graphics: Lecture 3
% Alberto Paoluzzi 
% \today

## Outline: Algebra reminders

\tableofcontents


# Linear spaces


## Definition

A **linear** (or *vector*) **space** ${\cal V}$ over a field ${\cal F}$ is a set with two composition rules, such that, for each $\p{u},\p{v},\p{w}\in{\cal V}$ and for each $\alpha,\beta\in {\cal F}$, the rules $+, \cdot$  satisfy the following axioms:


#. $\p{v}+\p{w} = \p{w}+\p{v}$; $\hfill$ (commutativity of addition)

#. $\p{u}+(\p{v}+\p{w}) = (\p{u}+\p{v})+\p{w}$; $\hfill$ (associativity of addition)

#. there is a $\p{0}\in{\cal V}$ such that $\p{v}+\p{0}=\p{v}$; $\hfill$ (neutral el. of addition)

#. there is a $-\p{v}\in{\cal V}$ such that $\p{v}+(-\p{v})=\p{0}$; $\hfill$ (inverse of add.)

#. $\alpha\cdot(\p{v}+\p{w}) = \alpha\cdot \p{v} + \alpha\cdot \p{w}$; $\hfill$ (distrib. of addition w.r.t. product)

#. $(\alpha+\beta)\cdot \p{v} = \alpha\cdot \p{v} + \alpha\cdot \p{v}$; $\hfill$ (distrib. of product w.r.t. addition)

#. $\alpha\cdot(\beta\cdot \p{v}) = (\alpha \beta) \cdot \p{v}$; $\hfill$ (associativity of product)

#. $1 \cdot \p{v} = \p{v}$. $\hfill$ (neutral element of product)



## Example: vector space of real matrices

Let ${\cal M}^m_n(\R)$ be the set of $m\times n$ matrices with elements in the field $\R$.  An element $A$ in such a set is denoted as $$A=(\alpha_{ij})$$

. . .

**Addition** and **multiplication by a scalar** are defined component-wise: $$ A+B=(\alpha_{ij})+(\beta_{ij})=(\alpha_{ij}+\beta_{ij}) $$ $$ \gamma A=\gamma(\alpha_{ij})=(\gamma\alpha_{ij}) $$



# Linear combinations


## Linear combination


Let $\v{v}_1,\v{v}_2,\ldots,\v{v}_n\in{\cal V}$ and $\alpha_1,\alpha_2, \ldots,\alpha_n\in {\cal F}$,


The vector $$ \alpha_1 \v{v}_1 + \cdots + \alpha_n \v{v}_n = \sum_{i=1}^n \alpha_i \v{v}_i \in{\cal V} $$ is called a **linear combination** of vectors $\v{v}_1,\v{v}_2,\ldots,\v{v}_n$ with scalars $\alpha_1,\alpha_2,\ldots,\alpha_n\in {\cal F}$


# Subspaces

## Subspace

Let $({\cal V},+,\cdot)$ be a vector space on the field ${\cal F}$.

${\cal U}\subset{\cal V}$ is a **subspace** of ${\cal V}$ 
:	if $({\cal U},+,\cdot)$ is a vector space with respect to the same operations.

${\cal U}\subset{\cal V}$ is a \emph{subspace} of ${\cal V}$ 

:	if and only if
:	${\cal U}\neq\emptyset$; 
:	for each $\alpha\in {\cal F}$ and $\v{u}_1,\v{u}_2\in{\cal U}$, $\alpha \v{u}_1+\v{u}_2 \in{\cal U}$

codimension
:	of a subspace ${\cal U}\subset{\cal V}$ 
:	is defined as $\dim{\cal V} - \dim{\cal U}$

. . .

\begin{question}{Examples of codimension?} 
in 1D, 2D, 3D
\end{question}

# Spans


## Span

* The set of all linear combinations of elements of a set $S \subset {\cal V}$ is a subspace of ${\cal V}$.

* Such a subspace is called the **span of $S$** and is denoted as $$ \lin S $$

* If a subspace ${\cal U}$ of ${\cal V}$ can be generated as the span of a set $S$ of vectors in ${\cal V}$, then $S$ is called a \emph{generating set} or a \emph{spanning set} for ${\cal U}$.


## Linear independence

* A set of vectors $\{\v{v}_1,\v{v}_2,\ldots,\v{v}_n\}$ is **linearly independent** if $$ \sum_{i=1}^n \alpha_i \v{v}_i = \v{0} $$ implies that $\alpha_i=0$ for each $i$

* As a consequence, *a set of vectors is linearly independent* when none of them belongs to the span of the others.



# Bases


## Bases and coordinates

When working with vector spaces, the concept of **basis**, a
*discrete subset of linearly independent elements*, is probably the most
useful to deal with.  

* each element of the space can be
*represented **uniquely** as linear combination of basis elements*  

* this
leads to a **parametrization** of the space, i.e. to *represent
each element by a sequence of scalars*, called its
**coordinates** with respect to the chosen basis.

## Bases

A set of vectors $\{\v{e}_1,\v{e}_2,\ldots,\v{e}_n\}$ is a **basis** for
the vector space ${\cal V}$ iff

#. the set is linearly independent, and
#. ${\cal V} = \lin \{ \v{e}_1,\v{e}_2,\ldots,\v{e}_n \}$


## Bases

*	Every two bases of ${\cal V}$ have the same number  of elements, that is called the *dimension* of  ${\cal V}$ and is denoted $$ \dim {\cal V} $$

*	Some important **properties** of the bases of a vector space are:

	#.  each spanning set for  ${\cal V}$ contains a basis;
	#.  each minimal spanning set is a basis;
	#.  each linearly independent set of vectors is contained in a basis;
	#.  each maximal set of linearly independent vectors is a basis;



## Example: vector space of polynomials of degree $\leq n$

A linear space we make often use of in *Computer Graphics* and *Geometric modeling* 
is the space of dimension $n+1$:
$$
\P^n(\R) = \{ p: \R \rightarrow \R: u \mapsto \sum_{i=0}^n a_i u^i , a_i\in\R\}
$$
of univariate **polynomials of degree $\leq n$** on the real field (with real coefficients),
with $p^i \in P_n$, where
$$
P_n = (p^n, p^{n-1}, ..., p^1, p^0)  \quad\mbox{and}\quad p^i: u \mapsto u^i 
$$
is **the power basis**.



## Components

If $(\v{e}_1,\v{e}_2,\ldots,\v{e}_n)$ is an ordered basis for ${\cal V}$,
then for each $\v{v}\in{\cal V}$ there exists a **unique** $n$-tuple of
scalars $\alpha_1,\alpha_2,\ldots, \alpha_n \in {\cal F}$ such that
$$
\v{v}=\sum_{i=1}^n \alpha_i \v{e}_i.
$$

## Components

The $n$-tuple of scalars $(\alpha_i)$ is called the
**components** of $\v{v}$ with respect to the
ordered basis $(\v{e}_1,\v{e}_2,\ldots,\v{e}_n)$.  

* If such a $n$-tuple
were not unique, then $\v{v}=\sum \alpha_i \v{e}_i=\sum \beta_i \v{e}_i$ 

* But this one would imply $\sum(\alpha_i-\beta_i) \v{e}_i
=\v{0}$, hence $(\alpha_i-\beta_i)=0$, 

* i.e. $\alpha_i=\beta_i$, for every $i$.

## Change of basis

* Let $B = (\v{e}_1, \ldots, \v{e}_n)\subset\cal V$ be a basis for $\cal V$. 

* Of course, the $\v{e}_i$ coordinates are $\vet{1 & 0 & \cdots & 0}, \vet{0 & 1 & \cdots & 0}, \ldots, \vet{0 & 0 & \cdots & 1}$, and, in $B$ coordinates, the basis is represented by the matrix 
$$ [B] = [I] $$.

* If we take $n$  (linearly independent) vectors $V = (\v{v}_1, \ldots, \v{v}_n) \subset\cal V$, represented in $B$ coordinates as $[V]$, and want to parametrize $\cal V$ with respect to the new basis, we have, for transformation of coordinates:
$$
[I] = [T][V]
$$

* and hence:
$$
[T] = [V]^{-1}
$$


## Example: two polynomial bases

* Let $P_3 = (u^3,u^2,u,1)$ 

* and $B_3 = ((1-u)^3, 3u(1-u)^2, 3u^2(1-u), u^3)$ be two ordered bases 

* for the linear space $\P^3(\R)$ of polynomials with  $\deg \leq 3$.

* the $[B_3]$ matrix in the $P_3$ basis is 
$$ [B_3]_{P_3} = 
\mat{-1 & 3 & -3 & 1 \\
	3 & -6 & 3 & 0 \\
	-3 & 3 & 0 & 0 \\
	1 & 0 & 0 & 0} $$

* the $[P_3]$ matrix in the $B_3$ basis is 
$$ [P_3]_{B_3} =  [B_3]_{P_3}^{-1} = 
\mat{0 & 0 & 0 & 1 \\
	0 & 0 & 1/3 & 1 \\
	0 & 1/3 & 1/6 & 1 \\
	1 & 1 & 1 & 1} $$
	
* **WHY ?**




# Affine spaces

## Affine space

The idea of affine space corresponds to that of a
set of points where the **displacement** from a point $\p{x}$ to another
point $\p{y}$ is obtained by summing a vector $\v{v}$ to the $\p{x}$ point.



## Definition

A set ${\cal A}$ of points is called an **affine space** modeled on
the vector space ${\cal V}$ if there is a function 
$$
{\cal A}\times{\cal V}\rightarrow{\cal A}:(\p{x},\v{v})\mapsto \p{x}+\v{v}
$$
called **affine action**\index{Affine!action}, with the properties:

. . .


#. $(\p{x}+\v{v})+\v{w} = \p{x}+(\v{v}+\v{w})$ for each $\p{x}\in{\cal A}$ and each $\v{v},\v{w}\in{\cal V}$;

#. $\p{x}+\p{0}=\p{x}$ for each $\p{x}\in{\cal A}$, where $\p{0}\in{\cal V}$ is the null vector;

#. for each pair $\p{x},\p{y}\in{\cal A}$ there is a unique $(\p{y}-\p{x})\in{\cal V}$ such that
$$
\p{x}+(\p{y}-\p{x})=\p{y}.
$$

## Dimension

The affine space ${\cal A}$  is said of *dimension* $n$ if modeled
on a vector space ${\cal V}$ of dimension $n$.


## Vector sum vs affine action


\begin{figure}
\centerline{\includegraphics[width=\linewidth]{../images/somma.pdf}}
\caption{(a) Vector sum and difference are given by the parallelogram rule
(b)~associativity of displacement (point and vector sum) in an affine
space}
\end{figure}


## Operations on vectors and points

* The **addition** of vectors is a primitive operation in a vector space.

* The **difference** of vectors is defined through the two primitive
operations:
$$
\v{v}_1-\v{v}_2=\v{v}_1+(-1)\v{v}_2.
$$

* Addition and difference of vectors are geometrically produced by the
*parallelogram rule*

* notice also the *associative property* of the affine action on a point space.


## Operations on vectors and points

The sum of a set $\{\v{v}_i\}$ of vectors ($i=1,\ldots,n$) can be
geometrically obtained, in an affine space:

* by setting $\p{p}_0=\p{0}$
* $\p{p}_i=\p{p}_{i-1}+\v{v}_i$, 
* so that $$ \sum_{i} \v{v}_i= \p{p}_n-\p{p}_0 $$

Remark: operations on points

#. the *addition of points* is **not** defined;
#. the *difference of two points* is a **vector**;
#. the *sum of a point and a vector* is a **point**.





# Affine combinations

## Positive, affine and convex combinations

Three types of combinations of vectors or points can be defined. They 
lead to the concepts of **cones**, **hyperplanes** and **convex sets**, 
respectively.


## Positive combination

Let $\p{v}_0,\ldots,\p{v}_d\in{\cal \R}^n$ and $\alpha_0,
\ldots,\alpha_d\in \R^{+}\cup\{0\}$.  

	
The vector
$$
\alpha_0 \p{v}_0 + \cdots + \alpha_d \p{v}_d = \sum_{i=0}^d \alpha_i \p{v}_i
$$
is called a **positive combination** of such vectors.  

	
The set of all the positive combinations of
$\{\p{v}_0,\ldots,\p{v}_d\}$ is called the **positive hull** of $\{\p{v}_0,\ldots,\p{v}_d\}$ and
denoted *$\pos \{\p{v}_0,\ldots,\p{v}_d\}$.* 

	
This set is also called the **cone** generated by the given vectors

## Affine combination

Let $\p{p}_0,\ldots,\p{p}_d\in{\E}^n$ and $\alpha_0,
\ldots,\alpha_d\in \R$, such that $\alpha_0  + \cdots + \alpha_d =1$.

The point
$$
\sum_{i=0}^d \alpha_i \p{p}_i
:= \p{p}_0 + \sum_{i=1}^d \alpha_i (\p{p}_i - \p{p}_0)
$$
is called an **affine combination** of the points $\p{p}_0,\ldots,\p{p}_d$.

## Affine combination

The set of all affine combinations of
$\{\p{p}_0,\ldots,\p{p}_d\}$ is an **affine
subspace**, denoted by *$\aff \{\p{p}_0,\ldots,\p{p}_d\}$* 

It is easy to verify that:
$$
\aff \{\p{p}_0,\ldots,\p{p}_d\} = 
\p{p}_0 + \lin\{ \p{p}_1-\p{p}_0,\ldots,\p{p}_d-\p{p}_0 \}.
$$

## Affine combination

#. The **dimension** of an affine subspace is the dimension of the 
corresponding linear vector space. 

#. Affine subspaces of $\E^{d}$ with 
dimensions 0, 1, 2 and $d-1$ are called **points**, **lines**, 
**planes** and **hyperplanes**, respectively.

#. Affine subspaces are also called **flats**.

. . . 

### Double description

Every affine subspace can be described either as 

- the *intersection* of affine *hyperplanes*, or as 
- the *affine hull* of a finite set of *points*.


# Convex combinations

## Convex combination

Let $\p{p}_0,\ldots,\p{p}_d\in{\E}^n$ and *$\alpha_0,\ldots,\alpha_d \geq 0$*, 
with *$\alpha_0  + \cdots + \alpha_d =1$*.

The point 
$$
\alpha_0 \p{p}_0 + \cdots + \alpha_d \p{p}_d = \sum_{i=0}^d \alpha_i \p{p}_i
$$
is called a **convex combination** of points $\p{p}_0,\ldots,\p{p}_d$.

A **convex** combinations is both *positive* and *affine*.  

## Convex hull

The set of **all**
convex combinations of $\{\p{p}_0,\ldots,\p{p}_d\}$ is a convex set,
called **convex hull** of
$\{\p{p}_0,\ldots,\p{p}_d\}$, and is denoted by *$\conv\{\p{p}_0,\ldots,\p{p}_d\}$*.


. . . 

### Properties

- the convex hull of a set of points is the *intersection of all convex sets* that contain them
- the convex hull of a set of points is the *smallest set* that contains them



## ASSIGNMENT


*	Produce (and draw) 100 random points within the unit square $[0,1]^2$;

*	Produce (and draw) 1000 random points within $S_1$, the 1D sphere (circle)  of unit radius centered at the origin $(0,0)$;




## References

[\emph{Linear Algebra Done Right} book](http://www.amazon.it/Linear-Algebra-Right-Sheldon-Axler/dp/0387982582)

[NumPy \emph{tutorial}](http://wiki.scipy.org/Tentative_NumPy_Tutorial)

