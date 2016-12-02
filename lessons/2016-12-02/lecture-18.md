% Geometric \& Graphics Programming Lab: Lecture 18
% Alberto Paoluzzi
% \today

\tableofcontents

# Workshop N.8 



## Solid models from .SVG drawings

The goal of this workshop is to quickly produce a solid model of a house 
starting from an image of its plan drawing.

\vfill

### Summary of steps

*	get an image of the architectural plan
*	produce the 1D wireframe of main building subsystems
*	transform the  SVG files into bunches of lines 
*	apply `pyplasm` transformations to lines to get 3D parts
*	apply colors and/or textures to model parts





## Dowload the `inkshape` drawing tool 
\framesubtitle{It's free and open source}

Inkscape is a professional vector graphics editor for Windows, Mac OS X and Linux. 


*	Flexible drawing tools
*	Broad file format compatibility
*	Powerful text tool
*	Bezier and spiro curves

\vfill

### DOWNLOAD

[InkScape](https://inkscape.org/en/)




## Choose a house (or apartment) image to model

Find a nice and fair architectural plan

![[*Images from Google*](https://www.google.it/search?q=architectural+drawings&rlz=1C5CHFA_enIT703IT707&espv=2&biw=1406&bih=755&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjNxL_D2tTQAhXICsAKHckEBJAQ_AUIBigB#tbm=isch&q=architectural+drawings+floor+plans)](figure-1.pdf "drawings.pdf")  


## Import the image in `InkShape`

*	_Freeze_ the image of the choosen architectural plan

*	Consider the main building subsystems:
	
	-	external enclosures
	-	internal partitions
	-	floor 
	
*	produce a simplified 2D cellular complex (wire frame drawing) using different colors

*	select and export the subsystems in different `.SVG` files

*	save the various produced `.SVG` files in your repository


## Transform your partial SVG drawing in a bunch of lines


*	Use **Chrome** 

*	Use the web service [_http://cvdlab.github.io/svg2lines/_](http://cvdlab.github.io/svg2lines/)

*	save the various produced _`.LINES` files_ in **your repository**

## Use `lines2lar`

*	Start your `ipython` _interactive session_ in your _`2016-12-02` repository_

*	import **`pyplasm`**

*	from each file read a _list of pairs_ of **2D points**


## Transform in 2D and/or 3D solids via PLaSM

*	Give 2D *solid shape* via proper _`OFFSET`_ primitive

*	Transform in 3D **solid parts** via product times a 1D interval



## Open doors and windows via proper subtractions

*	Invent some trick to open _doors_ and _windows_

* 	**Repeat** until necessary for the various subsystems

*	Apply _colors_ and/or _textures_

\vfill

### look in _pyplasm sources_ 

for _`fenvs.py`_ file and find the appropriate syntax


## Put all together and see ... :o)

\LARGE\centering

ENJOY !!


![[*Images from Google*](https://www.google.it/search?q=architectural+drawings&rlz=1C5CHFA_enIT703IT707&espv=2&biw=1406&bih=755&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjNxL_D2tTQAhXICsAKHckEBJAQ_AUIBigB#tbm=isch&q=architectural+drawings+of+houses+3d)](figure-2.pdf "drawings.pdf")  



## REQUIREMENTS

\footnotesize

*	Write a single notebook,  named *`workshop_08.ipynb`* 

*	Choose a notebook Title,  for example **`<House_modeling>`** 

*	Start the notebook with a *web reference* and one/more *image/s* of your **type of designe** 

*	List the **variables** used in your code, with a *textual definition*

*	Provide a *short description* of used **geometric methods** you are going to implement


*	Provide some **images** of your model from different viepoints

* 	Use measures (where necessary) in *meters ($m$)* 



## Style specs 


*	use **meaningfull** _identificators_ (variables and parameters)

*	use _camelCase_ ids

*	add **Python _`docstrings`_** (google for it)

*	produce a **single** notebook file, named *workshop_08.ipynb*

*	file path:  _`your_repo/2016-12-02/workshop_08.ipynb`_




# Minimal git/github instructions


## Minimal git/github instructions  (1/2)

create your local repository

```
$ mkdir 2016-12-02
$ cd 2016-12-02
$ touch workshop_08.ipynb
```


## Minimal git/github instructions  (2/2)

commit your work

```
$ git add -A .
$ git commit -m "add a short note to commit"
$ git push origin master
```
