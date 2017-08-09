<p align="center">
<a href="https://www.holbertonschool.com/"><img src="https://s3.amazonaws.com/bloc-global-assets/almanac-assets/bootcamps/logos/000/002/676/original/Holberton-School.png?1467187334"/>
</a>
</p>

![Python](https://img.shields.io/badge/python-v3.4-blue.svg)

# 0x03. Python - Data Structures: Lists, Tuples  #

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
Understanding concepts of the high-level language.

<p align="center">
<a href="https://www.python.org/"><img src="http://www.bebetterdeveloper.com/img/post_img/python-logo.png"/>
</a>
</p>

### Objectives ###
* At the end of this project you are expected to be able to explain to anyone, without the help of Google:

	* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
	* What are lists and how to use them
	* What are the differences and similarities between strings and lists
	* What are the most common methods of lists and how to use them
	* How to use lists as stacks and queues
	* What are list comprehensions and how to use them
	* What are tuples and how to use them
	* When to use tuples versus lists
	* What is a sequence
	* What is tuple packing
	* What is sequence unpacking
	* What is the del statement and how to use it

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
0. **Print a list of integers**
* Write a function that prints all integers of a list.
	* Prototype: `def print_list_integer(my_list=[]):`
	* Format: one integer per line. See example
	* You are not allowed to import any module
	* You can assume that the list only contains integers
	* You are not allowed to cast integers into strings
	* You have to use `str.format()` to print integers
```
guillaume@ubuntu:~/0x03$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/0x03$ 
```
#### Mandatory 1 ####
1. **Secure access to an element in a list**
* Write a function that retrieves an element from a list.
	* Prototype: `def element_at(my_list, idx):`
	* If `idx` is out of range (>number of element in `my_list` or negative), the function should return `None`
	* You are not allowed to import any module
	* You are not allowed to use `try/except`
```
guillaume@ubuntu:~/0x03$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

guillaume@ubuntu:~/0x03$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/0x03$ 
```
#### Mandatory 2 ####
2. **Replace element**
* Write a function that replaces an element of a list at a specific position.
	* Prototype: `def replace_in_list(my_list, idx, element):`
	* If `idx` is out of range (> of number of element in `my_list` or negative), the function should not modify anything, and returns the original list
	* You are not allowed to import any module
	* You are not allowed to use `try/except`
```
guillaume@ubuntu:~/0x03$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
guillaume@ubuntu:~/0x03$ 
```
#### Mandatory 3 ####
3. **Print a list of integers... in reverse!**
* Write a function that prints all integers of a list, in reverse order.
	* Prototype: `def print_reversed_list_integer(my_list=[]):`
	* Format: one integer per line. See example
	* You are not allowed to import any module
	* You can assume that the list only contains integers
	* You are not allowed to cast integers into strings
	* You have to use `str.format()` to print integers
```
guillaume@ubuntu:~/0x03$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/0x03$ 
```
#### Mandatory 4 ####
4. **Replace in a copy**
* Write a function that replaces an element in a list at a specific position without modifying the original list.
	* Prototype: `def new_in_list(my_list, idx, element):`
	* If `idx` is out of range (> of number of element in `my_list` or negative), the function should return a copy of the original `list`
	* You are not allowed to import any module
	* You are not allowed to use `try/except`
```
guillaume@ubuntu:~/0x03$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
guillaume@ubuntu:~/0x03$ 
```

#### Mandatory 5 ####
5. **Can you C me now?**
* Write a function that removes all characters `c` and `C` from a string.
	* Prototype: `def no_c(my_string):`
	* The function shoud return the new string
	* You are not allowed to import any module
	* You are not allowed to use `str.replace()`
```
guillaume@ubuntu:~/0x03$ cat 5-main.py
#!/usr/bin/env python3
no_c = __import__('5-no_c').no_c

print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

guillaume@ubuntu:~/0x03$ ./5-main.py
Holberton Shool
hiago
 is fun!
guillaume@ubuntu:~/0x03$ 
```

#### Mandatory 6 ####
6. **Lists of lists = Matrix**
* Write a function that prints a matrix of integers.
	* Prototype: `def print_matrix_integer(matrix=[[]]):`
	* Format: see example
	* You are not allowed to import any module
	* You can assume that the list only contains integers
	* You are not allowed to cast integers into strings
	* You have to use `str.format()` to print integers
```
guillaume@ubuntu:~/0x03$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

guillaume@ubuntu:~/0x03$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/0x03$ 
```
#### Mandatory 7 ####
7. **Tuples addition**
* Write a function that adds 2 tuples.
	* Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
	* Returns a tuple with 2 integers:
		* The first element should be the addition of the first element of each argument
		* The second element should be the addition of the second element of each argument
	* You are not allowed to import any module
	* You can assume that the two tuples will only contain integers
	* If a tuple is smaller than 2, use the value `0` for each missing integer
	* If a tuple is bigger than 2, use only the first 2 integers
```
guillaume@ubuntu:~/0x03$ cat 7-main.py
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

guillaume@ubuntu:~/0x03$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
guillaume@ubuntu:~/0x03$ 
```
#### Mandatory 8 ####
8. **More returns!**
* Write a function that returns a tuple with the length of a string and its first character.
	* Prototype: `def multiple_returns(sentence):`
	* If the sentence is empty, the first character should be equal to `None`
	* You are not allowed to import any module
```
guillaume@ubuntu:~/0x03$ cat 8-main.py
#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

guillaume@ubuntu:~/0x03$ ./8-main.py
Length: 32 - First character: A
guillaume@ubuntu:~/0x03$ 
```

#### Mandatory 9 ####
9. **Find the max**
* Write a function that finds the biggest integer of a list.
	* Prototype: `def max_integer(my_list=[]):`
	* If the list is empty, return `None`
	* You can assume that the list only contains integers
	* You are not allowed to import any module
	* You are not allowed to use the builtin `max()`
```
guillaume@ubuntu:~/0x03$ cat 9-main.py
#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

guillaume@ubuntu:~/0x03$ ./9-main.py
Max: 90
guillaume@ubuntu:~/0x03$ 
```

#### Mandatory 10 ####
10. **Only by 2**
* Write a function that finds all multiples of 2 in a list.
	* Prototype: `def divisible_by_2(my_list=[]):`
	* Return a new list with `True` or `False`, depending on wether the integer at the same position in the original list is a multiple of 2
	* The new list should have the same size as the original list
	* You are not allowed to import any module
```
guillaume@ubuntu:~/0x03$ cat 10-main.py
#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

guillaume@ubuntu:~/0x03$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
guillaume@ubuntu:~/0x03$ 
```

#### Mandatory 11 ####
11. **Delete at**
* Write a function that deletes the item at a specific position in a list.
	* Prototype: `def delete_at(my_list=[], idx=0):`
	* You are not allowed to use `pop()`
	* You are not allowed to import any module
```
guillaume@ubuntu:~/0x03$ cat 11-main.py
#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./11-main.py
[1, 2, 3, 5]
[1, 2, 3, 5]
guillaume@ubuntu:~/0x03$ 
```

#### Mandatory 12 ####
12. **Switch**
* Write the source code in order to switch value of `a` and `b`
	* You can find the source code [here](https://github.com/holbertonschool/0x03.py/blob/master/12-switch_py)
	* Your code should be inserted where the comment is (line 4)
	* Your program should be exactly 5 lines long
```
guillaume@ubuntu:~/py/0x03$ ./12-switch.py
a=10 - b=89
guillaume@ubuntu:~/py/0x03$ wc -l 12-switch.py
5 12-switch.py
guillaume@ubuntu:~/py/0x03$ 
```
