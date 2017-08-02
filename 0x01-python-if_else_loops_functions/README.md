<p align="center">
<img src="https://s3.amazonaws.com/bloc-global-assets/almanac-assets/bootcamps/logos/000/002/676/original/Holberton-School.png?1467187334" alt="Holberton's logo"/>
</p>

# 0x01. Python - if/else, loops, functions #

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
	  * [Mandatory 6](#mandatory-6)
	  * [Mandatory 7](#mandatory-7)
	  * [Mandatory 8](#mandatory-8)
	  * [Mandatory 9](#mandatory-9)
	  * [Mandatory 10](#mandatory-10)
	  * [Mandatory 11](#mandatory-11)
	  * [Mandatory 12](#mandatory-12)
### Author ###
* Jeffrey Kanemitsu
	* [Github](https://github.com/jeffreykanemitsu)	
	* [Twitter](https://twitter.com/canofmisosoup)
### Description ###
Understanding concepts of the higher level language - Python.
### Objectives ###
* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* Why indentation is so important in Python
* How to use the if, if ... else statements
* How to use comments
* How to affect values to variables
* How to use the while and for loops
* How is the Python's for different from the C's?
* How to use the break and continues statements
* How to use else clauses on loops
* What does the pass statement do, and when to use it
* How to use range
* What is a function and how do you use functions
* What does return a function that does not use any return statement
* Scope of variables
* What's a traceback
* What are the arithmetic operators and how to use them
### Compilation ###
All your files will be interpreted/compiled on Ubuntu 14.04 LTS using 'python3' (version 3.4.3)
### Requirements ###
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style
* All your files must be executable
* The length of your files will be tested using wc
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
0. **Positive anything is better than negative nothing**
 * This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.
 * [Source code](https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py)
 * The variable `number` will store a different value every time you will run this program
 * You don't have to understand what `import`, `random. randint` do. Please do not touch this code
 * The output of the program should be:
	* The number, followed by:
		* if the number is greater than 0: `is positive`
		* if the number is 0: `is zero`
		* if the number is less than 0: `is negative`
	* followed by a new line
#### Mandatory 1 ####
1. **The last digit**
 * This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`.
	* [Source code](https://github.com/holbertonschool/0x01.py/blob/master/1-last_digit_py)
	* The variable `number` will store a different value every time you will run this program
	* You don't have to understand what `import`, `random`. `randint` do. Please do not touch this code
	* The output of the program should be:
		* The string `Last digit of`, followed by:
		* the number, followed by
		* the string `is`, followed by
			* if the number is greater than 5: the string and is greater than 5
			* if the number is 0: the string and is 0
			* if the number is less than 6 and not 0: the string and is less than 6 and not 0
		* followed by a new line
#### Mandatory 2 ####
2. **I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game**
 * Write a program that prints the alphabet, in lowercase, not followed by a new line.
	* You can only use one `print` function with string format
	* You can only use one loop in your code
	* You are not allowed to store characters in a variable
	* You are not allowed to import any module
#### Mandatory 3 ####
3. **When I was having that alphabet soup, I never thought that it would pay off**
 * Write a program that prints the alphabet, in lowercase, not followed by a new line.
	* Print all the letters except `q` and `e`
	* You can only use one `print` function with string format
	* You can only use one loop in your code
	* You are not allowed to store characters in a variable
	* You are not allowed to import any module
#### Mandatory 4 ####
4. **Hexadecimal printing**
 * Write a program that prints all numbers from `0` to `98` in decimal and in hexadecimal (as in the following example)
	* You can only use one `print` function with string format
	* You can only use one loop in your code
	* You are not allowed to store numbers or strings in a variable
	* You are not allowed to import any module
#### Mandatory 5 ####
5. **00...99**
 * Write a program that prints numbers from `0` to `99`.
	* Numbers must be separated by `,`, followed by a space
	* Numbers should be printed in ascending order, with two digits
	* The last number should be followed by a new line
	* You can only use no more than 2 `print` functions with string format
	* You can only use one loop in your code
	* You are not allowed to store numbers or strings in a variable
	* You are not allowed to import any module
#### Mandatory 6 ####
6. **Inventing is a combination of brains and materials. The more brains you use, the less material you need**
 * Write a program that prints all possible different combinations of two digits.
	* Numbers must be separated by ,, followed by a space
	* The two digits must be different
	* `01` and `10` are considered the same combination of the two digits `0` and `1`
	* Print only the smallest combination of two digits
	* Numbers should be printed in ascending order, with two digits
	* The last number should be followed by a new line
	* You can only use no more than 3 `print` functions with string format
	* You can only use no more than 2 loops in your code
	* You are not allowed to store numbers or strings in a variable
	* You are not allowed to import any module
#### Mandatory 7 ####
7. **islower**
 * Write a function that checks for lowercase character.
	* Prototype: `def islower(c):`
	* Returns `True` if `c` is lowercase
	* Returns `False` otherwise
	* You are not allowed to import any module
	* You are not allowed to use `str.upper()` and `str.isupper()`
	* [Tips:ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)
	* You don't need to understand `__import__`
#### Mandatory 8 ####
8. **To uppercase**
 * Write a function that print a string in uppercase followed by a new line.
	* Prototype: `def uppercase(str):`
	* You can only use no more than 2 `print` functions with string format
	* You can only use one loop in your code
	* You are not allowed to import any module
	* You are not allowed to use `str.upper()` and `str.isupper()`
	* [Tips:ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)
	* You don't need to understand `__import__`
#### Mandatory 9 ####
9. **There are only 3 colors, 10 digits, and 7 notes; its what we do with them that's important**
 * Write a function that prints the last digit of a number.
	* Prototype: `def print_last_digit(number):`
	* Returns the value of the last digit
	* You are not allowed to import any module
	* You don't need to understand `__import__`
#### Mandatory 10 ####
10. **a + b**
 * Write a function that adds two integers and returns the result.
	* Prototype: `def add(a, b):`
	* Returns the value of `a + b`
	* You are not allowed to import any module
	* You don't need to understand `__import__`
#### Mandatory 11 ####
11. **a ^ b**
 * Write a function that computes `a` to the power of `b` and return the value.
	* Prototype: `def pow(a, b):`
	* Returns the value of `a ^ b`
	* You are not allowed to import any module
	* You don't need to understand `__import__`
#### Mandatory 12 ####
12. **Fizz Buzz**
 * Write a function that prints the numbers from 1 to 100 separated by a space.
	* For multiples of three print `Fizz` instead of the number and for multiples of five print `Buzz`.
	* For numbers which are multiples of both three and five print `FizzBuzz`.
	* Prototype: `def fizzbuzz():`
	* Each element should be followed by a space
	* You are not allowed to import any module
	* You don't need to understand `__import__`
