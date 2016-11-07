% Computational Graphics: Lecture 7
% Alberto Paoluzzi
% \today

## Outline: Cell complexes (LAR)

\tableofcontents

# Solid Modeling


## Representation scheme: definition

\footnotesize

mapping \textbf{$s : M \to R$} from a space $M$ of mathematical models to a space $R$ of computer representations

> \includegraphics[width=0.6\linewidth]{images/schema}

#. The $M$ set contains the mathematical models of the class of solid objects the scheme aims to represent

#. The $R$ set contains the symbolic representations, i.e. the proper data structures, built according to a suitable grammar

\tiny 

A. Requicha, \emph{Representations for Rigid Solids: Theory, Methods, and Systems}, \alert{ACM Comput. Surv.}, 1980.

V. Shapiro, \emph{Solid Modeling}, In \alert{Handbook of Computer Aided Geometric Design}, 2001


## Representation schemes 

\footnotesize

Most of such papers introduce or discuss one or more representation schemes ...


\begin{columns}\tiny
\begin{column}{6.4cm}
\begin{enumerate}
\item
Requicha, ACM Comput. Surv., 1980 \cite{Requicha:1980:RRS:356827.356833}
\item
Requicha \& Voelcker, PEP TM-25, 1977, \cite{RequichaVoelcker:77}
\item
Rossignac \& Requicha, Comput. Aided Des., 1991, \cite{Rossignac:1991:CNG:115604.115606}
\item
Bowyer, SVLIS, 1994, \cite{bowyer1995svlis}
\item
Baumgart, Stan-CS-320, 1972, \cite{Baumgart:1972:WEP:891970}
\item
Braid, Commun. ACM, 1975, \cite{Braid:1975:SSB:360715.360727}
\item
Dobkin \& Laszlo, ACM SCG, 1987, \cite{Dobkin:1987:PMT:41958.41967}
\item
Guibas \& Stolfi, ACM Trans. Graph., 1985, \cite{Guibas:1985:PMG:282918.282923}
\item
Woo, {IEEE} Comp. Graph. \& Appl., 1985, \cite{woo:85}
\item
Yamaguchi \& Kimura, Comp. Graph. \& Appl., 1995, \cite{yamaguchi1995ntb}
\item
Gursoz \& Choi \& Prinz, Geom.Mod., 1990, \cite{wozny1990geometric}
\item
S.S.Lee \& K.Lee, ACM SMA, 2001, \cite{Lee:2001:PES:376957.376976}
\item
Rossignac \& O'Connor, IFIP WG 5.2, 1988, \cite{Rossignac:SGC:90}
\item
Weiler, {IEEE} Comp. Graph. \& Appl., 1985, \cite{4055948}
\item
Silva, Rochester,  PEP TM-36, 1981, \cite{Silva:81}
\end{enumerate}
\end{column}

\begin{column}{6.5cm}
\begin{enumerate}
\item[\myenum{16}]
Shapiro, Cornell Ph.D Th., 1991, \cite{Shapiro:1991:RSS:124951}
\item[\myenum{17}]
Paoluzzi et al., ACM Trans. Graph., 1993, \cite{Paoluzzi:1993:DMS:169728.169719}
\item[\myenum{18}]
Pratt \& Anderson, ICAP, 1994, \cite{Pratt94ashape}
\item[\myenum{19}]
Bowyer, Djinn, 1995, \cite{bowyer1995introducing}
\item[\myenum{20}]
Gomes et al., ACM SMA, 1999, \cite{Gomes:1999:MMB:304012.304039}
\item[\myenum{21}]
Raghothama \& Shapiro, ACM Trans. Graph., 1998, \cite{Raghothama:1998:BRD:293145.293148}
\item[\myenum{22}]
Shapiro \& Vossler, ACM SMA, 1995, \cite{Shapiro:1995:PFS:218013.218029}
\item[\myenum{23}]
Hoffmann \& Kim, Comput. Aided Des., 2001, \cite{HoffmannK01}
\item[\myenum{24}]
Raghothama \& Shapiro, ACM SMA, 1999, \cite{Raghothama:1999:CUD:304012.304019}
\item[\myenum{25}]
DiCarlo et al., IEEE TASE, 2008, \cite{ieee-tase}
\item[\myenum{26}]
Bajaj et al., CAD\&A, 2006, \cite{cadanda}
\item[\myenum{27}]
Pascucci et al., ACM SMA, 1995, \cite{Pascucci:1995:DCB:218013.218055}
\item[\myenum{28}]
Paoluzzi et al., ACM Trans. Graph., 1995, \cite{Paoluzzi:1995:GPP:212332.212349}
\item[\myenum{29}]
Paoluzzi et al., Comput. Aided Des., 1989, \cite{Paoluzzi:1989:BAO:70248.70249}
\item[\myenum{30}]
Ala, IEEE Comput. Graph. Appl., 1992, \cite{Ala:1992:PAB:616022.617736}
\end{enumerate}
\end{column}
\end{columns}

\centering\vfill

and much more ...

## Representation scheme: Quad-Edge data structure
\framesubtitle{(Guibas \& Stolfi, ACM Transactions on Graphics, 1985)}

\includegraphics[width=\linewidth]{images/fig2}


## Representation scheme: Partial-Entity data structure 
\framesubtitle{(Sang Hun Lee \& Kunwoo Lee, ACM Solid Modeling, 2001)}

\includegraphics[width=\linewidth]{images/fig1}


## Representation scheme: Coupling Entities data structure
\framesubtitle{(Yamaguchi \& Kimura, IEEE Computer Graphics and Applications, 1995)}

\includegraphics[width=\linewidth]{images/fig3}


# Space decompositions

## Join of pointsets

The **join** of two sets $P, Q \subset \E^n$ is the convex hull of their points:

$$PQ = join(P, Q) := \{ \gamma p + \lambda q, \ p \in P,\ q \in Q \}$$
$$\gamma,\lambda \in \R,\ \gamma,\lambda \geq 0,\ \gamma + \lambda = 1$$. 

The join operation is *associative* and *commutative*. 


## Join of pointsets: examples

\scriptsize

```{.python}
pts = [[0,0],[.5,0],[0,.5],[.5,.5],
	   [1,.5],[1.5,.5],[1.5,1],[.25,1]]		# coords
P = AA(MK)(pts)								# 0-polyhedra
S = AA(JOIN)([P[0:4],P[4:7],P[7]])			# array of d-polyhedra
H = JOIN(S)									# 2-polyhedron

VIEW(STRUCT(AA(SKELETON(1))(S)))
VIEW(H)
```
\vspace{-3mm}
\begin{figure}[htbp] %  figure placement: here, top, bottom, or page
   \centering
   \includegraphics[height=0.3\textwidth,width=0.5\textwidth]{images/join1} 
   \includegraphics[height=0.3\textwidth,width=0.5\textwidth]{images/join2} 
   \caption{(a) 1-skeleton of pointsets in $S$; (b) convex hull $H$ of pointset $P$}
   \label{fig:example}
\end{figure}



## Simplex

A **simplex $\sigma\subset\E^n$** of order $d$, or $d$-simplex, is the **join** of $d + 1$ *affinely independent points*, called *vertices*. 

The $n + 1$ points $p_0,\ldots, p_n$ are **affinely independent** when the $n$ vectors $p_1-p_0,\ldots,p_n-p_0$ are *linearly independent*. 

A **$d$-simplex** can be seen as a **$d$-dimensional triangle**: 0-simplex is a *point*, 1-simplex is a *segment*, 2-simplex is a *triangle*, 3-simplex is a *tetrahedron*, and so on. 



## Simplex: examples


\scriptsize

```{.python}
s0,s1,s2,s3 = [SIMPLEX(d) for d in range(4)]	# array of standard d-simplices
VIEW(s1); VIEW(s2); VIEW(s3);					

points = [[1,1,1],[0,1,1],[1,0,0],[1,1,0]]		# coords of 4 points
tetra = JOIN(AA(MK)(points))					# 3-simplex
VIEW(tetra)

```

\begin{figure}[htbp] %  figure placement: here, top, bottom, or page
   \centering
   \includegraphics[height=0.25\textwidth,width=0.25\textwidth]{images/s1} 
   \includegraphics[height=0.25\textwidth,width=0.25\textwidth]{images/s2} 
   \includegraphics[height=0.25\textwidth,width=0.25\textwidth]{images/s3} 
   \includegraphics[height=0.25\textwidth,width=0.25\textwidth]{images/tetra} 
   \caption{(a,b,c) 1-, 2-, and 3-standard simplex; (d) 3-simplex defined by 4 points}
   \label{fig:example}
\end{figure}





## Simplicial complex

*Any subset* of $s + 1$ vertices ($0 \geq s \geq d$) of a $d$-simplex $\sigma$ defines an **$s$-simplex**, which is called **$s$-face** of $\sigma$.

\pause

A **simplicial complex** is a *set of simplices $\Sigma$*, verifying the following conditions: 

#. if $\sigma\in\Sigma$, then any $s$-face of $\sigma$ belongs to $\Sigma$; 
#. if $\sigma,\tau \in\Sigma$, then $\sigma\cap\tau \in\Sigma$.

\pause

**Geometric carrier** $|\Sigma|$ is the pointset union of simplices in $\Sigma$.



## Simplicial complex: examples

\scriptsize

```{.python}
from larlib import *								# import LAR library
V,CV = larSimplexGrid1([5,5,5])					# structured simplicial grid
FV = larSimplexFacets(CV)						# 2-simplicial grid
EV = larSimplexFacets(FV)						# 1-simplicial grid
VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS((V,CV))))
VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS((V,FV))))
VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS((V,EV))))

BV = [FV[t] for t in boundaryCells(CV,FV)]		# boundary 2-simplices
VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS((V,BV))))
```

\begin{figure}[htbp] %  figure placement: here, top, bottom, or page
	\includegraphics[height=0.25\linewidth,width=0.25\linewidth]{images/tetra5x5x5-3d} 
	\includegraphics[height=0.25\linewidth,width=0.25\linewidth]{images/tetra5x5x5-2d} 
	\includegraphics[height=0.25\linewidth,width=0.25\linewidth]{images/tetra5x5x5-1d} 
	\includegraphics[height=0.25\linewidth,width=0.25\linewidth]{images/tetra5x5x5-bd} 
   \label{fig:example}\scriptsize
   \caption{(a) 3-complex; (b) 2-subcomplex; (c)~1-subcomplex; (d)~2-boundary.}
\end{figure}



## Simplicial complex: examples \footnotesize\hfill (see [*Disk Point Picking*](http://mathworld.wolfram.com/DiskPointPicking.html))

\scriptsize

```{.python}
from larlib import *; from random import random as rand
points = [[2*PI*rand(),rand()] for k in range(1000)]
V = [[SQRT(r)*COS(alpha),SQRT(r)*SIN(alpha)] for alpha,r in points]
cells = [[k+1] for k,v in enumerate(V)]
VIEW(MKPOL([V,cells,None]))

from scipy.spatial import Delaunay
FV = Delaunay(array(V)).vertices
VIEW(EXPLODE(1.2,1.2,1)(MKPOLS((V,FV))))
VIEW(SKELETON(1)(STRUCT(MKPOLS((V,FV)))))
```

\begin{figure}[htbp] %  figure placement: here, top, bottom, or page
	\includegraphics[height=0.25\linewidth,width=0.25\linewidth]{images/tria0} 
	\includegraphics[height=0.25\linewidth,width=0.25\linewidth]{images/tria2} 
	\includegraphics[height=0.25\linewidth,width=0.25\linewidth]{images/tria1} 
   \caption{(a) Points; (b) Delaunay triangulation; (c)~1-skeleton.}
   \label{fig:example}
\end{figure}



## Simplicial complex: examples \footnotesize\hfill (see [*Disk Point Picking*](http://mathworld.wolfram.com/DiskPointPicking.html))

\scriptsize

```{.python}
from larlib import *; from random import random as rand
points = [[2*rand()-1,2*rand()-1,2*rand()-1] for k in range(30000)]
V = [p for p in points if VECTNORM(p) <= 1]
VIEW(STRUCT(MKPOLS((V,AA(LIST)(range(len(V)))))))


from scipy.spatial import Delaunay
CV = Delaunay(array(V)).vertices
def test(tetra): return AND([v[-1] < 0 for v in tetra])
CV = [cell for cell in CV if test([V[v] for v in cell]) ]
VIEW(STRUCT(MKPOLS((V,CV))))
```

\begin{figure}[htbp] %  figure placement: here, top, bottom, or page
	\includegraphics[height=0.25\linewidth,width=0.25\linewidth]{images/tria0} 
	\includegraphics[height=0.25\linewidth,width=0.25\linewidth]{images/tria2} 
	\includegraphics[height=0.25\linewidth,width=0.25\linewidth]{images/tria1} 
   \caption{(a) Points; (b) Delaunay triangulation; (c)~1-skeleton.}
   \label{fig:example}
\end{figure}



# Cellular complex
<!-- 

## CW-complex

\scriptsize

*	Roughly speaking, a [*CW-complex*](http://www.math.ksu.edu/~hansen/CWcomplexes.pdf) is made of *basic building blocks* called **cells**. 
*	The C stands for *closure-finite*, and the W for [*weak topology*](https://www.princeton.edu/~achaney/tmve/wiki100k/docs/Weak_topology.html).
*	**Closure-finite** means that *each closed cell* is covered by a **finite union** of *open cells*.

\pause

#.	An $n$-dimensional closed cell is the image of an $n$-disk under an attaching map. 
#.	*A simplex is a closed cell*, and more generally, **a convex polytope is a closed cell**. 
#.	An $n$-dimensional open cell is a topological space that is homeomorphic to the open disk. 
#.	A 0-dimensional open (and closed) cell is a *singleton* space. 

\pause

#### $n$-Dimensional disk:
$$ D^n = \{ x \in \R^n: |x| \leq 1 \}$$

#### Interior of $D^n \subset \R^n$:
$$ int(D^n) = \{ x \in \R^n: |x| \leq 1 \}$$

#### Boundary of $D^n \subset \R^n$:
$$ S^{n-1} = \{ x \in \R^n: |x| = 1 \}$$



##	CW-complex: inductive definition

\footnotesize

Let $X$ be a [*topological space*](http://mathworld.wolfram.com/TopologicalSpace.html).

Let $\Lambda (X) = \cup_p X_{p\in\N}$ be a [*partition*](http://en.wikipedia.org/wiki/Partition_of_a_set) of $X$, with $X_p$ the set of $p$-cells.

. . .

\begin{definition}[\alert{CW-structure}]
A \emph{CW-structure} on the space $X$ is a \href{http://en.wikipedia.org/wiki/Filtration_(mathematics)}{\emph{filtration}} 
$$
\emptyset = X^{-1} \subset X_0 \subset X_1 \subset\cdots\subset X_n = \Lambda (X),
$$
such that, for each $n$, the space $X_n$ is \href{http://mathworld.wolfram.com/Homeomorphic.html}{\emph{homeomorphic}} to a space obtained from $X_{n-1}$ by attachment of $n$-cells. 
\end{definition}

. . .

\begin{definition}[\alert{Cellular complex}]
A \emph{cellular complex} is a space endowed with a CW-structure.  
\end{definition}

. . .

A cellular complex is \emph{finite} when it contains a finite number of cells. 

 -->


## Politopal, simplicial, cuboidal complexes

\footnotesize

Cellular complexes characterised by different types of cells:

#.	In polytopal complexes cells are polytopes, i.e. bounded convex sets; 
#.	In simplicial complexes cells are  simplices, i.e. $d$-polyedra with $d + 1$ facets ($(d - 1)$-faces) and $d + 1$ vertices. 
#.	In cuboidal complexes cells are cuboids,  (in general, sets homeomorphic to) Cartesian products of intervals, i.e. $d$-polyedra with $2d$ facets and $2d$ vertices.



## Numbers of vertices and *facets*

\footnotesize

A **$d$-simplex**, or $d$-dimensional simplex, has **$d + 1$** *extremal points* called **vertices** and **$d + 1$** facets. 

*	a *point* (0-simplex) has $0 + 1 = 1$ vertices and 1 facet ($\emptyset$); 
*	an *edge* (1-simplex) has $1 + 1 = 2$ vertices and 2 facets; 
*	a *triangle* (2-simplex) has $2 + 1 = 3$ vertices and 3 facets; 
*	a *tetrahedron* (3-simplex) has $3 + 1 = 4$ vertices and 4 facets, etc. 

. . .
 
A **$d$-cuboid** has conversely **$2^d$ vertices** and **$2d$ facets**: 

*	a *point* (0-cuboid) has $2^0 = 1$ vertices and 0 facets; 
*	an *edge* (1-cuboid) has $2^1 = 2$ vertices and 2 facets; 
*	a *quadrilateral* (2-cuboid) has $2^2 = 4$ vertices and 4 facets; 
*	a *hexahedron* (3-cuboids) has $2^3 = 8$ vertices and 8 facets, etc.


## Cellular complex: properties 

*	Support $|K|$ of a cellular complex $K$ is the union of points  of its cells 

*	A triangulation of a polytope $P$ is a simplicial complex $K$ whose support is $|K| = P$

	-	For example, a triangulation  of a polygon is a subdivision in triangles 

\vfill

*	Simplices and  cuboids are polytopes. 

*	A polytope is always triangulable; 

	-	For example, a quadrilateral by be divided in two triangles, and a cube in either 5 or 6 tetrahedra without adding new vertices


# Simplicial mapping

## Simplicial mapping: definition

### Definition

A **simplicial map** is a map *between simplicial complexes* with the property that the images of the vertices of a simplex always span a simplex.

### Remarks

Simplicial maps are *determined by their effects on vertices*


for a precise definition of [*Simplicial Map*](http://mathworld.wolfram.com/SimplicialMap.html) look at [*Wolfram MathWorld*](http://mathworld.wolfram.com/)


## MAP operator in plasm

### Map operator

```{.python}
MAP(fun)(domain)
```
### Semantics

1.  **domain** (HPC value) is decomposed into a *simplicial complex*
2.	**fun** (a simplicial function) is applied to the *domain vertices*
3.	the *mapped domain* is returned



## MAP examples: 1-sphere ($S^1$) and 2-disk ($D^2$)

\scriptsize

```{.python}
def sphere1(p): return [COS(p[0]), SIN(p[0])] # point function
def domain(n): return INTERVALS(2*PI)(n)	  # generator of domain decomp
VIEW( MAP(sphere1)(domain(32)) )		  	  # geometric value (HPC type)

def disk2D(p): 											# point function
	u,v = p
	return [v*COS(u), v*SIN(u)] 						# coordinate functions
domain2D = PROD([INTERVALS(2*PI)(32), INTERVALS(1)(3)])	# 2D domain decompos
VIEW( MAP(disk2D)(domain2D) )
VIEW( SKELETON(1)(MAP(disk2D)(domain2D)) )
```

\begin{figure}[htbp] %  figure placement: here, top, bottom, or page
	\includegraphics[height=0.25\linewidth,width=0.25\linewidth]{images/circle3} 
	\includegraphics[height=0.25\linewidth,width=0.25\linewidth]{images/circle4} 
	\includegraphics[height=0.25\linewidth,width=0.25\linewidth]{images/circle5} 
   \caption{(a) sphere $S^1$ (b) disk $D^2$; (c)~1-skeleton.}
   \label{fig:circle}
\end{figure}





