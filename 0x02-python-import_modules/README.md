<p align="center">
<a href="https://www.holbertonschool.com/"><img src="https://s3.amazonaws.com/bloc-global-assets/almanac-assets/bootcamps/logos/000/002/676/original/Holberton-School.png?1467187334"/>
</a>
</p>

![Python](https://img.shields.io/badge/python-v3.4-blue.svg)
![Holberton](https://img.shields.io/badge/Holberton-Batch 3-red.svg)


# 0x02. Python - import & modules  #

* [Table of Contents](#table-of-contents)
	* [Author](#author)
	* [Description](#description)
	* [Objectives](#objectives)
	* [Compilation](#compilation)
	* [Requirements](#requirements)
	* [Zen](#zen)
	* [Tasks](#tasks)
	  * [Mandatory 0](#mandatory-0)
	  * [Mandatory 1](#mandatory-1)
	  * [Mandatory 2](#mandatory-2)
	  * [Mandatory 3](#mandatory-3)
	  * [Mandatory 4](#mandatory-4)
	  * [Mandatory 5](#mandatory-5)
### Author ###
* Jeffrey Kanemitsu
    * [Github](https://github.com/jeffreykanemitsu)
    * [Twitter](https://twitter.com/canofmisosoup)
### Description ###
Understanding concepts of the high-level language.

<p align="center">
<a href="https://www.python.org/"><img src="http://www.bebetterdeveloper.com/img/post_img/python-logo.png"/>
</a>
</p>

### Objectives ###
* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* How to import functions from another file
* How to use imported functions
* How to create a module
* How to use the built-in function dir()
* How to prevent code in your script from being executed when imported
* How to use command line arguments with your Python programs

### Compilation ###
All your files will be interpreted/compiled on Ubuntu 14.04 LTS using 'python3' (version 3.4.3)

### Requirements ###
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `PEP 8` style
* All your files must be executable
* The length of your files will be tested using `wc`

### Zen ###
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

### Tasks ###
#### Mandatory 0 ####
0. **Import a simple function from a simple file**
* Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`
	* You have to use `print` function with string format to display integers
	* You have to assign:
		* the value `1` to a variable called `a`
		* the value `2` to a variable called `b`
		* and use those two variables as arguments when calling the functions `add` and `print`
	* Your program should print: `<a value> + <b value> = <add(a, b) value>` followed with a new line
	* You can only use the word `add_0` once in your code
	* You are not allowed to use `*` for importing
	* Your code should not be executed when imported
#### Mandatory 1 ####
1. **My first toolbox!**
* Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.
	* Do not use the function `print` (with string format to display integers) more than 4 times
	* You have to define:
		* the value `10` to a variable `a`
		* the value `5` to a variable `b`
	* and use those two variables only, as arguments when calling functions (included `print`)
	* Your program should call each of the imported functions. See example bellow for format
	* the word `calculator_1` should be used only once in your file
	* You are not allowed to use `*` for importing
	* Your code should not be executed when imported
#### Mandatory 2 ####
2. **How to make a script dynamic!**
* Write a program that prints the number of and the list of its arguments.
	* The output should be:
		* Number of argument(s) followed by argument or arguments, followed by
		* `:` (or `.` if no argument where passed) followed by
		* one line per argument:
			* the position of the argument (starting at `1`) followed by `:`, followed by the argument value and a new line
	* Your code should not be executed when imported
	* The number of elements of `argv` can be retrieved by using: `len(argv)`
	* You do not have to fully understand lists yet, but imagine that `argv` can be used just like a C array: you can use an index to walk through it. There are other ways (preferred in a near Future), if you know them you can use them.
#### Mandatory 3 ####
3. **Infinite addition**
* Write a program that prints the result of the addition of all arguments
	* The output should be the result of the addition of all arguments, followed by a new line
	* You can cast arguments into integers by using `int()` (you can assume that all arguments can be casted into integers)
	* Your code should not be executed when imported
#### Mandatory 4 ####
4. **Who are you?**
* Write a program that prints all the names defined by the compiled module [hidden_4.pyc](https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc) (please download it locally).
	* You should print one name per line, in alpha order
	* You should print only names that do not start with `__`
	* Your code should not be executed when imported

#### Mandatory 5 ####
**Everything can be imported**
* Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.
	* You are not allowed to use `*` for importing
	* Your code should not be executed when imported
