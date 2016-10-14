% Geometric \& Graphics Programming Lab: Lecture 4
% Alberto Paoluzzi
% \today

\tableofcontents

# Workshop N.1


##  Simple parametric building structure in reinforced concrete


*	Space frame of reinforced concrete
*	including beams, pillars and footings
*	using few `pyplasm` primitive operations
*	parameterized by:
	+	`(bx,bz)`  (given dimensions of beam section) 
	+	`(px,py)`	(given dimensions of pillar section)
	+	`[dy1,dy2,...]`   (distances between axes of the pillars)
	+	`[hz1,hz2,...]`	(interstory heights)



## Sketch of object shape


![](fig_01.pdf "test")


## Hint: solution 1

Use `pyplasm` primitives `QUOTE` (to produce _1D cell complexes_) and `PROD` for _Cartesian product_ of cell complexes (**HPC** values)

```python
x = [.1,-.05,.001,-.05]
a = QUOTE(x*5)
aa = PROD([a,a])
aaa = PROD([aa,a])
VIEW(aaa)
```


## Hint: solution 2

Use `pyplasm` primitives `CUBOID` (to produce 3D cuboidal cells), `T()()` for translations, and `STRUCT` (for assembly of cell complexes) to create _structures_ of **HPC** values

```python
b = CUBOID([1,2,3])
d = STRUCT([b,T(1)(4.0),b])
VIEW(d)
```


## Style specs

*	produce a _single_ Python function, with real or integer or list parameters
*	output: a single *HPC* value
*	use **meaningfull** _identificators_ (variables and parameters)
*	use _camelCase_ ids
*	add **Python `docstrings`** (google for it)
*	produce a single Python file, named *workshop_01.py*
*	file path:  _`your_repo/2016-10-14/workshop_01.py`_


## Minimal git/github instructions  (1/2)

create your local repository

```
$ mkdir development
$ cd development
$ git clone https://github.com/your-account/ggpl
$ cd ggpl
$ mkdir 2016-10-14
$ cd 2016-10-14
$ touch workshop_01.py
```


## Minimal git/github instructions  (2/2)

commit your work

```
$ git add -A .
$ git commit -m "add a short note to commit"
$ git push origin master
```

look to your GitHub repository and check


## Assignment for next Friday

1.	Install [_Jupyter_](http://jupyter.readthedocs.io/en/latest/)

2. 	see tutorial

3.	play with it
