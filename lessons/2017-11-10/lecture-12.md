% Geometric and Graphics Programming Laboratory: Lecture 12
% Alberto Paoluzzi
% \today

## Outline: LAR3 [@Dicarlo:2014:TNL:2543138.2543294]

\tableofcontents

# LAR-CC library


## download from github

```
$ git clone https@github.com:cvdlab/lar-cc.git 
```
\pause

In your python files:

```{.python}
""" import modules from larlib """
from larlib import *
```
# LAR representation

## Input of a simplicial complex  (brc2csr)

\framesubtitle{From BRC (Binary Row Compressed) to CSR (Compressed Sparse Row)}

\footnotesize

*	LAR model: (V,FV,EV)

```{.python}
V = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1]]
FV = [[0, 1, 3], [1, 2, 4], [1, 3, 4], [2, 4, 5]]
EV = [[0,1],[0,3],[1,2],[1,3],[1,4],[2,4],[2,5],[3,4],[4,5]]

VIEW(STRUCT(MKPOLS((V,FV)))); VIEW(EXPLODE(1.2,1.2,1)(MKPOLS((V,FV))))
VIEW(STRUCT(MKPOLS((V,EV)))); VIEW(EXPLODE(1.2,1.2,1)(MKPOLS((V,EV))))
```

*	Lar representation: (CSR matrix)

```{.python}
csrFV = csrCreate(FV)
csrEV = csrCreate(EV)

print "\ncsrCreate(FV) =\n", csrFV
print "\n>>> csr2DenseMatrix"
print "\nFV =\n", csr2DenseMatrix(csrFV)
print "\nEV =\n", csr2DenseMatrix(csrEV)
```

## Input of a simplicial complex  (brc2csr)

\footnotesize

\begin{columns}
\begin{column}{0.5\textwidth}
   \centering
   \includegraphics[width=0.5\linewidth]{../images/_text1} 
\end{column}

\begin{column}{0.5\textwidth}
   \centering
   \includegraphics[width=0.35\linewidth]{../images/_text2} 
\end{column}
\end{columns}

   \centering
   \includegraphics[height=0.25\linewidth,width=0.5\linewidth]{../images/4triangle1} 
   \includegraphics[height=0.25\linewidth,width=0.5\linewidth]{../images/4triangle2} 

# Facet extraction

## Facet extraction from simplices

\framesubtitle{combinatorial approach}

\footnotesize

*	A $k$-face of a $d$-simplex is defined as the convex hull of any subset of $k$ vertices.

*	A $(d-1)$-face of a $d$-simplex 
$$
\sigma^d = \langle v_0, v_1, \ldots, v_d \rangle
$$
 is also called a \emph{facet}. 
 
*	Each of the $d+1$ facets of $\sigma^d$, obtained by removing a vertex from $\sigma^d$, is a $(d-1)$-simplex. 
 
*	A simplex may be oriented in two different ways according to the permutation
class of its vertices. 

*	The simplex \emph{orientation} is so changed by either multiplying the simplex by -1, or by executing an odd number of exchanges of its vertices. 

## Facet extraction from simplices

\framesubtitle{combinatorial approach}

The **chain** of *oriented boundary facets* of $\sigma^d$, usually denoted as $\partial \sigma^d$, is **generated combinatorially** as follows:
$$
\partial\, \sigma^d = \sum_{k=0}^d (-1)^d \langle v_0, \ldots, v_{k-1}, v_{k+1}, \ldots, v_d \rangle
$$

## Implementation

```{.python}
def larSimplexFacets(simplices):
	''' To return the facets of a list of d-simplices '''
    out = []
    d = len(simplices[0])
    for simplex in simplices:
        out += [simplex[0:k]+simplex[k+1:d] 
        		for k in range(d)]
    out = sorted(out)
    return [facet for k,facet in enumerate(out[:-1]) 
    			if out[k] != out[k+1]] + [out[-1]] 
```

## Test of implementation

```{.python}
>>>larSimplexFacets([[0]])
[[]]
>>>larSimplexFacets([[0,1]])
[[0],[1]]
>>>larSimplexFacets([[0,1,2]])
[[0,1],[0,2],[1,2]]
>>>larSimplexFacets([[0,1,2,3]])
[[0,1,2],[0,1,3],[0,2,3],[1,2,3]]
>>>larSimplexFacets([[0,1,2,3,4]])
[[0,1,2,3],[0,1,2,4],[0,1,3,4],[0,2,3,4],[1,2,3,4]]
```
. . . 

Are such facets **oriented**? 

## Examples of facet extraction from 3D simplicial cube

```{.python}
V,CV = larSimplexGrid1([1,1,1])

VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS((V,CV))))
SK2 = (V,larSimplexFacets(CV))
VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS(SK2)))
SK1 = (V,larSimplexFacets(SK2[1]))
VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS(SK1)))
```

look also at 

```{.python}
V,CV = larSimplexGrid1([5,5,2])
```

## Assignment

Change the *larSimplexFacets* so that the extracted facets are **coherently oriented**


# Boundary computation

## From cells and facets to boundary operator

```{.python}
def boundary(cells,facets):
    csrCV = csrCreate(cells)
    csrFV = csrCreate(facets)
    csrFC = matrixProduct(csrFV, csrTranspose(csrCV))
    facetLengths = [csrCell.getnnz() for csrCell in csrCV]
    return csrBoundaryFilter(csrFC,facetLengths)

def coboundary(cells,facets):
    Boundary = boundary(cells,facets)
    return csrTranspose(Boundary)
```


## Oriented boundary example

\footnotesize

```{.python}
V,CV = larSimplexGrid1([4,4,4])
VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS((V,CV))))

FV = larSimplexFacets(CV)
EV = larSimplexFacets(FV)
VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS((V,FV))))

csrSignedBoundaryMat = signedBoundary (V,CV,FV)
boundaryCells_2 = signedBoundaryCells(V,CV,FV)
def swap(l): return [l[1],l[0],l[2]]
boundaryFV = [FV[-k] if k<0 else swap(FV[k]) for k in boundaryCells_2]
boundary = (V,boundaryFV)
VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS(boundary)))
```


## Oriented boundary example

\begin{figure}
\includegraphics[height=0.333\linewidth,width=0.333\linewidth]{../images/boundarygrid1} 
\includegraphics[height=0.333\linewidth,width=0.333\linewidth]{../images/boundarygrid2} 
\includegraphics[height=0.333\linewidth,width=0.333\linewidth]{../images/boundarygrid3} 
\caption{Simplicial complexes: (a)  3-complex $S_3$; (b)  2-complex $S_2=K_2(S_3)$; 
(c)  2-complex $T_2 = \partial S_3 \subset S_2$)}
\end{figure}


# Extrusion

## Simplicial extrusion

\framesubtitle{Computation}


\begin{figure}[htbp] %  figure placement: here, top, bottom, or page
   \centering
   \includegraphics[width=\textwidth]{../images/simplexextrusion} 
   \caption{example caption}
   \label{fig:example}
\end{figure}


## Simplicial extrusion

\framesubtitle{Computation}

Let us concentrate on the generation of the simplex chain $\gamma^{d+1}$ of dimension $d+1$ produced by combinatorial extrusion of a single simplex 
$$
\sigma^d = \langle v_0, v_1, \ldots, v_d,   \rangle .
$$
Then we have, with $|\gamma^{d+1}| = \sigma^d \times I$, and $I=[0,1]$:
$$
\gamma^{d+1} = \sum_{k=0}^{d} (-1)^{kd} \langle v_k, \ldots v_d, v^*_0, \ldots  v^*_k \rangle 
$$
with $v_k\in \sigma^d \times \{0\}$ and  $v^*_k\in \sigma^d \times \{1\}$, and where the term $(-1)^{kd}$ is used to generate a chain of coherently-oriented extruded simplices.


## Example of simplicial complex extrusion

```{.python}
V = [[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2]]
FV = [[0,1,3],[1,2,4],[2,4,5],[3,4,6],[4,6,7],[5,7,8]]
model = larExtrude1((V,FV),4*[1,2,-3])
VIEW(EXPLODE(1,1,1.2)(MKPOLS(model)))
```

\begin{figure}[htbp] %  figure placement: here, top, bottom, or page
   \centering
   \includegraphics[width=0.7\linewidth]{../images/assembly} 
   \caption{A simplicial complex providing a quite complex 3D assembly of tetrahedra.}
   \label{fig:assembly}
\end{figure}


## Multidimensional simplicial grids

\framesubtitle{The generation of simplicial grids of any dimension and shape is amazingly simple}


The input parameter \texttt{shape} is either a tuple or a list of integers used to specify the \emph{shape} of the created array


```{.python}
VOID = V0,CV0 = [[]],[[0]]    	# the empty simplicial model

def larSimplexGrid1(shape):
    model = VOID
    for item in shape:
        model = larExtrude1(model,item*[1])
    return model
```

The returned  \texttt{model} has integer vertices, to be scaled and/or translated and/or mapped 



# Cartesian product of complexes

## Cartesian product of two LAR models 

\scriptsize

```{.python}
def larModelProduct(twoModels):
    (V, cells1), (W, cells2) = twoModels
    @< Cartesian product of vertices @>
    @< Topological product of cells    @>
    model = [list(v) for v in vertices.keys()], cells
    return model
```
. . . 

### Cartesian product of vertices  

```{.python}
vertices = collections.OrderedDict(); k = 0
for v in V:
    for w in W:
        id = tuple(v+w)
        if not vertices.has_key(id):
            vertices[id] = k
            k += 1	@}
```

. . . 

### Topological product of cells    

```{.python}
cells = [ [vertices[tuple(V[v] + W[w])] for v in c1 for w in c2]
         for c1 in cells1 for c2 in cells2]	@}
```


## Cuboidal grids

```{.python}
VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS(larCuboids([3,2,1]))))
```

\begin{figure}[htbp] %  figure placement: here, top, bottom, or page
   \centering
   \includegraphics[height=0.245\linewidth,width=0.242\linewidth]{../images/skel0} 
   \includegraphics[height=0.245\linewidth,width=0.242\linewidth]{../images/skel1} 
   \includegraphics[height=0.245\linewidth,width=0.242\linewidth]{../images/skel2} 
   \includegraphics[height=0.245\linewidth,width=0.242\linewidth]{../images/skel3} 
   \caption{Exploded views of 0-, 1-, 2-, and 3-dimensional skeletons.}
   \label{fig:grid23D}
\end{figure}



## Cuboidal grids

```{.python}
VIEW(EXPLODE(1.5,1.5,1.5)(MKPOLS(larCuboids([3,2,1]))))
```

\begin{figure}[htbp] %  figure placement: here, top, bottom, or page
   \centering
   \includegraphics[height=0.28\linewidth,width=0.5\linewidth]{../images/cuboids1} 
   \includegraphics[height=0.28\linewidth,width=0.5\linewidth]{../images/cuboids2} 
   \caption{Exploded views of 0-, 1-, 2-, and 3-dimensional skeletons.}
   \label{fig:grid23D}
\end{figure}



# Skeletons

## Cuboidal skeletons


\footnotesize

A list of \texttt{BRC} characteristic matrices of cellular $k$-complexes ($0\leq k\leq d$) with dimension $d$, where $d={}$\texttt{len(shape)}, is returned by the function \texttt{gridSkeletons} in the macro below, where the input is given by the \emph{shape} of the grid, i.e. by the list of cell items in each coordinate direction. 


```{.python}
def gridSkeletons(shape):
	gridMap = larGridSkeleton(shape)
	skeletonIds = range(len(shape)+1)
	skeletons = [ gridMap(id) for id in skeletonIds ]
	return skeletons
```

## Cuboidal skeletons

\framesubtitle{Just notice that the number of returned $d$-cells is equal to \texttt{PROD(shape)}}

```{.python}
print "\ngridSkeletons([3]) =\n", gridSkeletons([3])
print "\ngridSkeletons([3,2]) =\n", gridSkeletons([3,2])
print "\ngridSkeletons([3,2,1]) =\n", gridSkeletons([3,2,1])
```


## Generation of grid boundary complex

```{.python}
def gridBoundaryMatrices(shape):
	skeletons = gridSkeletons(shape)
	boundaryMatrices = [boundary(skeletons[k+1],faces) 
						 for k,faces in enumerate(skeletons[:-1])]
	return boundaryMatrices
	
for k in range(1):
	print "\ngridBoundaryMatrices([3]) =\n", \
			csr2DenseMatrix(gridBoundaryMatrices([3])[k])
for k in range(2):
	print "\ngridBoundaryMatrices([3,2]) =\n", \
			csr2DenseMatrix(gridBoundaryMatrices([3,2])[k])
for k in range(3):
	print "\ngridBoundaryMatrices([3,2,1]) =\n", \
			csr2DenseMatrix(gridBoundaryMatrices([3,2,1])[k])
```








# References

## References

