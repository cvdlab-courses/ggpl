% Geometric and Graphics Programming Laboratory: workshop 1
% Alberto Paoluzzi 
% \today

## Outline: workshop 1

\tableofcontents

#	From PLaSM classic to Pyplasm

<!-- ------------------------------------------------------------- -->
##	Syntactical diffs  (1/2)
<!-- ------------------------------------------------------------- -->
    
    
\columnsbegin
\column{.5\textwidth}

_PLaSM classic (FL)_

*	List 

	```{.python}
	<a,b,c,d>
	```

*	Application operator 

	```{.python}
	fun : args
	```

*	Composition operator 

	```{.python}
	f ~ g
	```

*	Construction operator 

	```{.python}
	[f,g,h]:x == <f:x,g:x,h:x>
	```

\column{.5\textwidth}

__pyplasm (Python)__

*	List (array)

	```{.python}
	[a,b,c,d]
	```

*	Application operator

	```{.python}
	fun(args)
	```

*	Composition operator 

	```{.python}
	COMP([f,g]) 
	```

*	Construction operator 

	```{.python}
	CONS([f,g,h])(x) == 
		[f(x),g(x),h(x)]
```

\columnsend

    
<!-- ------------------------------------------------------------- -->
##	Syntactical diffs  (2/2)
<!-- ------------------------------------------------------------- -->
    
### PLaSM classic (FL)  
    

```{.python}

DEF name (arg::pred)(a1,a2::pred) = expr
WHERE
	local1 = expr1,
	local2 = expr2
END
```

\vfill

### pyplasm (Python)

```{.python}
def name(arg):
	local1 = expr1
	local2 = expr2
	def name1(a1,a2):
		return expr
	return name1
```


<!-- ------------------------------------------------------------- -->
##	Workshop assignment
<!-- ------------------------------------------------------------- -->
    
Convert some Classic PlASM scripts from Chapter 1 and/or Chapter 2
of book [*Geometric Programming for Computer-Aided Design*](http://onlinelibrary.wiley.com/book/10.1002/0470013885) (GP4CAD)

\vfill

Free choice of number and type of scripts to Convert
 
 
 

<!-- ------------------------------------------------------------- -->
## Style specs (1/2)
<!-- ------------------------------------------------------------- -->

*	produce a **notebook** file, of type _`.ipynb`_
	(The ipynb file extension is associated with the [_IPython notebook_](https://ipython.org/ipython-doc/1/interactive/notebook.html) and/or [**Jupiter**](http://jupyter.org), a rich architecture for interactive computing written in Python and available for various platforms.)

\vfill

*	alternate notebook cells with

	*	Title and description (markdown)
	*	PLaSM classic code (markdown teletype)
	*	Python code
	*	Image from execution (markdown)

<!-- ------------------------------------------------------------- -->
## Style specs (1/2)
<!-- ------------------------------------------------------------- -->

*	standard output: a single *HPC* value

*	use **meaningfull** _identificators_ (variables and parameters)

*	use _camelCase_ ids

*	add **Python _`docstrings`_** (google for it)

*	produce a **single** notebook file, named *workshop_01.ipynb*

*	file path:  _`your_repos/ggpl/2017-10-23/workshop_01.ipynb`_



# Jupyter notebook required

[**http://jupyter.org**](http://jupyter.org)


<!-- ------------------------------------------------------------- -->
## Notebook tutorial
<!-- ------------------------------------------------------------- -->


[_Notebook Basics_](http://nbviewer.jupyter.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/Notebook%20Basics.ipynb)




# Minimal git/github instructions

<!-- ------------------------------------------------------------- -->
## Minimal git/github instructions  (1/2)
<!-- ------------------------------------------------------------- -->

create your local repository

```
$ mkdir development
$ cd development
$ git clone https://github.com/your-account/ggpl
$ cd ggpl
$ mkdir 2017-10-23
$ cd 2017-10-23
$ touch workshop_01.ipynb
```


<!-- ------------------------------------------------------------- -->
## Minimal git/github instructions  (2/2)
<!-- ------------------------------------------------------------- -->

commit your work

```
$ cd ..  # move to ggpl/
$ git add -A .
$ git commit -m "add a short note to commit"
$ git push origin master
```



<!-- ------------------------------------------------------------- -->
##	References
<!-- ------------------------------------------------------------- -->
    




<!-- 
##	Graphics slide

![*Some examples*](../examples.pdf "examples"){#id .class width=100%}


##	Julia code slide


```{.julia}

```


##	Multicolumn slide

\columnsbegin
\column{.5\textwidth}

aaaa

\column{.5\textwidth}

![*Some examples*](../examples.pdf "examples"){#id .class width=100%}

\columnsend


## Citation

[@ClementiSSPP-CAD16]
 -->

