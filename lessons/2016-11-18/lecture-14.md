% Geometric \& Graphics Programming Lab: Lecture 14
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




# Linear Algebraic Representation (LAR)


## LAR: Mathematical models


Space of CW-complexes  (cellular complexes)


## Chain complex (of chain spaces)

  \framesubtitle{Sequence of linear spaces (over $\Z_2$) of $d$-cell {\bf subsets}}

A \alert{chain} \emph{complex} $C$ is a complex of \emph{chain spaces} and  \emph{boundary maps}:

\footnotesize
\emph{Unit $d$-chains} (single $d$-cell subsets), give the \alert{standard bases} ($M_d$ rows) of \emph{$d$-chain spaces}  


\begin{center}
   \includegraphics[width=0.7\linewidth]{figs/matrices} 
\end{center}
\vspace{-10mm}
\begin{center}
	~\hfill
   \includegraphics[width=0.2\linewidth]{figs/Tshape3} 
   \includegraphics[width=0.2\linewidth]{figs/Tshape2} 
   \includegraphics[width=0.2\linewidth]{figs/Tshape1} 
   \includegraphics[width=0.2\linewidth]{figs/Tshape0} 
   \hfill~
\end{center}


## Characteristic matrices of $d$-chain spaces

  \framesubtitle{Matrix representation of the basis --- {\bf $d$-cells as subsets of vertices} }

   \centering
   \includegraphics[width=\textwidth]{figs/char_matrix} 


<!-- 

## CW-complex  (Cellular complex)


*	Roughly speaking, a [*CW-complex*](http://www.math.ksu.edu/~hansen/CWcomplexes.pdf) is made of *basic building blocks* called **cells**. 
*	The C stands for *closure-finite*, and the W for [*weak topology*](https://www.princeton.edu/~achaney/tmve/wiki100k/docs/Weak_topology.html).
*	**Closure-finite** means that *each closed cell* is covered by a **finite union** of *open cells*.


#.	An $n$-dimensional closed cell is the image of an $n$-disk under an attaching map. 
#.	*A simplex is a closed cell*, and more generally, **a convex polytope is a closed cell**. 
#.	An $n$-dimensional open cell is a topological space that is homeomorphic to the open disk. 
#.	A 0-dimensional open (and closed) cell is a *singleton* space. 



##	CW-complex: inductive definition

\footnotesize

Let $X$ be a [*topological space*](http://mathworld.wolfram.com/TopologicalSpace.html).

Let $\Lambda (X) = \cup_p X_{p\in\N}$ be a [*partition*](http://en.wikipedia.org/wiki/Partition_of_a_set) of $X$, with $X_p$ the set of $p$-cells.

. . .

\begin{definition}[\alert{CW-structure}]
A \emph{CW-structure} on the space $X$ is a \href{http://en.wikipedia.org/wiki/Filtration_(mathematics)}{\emph{filtration}} 
(a family of subsets) s.t.
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


## Politopal, simplicial, cuboidal complexes


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

 -->

<!-- 
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

 -->



# LAR: computer representation



## Sparse matrix representations

\framesubtitle{Basic representations}


A few basic representation of topology are used in LARCC. 

They include some common sparse matrix representations: 

\begin{itemize}
\item 
CSR (Compressed Sparse Row), 
\item 
CSC (Compressed Sparse Column), 
\item 
COO (Coordinate Representation), 
\item 
and BRC (Binary Row Compressed)
\end{itemize}



## Data definition

\footnotesize

*	We can **identify each cell** with its **set of vertices**. 

*	Thus, to define $S$, we *start from the vertex set* $V$, and *specify the vertex subsets* which correspond to the **cells**, and the *rank* of each cell. 

*	The *partial order* is induced by *set inclusion*.


\vfill

### **Characteristic matrix $M_2: C_0 \to C_2$ **


$$
M_2 = \mat{
1 & 0 & 1 & 0 & 1 & 0 & 1\\
0 & 1 & 0 & 0 & 1 & 1 & 1\\
0 & 1 & 0 & 1 & 1 & 0 & 0\\
0 & 0 & 1 & 0 & 0 & 1 & 1}
\qquad\qquad
\begin{minipage}[c]{3cm}
\includegraphics[width=\linewidth]{figs/brc2} 
\end{minipage}
$$


## BRC (Binary Row Compressed) representation
\framesubtitle{List of list of integer \hfill typically used for input of cell complexes}


### Let $A = (a_{i,j} \in \{0,1\})$ be a characteristic matrix. 

   \centering
   \includegraphics[width=0.8\linewidth]{figs/brc} 




## The idea: \hfill generalisation of abstract simplicial sets
\vspace{-5mm}
$$
\begin{minipage}[c]{7cm}
\includegraphics[width=\linewidth]{figs/brc2} 
\end{minipage}
~~~~~~~~~
\begin{minipage}[c]{3cm}
\flushleft\Large
$n$-cells by their vertices:\\[5mm]
\tt
[[0,2,4,6], 
~[1,4,5,6], 
~[1,5,6], 
~[2,5,6]]
\end{minipage}
$$



##
\includegraphics[width=\linewidth]{figs/2Dpolytopes0} 


## The bare minimum data \hfill\scriptsize{with full awareness of topology}

\includegraphics[width=0.5\linewidth]{figs/2Dpolytopes1} 
\includegraphics[width=0.5\linewidth]{figs/2Dpolytopes2} 

\scriptsize\tt

V=[[5,0],[7,1],[9,0],[13,2],[15,4],[17,8],[14,9],[13,10],[11,11],[9,10],[5,9],[7,
9],[3,8],[0,6],[2,3],[2,1],[8,3],[10,2],[13,4],[14,6],[13,7],[12,10],[11,9],[9,7],
[7,7],[4,7],[2,6],[3,5],[4,2],[6,3],[11,4],[12,6],[12,7],[10,5],[8,5],[7,6],[5,5]]

FV = [[0,1,16,28,29],[0,15,28],[1,2,17],[1,16,17,33],[2,3,17],[3,4,18,19],[3,17,
18,30],[4,5,19],[5,6,19],[6,7,20,21,22,32],[6,19,20],[7,8,21],[8,9,21,22],[9,11,
23,24],[9,22,23],[10,11,24,25],[10,12,25],[12,13,25,26],[13,14,27],[13,26,27],
[14,15,28],[14,27,28,29,36],[16,29,34],[16,33,34],[17,30,33],[18,19,31],[18,30,
31],[19,20,31,32],[22,23,32,33],[23,24,34,35],[23,33,34],[24,25,27,36],[24,35,36],
[25,26,27],[29,34,35],[29,35,36],[30,31,32,33]]



## Compressed Sparse Row (CSR) matrix storage
\centering

\includegraphics[width=\linewidth]{figs/csr} 


image from

\includegraphics[width=0.7\linewidth]{figs/williams} 




## CSR storage of a \emph{BINARY} matrix
\centering

\includegraphics[width=\linewidth]{figs/csr-binary} 

of course, \emph{non-zero values (all ones)} do not require storage





## CSR storage of a \emph{binary} matrix $M_d$ \emph{such that}
$$
M_d\, {\bf 1} = {\bf k}
$$

\includegraphics[width=\linewidth]{figs/csr-compressed} 

\vfill\pause

important cases:
\begin{itemize}
\item regular \alert{simplicial} $d$-complexes: $k = d+1$
\item regular \alert{cuboidal} $d$-complexes: $k = 2^d$
\end{itemize}



# Operations




## Facet extraction (1/5)

\framesubtitle{use the \emph{characteristic matrix} $M_d$ of a \emph{cellular partition} $\Lambda_d$ of $\E^d$, empty cells included}

\includegraphics[width=\linewidth]{figs/facets1}



## Facet extraction (2/5)

\framesubtitle{use the \emph{characteristic matrix} $M_d$ of a \emph{cellular partition} $\Lambda_d$ of $\E^d$, empty cells included}

\includegraphics[width=\linewidth]{figs/facets0}



## Facet extraction (3/5)

\framesubtitle{use the \emph{characteristic matrix} $M_d$ of a \emph{cellular partition} $\Lambda_d$ of $\E^d$, empty cells included}

\includegraphics[width=\linewidth]{figs/facets2}



## Facet extraction (4/5)

\framesubtitle{use the \emph{characteristic matrix} $M_d$ of a \emph{cellular partition} $\Lambda_d$ of $\E^d$, empty cells included}

\includegraphics[width=\linewidth]{figs/facets3}



## Facet extraction (5/5)

\framesubtitle{use the \emph{characteristic matrix} $M_d$ of a \emph{cellular partition} $\Lambda_d$ of $\E^d$, empty cells included}

\includegraphics[width=\linewidth]{figs/facets4}




## Simplicial extrusion (1/3)

\framesubtitle{Optimal combinatorial algorithm \hfill [Ferrucci \& Paoluzzi, CAD, 1991]}

\footnotesize

for each d-simplex 
$$
\sigma^d = (v_0,v_1,\ldots,v_d)
$$ 
in the input complex $S(d)$, we generate combinatorially a chain of $d+1$ *coherently-oriented* simplexes of dimension $d+1$:

\vfill

\begin{minipage}[c]{\linewidth}
\begin{framed}
	\begin{minipage}[c]{3.3cm}
	\includegraphics[width=\linewidth]{figs/extr0}
	\end{minipage}
	\hfill
	\begin{minipage}[c]{3.3cm}
	\includegraphics[width=\linewidth]{figs/extr1}
	\end{minipage}
	\hfill
	\begin{minipage}[c]{3.3cm}
	\includegraphics[width=\linewidth]{figs/extr2}
	\end{minipage}
\end{framed}
\end{minipage}

\vfill

So we have, with $|\gamma^{d+1}| = \sigma^d \times I$, and $I=[0,1]$:
$$
\gamma^{d+1} = \sum_{k=0}^{d} (-1)^{kd} \langle v_k, \ldots v_d, v^*_0, \ldots  v^*_k \rangle 
$$
with $v_k\in \sigma^d \times \{0\}$ and  $v^*_k\in \sigma^d \times \{1\}$,  




## Simplicial extrusion (2/3)

Let $\mathfrak{S}$ be the set of simplicial c.c.c., and $S_d, S_1 \in \mathfrak{S}$:
$$
S_d \times S_1 =: S_{d+1} \in \mathfrak{S}
$$

   \centering
   \includegraphics[height=0.33\linewidth,width=0.33\linewidth]{figs/simplices1} 
   \includegraphics[height=0.33\linewidth,width=0.33\linewidth]{figs/simplices2} 
   \includegraphics[height=0.33\linewidth,width=0.33\linewidth]{figs/simplices3} 

```{.python}
model1 = larExtrude( VOID, 10*[1] ) 
model2 = larExtrude( model1, 10*[1] ) 
model3 = larExtrude( model2, 10*[1] )
```



## Simplicial extrusion (3/3)

   \centering
   \includegraphics[width=\linewidth]{figs/helicoid} 





## Cartesian product of complexes (1/4)

\framesubtitle{Let $\mathfrak{C}$ be the set of c.c.c’s.  \hfill
$X,Y \in \mathfrak{C} \Rightarrow X\times Y \in \mathfrak{C}$ 
\hfill [Basak, Geom.~dedicata, 2010]}

Let
$$
X = S(m)  \in \mathfrak{S},\quad\mbox{and}\quad Y = S(n) \in \mathfrak{S};
$$
Then
$$
X\times Y = S(X\times Y) \in \mathfrak{S}
$$
with
$$
x\times y = (x_1y_1,\ldots,x_1y_n, \ldots,   x_my_1,\ldots,x_my_n) \in S(m+n).
$$


## Cartesian product of complexes (2/4)

\framesubtitle{Implementation} \footnotesize

```{.python}
def larModelProduct(twoModels):
    (V, cells1), (W, cells2) = twoModels
    vertices = collections.OrderedDict(); k = 0
    for v in V:
        for w in W:
            id = tuple(v+w)
            if not vertices.has_key(id):
                vertices[id] = k
                k += 1   
    cells = [ [vertices[tuple(V[v] + W[w])] for v in c1 for w in c2 ]
             for c1 in cells1 for c2 in cells2]  
    model = [list(v) for v in vertices.keys()], cells
    return model
```




## Cartesian product of complexes (4/4)


\begin{minipage}[c]{\linewidth}
	\begin{minipage}[c]{0.32\linewidth}
	\centering
	\includegraphics[width=0.8\linewidth]{figs/larproduct1}
	\end{minipage}
	\hfill
	\begin{minipage}[c]{0.32\linewidth}
	\centering
	\includegraphics[width=0.8\linewidth]{figs/larproduct2}
	\end{minipage}
	\hfill
	\begin{minipage}[c]{0.32\linewidth}
	\centering
	\includegraphics[width=0.8\linewidth]{figs/larproduct3}
	\end{minipage}
\end{minipage}

\vfill

\begin{minipage}[c]{\linewidth}
	\begin{minipage}[c]{0.32\linewidth}
	\centering
	\includegraphics[width=0.8\linewidth]{figs/larproduct4}
	\end{minipage}
	\hfill
	\begin{minipage}[c]{0.32\linewidth}
	\centering
	\includegraphics[width=0.8\linewidth]{figs/larproduct5}
	\end{minipage}
	\hfill
	\begin{minipage}[c]{0.32\linewidth}
	\centering
	\includegraphics[width=0.8\linewidth]{figs/larproduct6}
	\end{minipage}
\end{minipage}

\vfill

\begin{minipage}[c]{\linewidth}
	\begin{minipage}[c]{0.32\linewidth}
	\centering
	\includegraphics[width=0.8\linewidth]{figs/larproduct7}
	\end{minipage}
	\hfill
	\begin{minipage}[c]{0.32\linewidth}
	\centering
	\includegraphics[width=0.8\linewidth]{figs/larproduct8}
	\end{minipage}
	\hfill
	\begin{minipage}[c]{0.32\linewidth}
	\centering
	\includegraphics[width=0.8\linewidth]{figs/larproduct9}
	\end{minipage}
\end{minipage}


##  `Larlib` Examples ()

\footnotesize

```{.python}
from larlib import *

V = [[0,0],[4,0],[6,0],[8,0],[10,0],[15,0],[17,0],[0,7],[4,7],[6,7],[8,7],[10,7],
[15,7],[17,7],[17,4],[17,3],[4,4],[6,4],[8,4],[10,4],[15,4],[4,3],[6,3],[8,3],
[10,3],[15,3]]

FV = [[0,1,7,8,16,21],[1,2,21,22],[2,3,22,23],[3,4,23,24],[4,5,24,25],[5, 6,25,15],
[8,9,16,17],[9,10,17,18],[10,11,18,19],[11,12,19,20],[12,13,14,20],range(14,26),
range(7),range(7,14),[0,7],[6,13,14,15]]
```


##  `Larlib` Examples (1/8)

\footnotesize

```{.python}
submodel = SKEL_1(STRUCT(MKPOLS((V,FV))))
V,EV = larFacets((V,FV),2,4)
VV = AA(LIST)(range(len(V)))
VIEW(larModelNumbering(1,1,1)(V,[VV,EV,FV[:-4]],submodel,3))
```

![](images/larlib1.pdf "larlib")

##  `Larlib` Examples (2/8)

\footnotesize

```{.python}
VIEW(EXPLODE(1.2,1.2,1.2)(MKPOLS((V,FV[:-4]))+MKPOLS((V,EV))+AA(MK)(V)))
```

![](images/larlib2.pdf "larlib")


##  `Larlib` Examples (3/8)

\footnotesize

```{.python}
BE = boundaryCells(FV[:-4],EV)
VIEW(EXPLODE(1.2,1.2,1)(MKPOLS((V,[EV[e] for e in BE]))))
```

![](images/larlib3.pdf "larlib")


##  `Larlib` Examples (4/8)

\footnotesize

```{.python}
C1 = larCuboids([10])
V3,CV = larModelProduct([(V,FV[:-4]),C1])
VIEW(EXPLODE(1.2,1.2,1.2)(MKPOLS((V3,CV))))
```

![](images/larlib4.pdf "larlib")


##  `Larlib` Examples (5/8)

\footnotesize

```{.python}
full3D = CV + exteriorCells((V3,CV))
V3,FV3 = larFacets((V3,full3D),3,6)
VIEW(EXPLODE(1.2,1.2,1.2)(MKPOLS((V3,FV3))))
```

![](images/larlib5.pdf "larlib")


##  `Larlib` Examples (6/8)

\footnotesize

```{.python}
V3,EV3 = larFacets((V3,FV3),2)
VIEW(EXPLODE(1.2,1.2,1.2)(MKPOLS((V3,EV3))))
```

![](images/larlib6.pdf "larlib")


##  `Larlib` Examples (7/8)

\footnotesize

```{.python}
VV3 = AA(LIST)(range(len(V3)))
boundary3D = boundaryCells(CV,FV3)
VIEW(EXPLODE(1.25,1.25,1.25)(MKPOLS((V3,[FV3[f] for f in boundary3D]))))
```

![](images/larlib7.pdf "larlib")


##  `Larlib` Examples (8/8)

\footnotesize

```{.python}
V3,F3 = larFacets((V3,CV))
VIEW(EXPLODE(1.2,1.2,1.2)(MKPOLS((V3,F3))))
```

![](images/larlib8.pdf "larlib")
