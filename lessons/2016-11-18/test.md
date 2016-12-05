% Test
%
%

\tableofcontents

# Mathematical models

## Combinatorial Cell Complexes (1/3)



# Computer representations



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


