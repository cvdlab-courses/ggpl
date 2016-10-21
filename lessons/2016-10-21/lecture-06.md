% Geometric \& Graphics Programming Lab: Lecture 6
% Alberto Paoluzzi
% \today

\tableofcontents

# Workshop N.2 

## Parametric (spatial) building frame in reinforced concrete


![](images/sketch.pdf "sketch")


##  Look at some examples

*	[_Strutture in cemento armato_](https://www.google.it/search?q=strutture+in+cemento+armato&client=safari&rls=en&source=lnms&tbm=isch&sa=X&ved=0ahUKEwisvcT59urPAhWEiRoKHY4gAOYQ_AUICCgB&biw=1031&bih=812#imgrc=_)

*	[_Reinforced concrete structures_](https://www.google.it/search?q=reinforced+concrete+structures&rlz=1C5CHFA_enIT703IT707&espv=2&biw=1204&bih=862&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi6sqrB-erPAhVHchQKHXX3BUsQ_AUIBigB#imgdii=bUBBkzphNwcgtM%3A%3BbUBBkzphNwcgtM%3A%3BThMxdl1D95nUvM%3A&imgrc=bUBBkzphNwcgtM%3A)

!

## Requirements (1/2)

*	Define a single Python function, named **`ggpl_bone_structure`**, with a single input parameter **`file_name`**.

*	The function must return a _3D value_ of **type HPC** (the geometric type of the `pyplasm` library), representing the bone structure of a (parametric) reinforced concrete building.

*	The function must read a _comma separated value file_ (suffix `.csv`), named **`frame_data_xxxxxx.csv`**, where _`xxxxxx`_ is the student's ID code.

## Requirements (2/2)

*	The `frame_data_xxxxxx.csv` file must include on **odd lines**:

	-	the	3D vector positioning the local origin of the next frame with respect to the local origin of the the previous one.  
	
	-	The first such vector sets the origin of the first frame w.r.t. the basis of the whole building. 

*	The `frame_data_xxxxxx.csv` file must include on **even lines**:

	-	the actual parameters of a planar concrete frame, according to the scheme of formal parameters required by  the _ggpl_ function developed in [_workshop n.1_](../2016-10/14/lecture-04.md) by the student itself.


## Hints to solution


*	Once read the data file and assembled the _`STRUCT`_ of planar frames, create the _connecting beams_ using the _`QUOTE`_ primitive

*	Provide **only orthogonal connections**. Every pillar _must have_ either 2 or 3 beams 
incident on it.

*	Use `pyplasm` primitives **`QUOTE`** (to produce _1D cell complexes_) and **`PROD`** for _Cartesian product_ of cell complexes (**HPC** values)



## Style specs (1/2)

*	produce a **notebook** file, of type `.ipynb`
	(The ipynb file extension is associated with the [_IPython notebook_](https://ipython.org/ipython-doc/1/interactive/notebook.html) and/or [**Jupiter**](http://jupyter.org), a rich architecture for interactive computing written in Python and available for various platforms.)


## Style specs (1/2)

*	produce a _single_ Python function, with ONE parameter of `str` type
*	output: a single *HPC* value
*	use **meaningfull** _identificators_ (variables and parameters)
*	use _camelCase_ ids
*	add **Python `docstrings`** (google for it)
*	produce a **single** notebook file, named *workshop_02.ipynb*
*	file path:  _`your_repo/2016-10-14/workshop_02.py`_



# Jupyter notebook required

[**http://jupyter.org**](http://jupyter.org)


## Notebook tutorial


[Notebook Basics](http://nbviewer.jupyter.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/Notebook%20Basics.ipynb)




# Minimal git/github instructions

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

