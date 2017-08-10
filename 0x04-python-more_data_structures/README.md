<p align="center">
<a href="https://www.holbertonschool.com/"><img src="https://s3.amazonaws.com/bloc-global-assets/almanac-assets/bootcamps/logos/000/002/676/original/Holberton-School.png?1467187334"/>
</a>
</p>

![Python](https://img.shields.io/badge/python-v3.4-blue.svg)

# Title  #

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
	* What are set and how to use them
	* What are the most common methods of set and how to use them
	* When to use sets versus lists
	* How to iterate into a set
	* What are dictionary and how to use them
	* When to use dictionaries versus lists or sets
	* What is a key in a dictionary
	* How to iterate into a dictionary
	* What is a lambda function
	* What is map, reduce and map functions

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
0. **Squared simple**
* Write a function that computes the square value of all integers of a matrix.
	* Prototype: `def square_matrix_simple(matrix=[]):`
	* `matrix` is a 2 dimensional array
	* Returns a new matrix:
		* Same size as `matrix`
		* Each value should be the square of the value of the input
	* Initial matrix should not be modified
	* You are not allowed to import any module
	* You are allow to use regular loops, `map`, etc.
```
guillaume@ubuntu:~/0x04$ cat 0-main.py
#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

guillaume@ubuntu:~/0x04$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/0x04$ 
```

#### Mandatory 1 ####
1. **Search and replace**
* Write a function that replaces all occurrences of an element by another in a new list.
	* Prototype: `def search_replace(my_list, search, replace):`
	* `list` is the initial list
	* `search` is the element to replace in the list
	* `replace` is the new element
	* You are not allowed to import any module
```
guillaume@ubuntu:~/0x04$ cat 1-main.py
#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x04$ ./1-main.py
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
guillaume@ubuntu:~/0x04$ 
```

#### Mandatory 2 ####
2. **Unique addition**
* Write a function that makes the addition of all unique integers in a list (only one time each integer).
	* Prototype: `def uniq_add(my_list=[]):`
	* You are not allowed to import any module
```
guillaume@ubuntu:~/0x04$ cat 2-main.py
#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

guillaume@ubuntu:~/0x04$ ./2-main.py
Result: 15
guillaume@ubuntu:~/0x04$ 
```

#### Mandatory 3 ####
3. **Present in both**
* Write a function that returns a set of common elements in two sets.
	* Prototype: `def common_elements(set_1, set_2):`
	* You are not allowed to import any module
```
guillaume@ubuntu:~/0x04$ cat 3-main.py
#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

guillaume@ubuntu:~/0x04$ ./3-main.py
['C']
guillaume@ubuntu:~/0x04$ 
```

#### Mandatory 4 ####
4. **Only differents**
	* Prototype: `def only_diff_elements(set_1, set_2):`
	* You are not allowed to import any module
```
guillaume@ubuntu:~/0x04$ cat 4-main.py
#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))

guillaume@ubuntu:~/0x04$ ./4-main.py
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
guillaume@ubuntu:~/0x04$ 
```

#### Mandatory 5 ####
5. **Number of keys**
* Write a function that returns the number of keys in a dictionary.
	* Prototype: `def number_keys(my_dict):`
	* You are not allowed to import any module
```
guillaume@ubuntu:~/0x04$ cat 5-main.py
#!/usr/bin/python3
number_keys = __import__('5-number_keys').number_keys

my_dict = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(my_dict)
print("Number of keys: {:d}".format(nb_keys))

guillaume@ubuntu:~/0x04$ ./5-main.py
Number of keys: 3
guillaume@ubuntu:~/0x04$ 
```

#### Mandatory 6 ####
6. **Print sorted dictionary**
	* Prototype: `def print_sorted_dictionary(my_dict):`
	* You can assume that all keys are string
	* Keys should be sorted by alphabetic order
	* Only sort keys of the first level (don't sort keys of a dictionary inside the main dictionary)
	* Dictionary values can have any type
	* You are not allowed to import any module
```
guillaume@ubuntu:~/0x04$ cat 6-main.py
#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

my_dict = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(my_dict)

guillaume@ubuntu:~/0x04$ ./6-main.py
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
guillaume@ubuntu:~/0x04$ 
```

#### Mandatory 7 ####
7. **Update dictionary**
* Write a function that replace or add key/value in a dictionary.
	* Prototype: `def update_dictionary(my_dict, key, value):`
	* `key` argument will be always a string
	* `value` argument will be any type
	* If a key exists in the dictionary, the value will be replaced
	* If a key doesn't exist in the dictionary, it will be created
	* You are not allowed to import any module
```
guillaume@ubuntu:~/0x04$ cat 7-main.py
#!/usr/bin/python3
update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

my_dict = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(my_dict, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(my_dict)

print("--")
print("--")

new_dict = update_dictionary(my_dict, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(my_dict)

guillaume@ubuntu:~/0x04$ ./7-main.py
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
guillaume@ubuntu:~/0x04$ 
```

#### Mandatory 8 ####
8. **Simple delete by key**
* Write a function that deletes a key in a dictionary.
	* Prototype: `def simple_delete(my_dict, key=""):`
	* `key` argument will be always a string
	* If a key doesn't exist, the dictionary won't change
	* You are not allowed to import any module
```
guillaume@ubuntu:~/0x04$ cat 8-main.py
#!/usr/bin/python3
simple_delete = __import__('8-simple_delete').simple_delete
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

my_dict = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(my_dict, 'track')
print_sorted_dictionary(my_dict)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = simple_delete(my_dict, 'c_is_fun')
print_sorted_dictionary(my_dict)
print("--")
print_sorted_dictionary(new_dict)

guillaume@ubuntu:~/0x04$ ./8-main.py
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
--
--
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
guillaume@ubuntu:~/0x04$ 
```

#### Mandatory 9 ####
9. **Multiply by 2**
* Write a function that returns a new dictionary with all values multiplied by 2
	* Prototype: `def multiply_by_2(my_dict):`
	* You can assume that all values are only integers
	* Returns a new dictionary
	* You are not allowed to import any module
```
guillaume@ubuntu:~/0x04$ cat 9-main.py
#!/usr/bin/python3
multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

my_dict = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(my_dict)
print_sorted_dictionary(my_dict)
print("--")
print_sorted_dictionary(new_dict)

guillaume@ubuntu:~/0x04$ ./9-main.py
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
guillaume@ubuntu:~/0x04$ 
```

#### Mandatory 10 ####
10. **Best score**
* Write a function that returns a key with the biggest integer value.
	* Prototype: `def best_score(my_dict):`
	* You can assume that all values are only integers
	* If no score found, return `None`
	* You can assume all students have a different score
	* You are not allowed to import any module
```
guillaume@ubuntu:~/0x04$ cat 10-main.py
#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

my_dict = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(my_dict)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))

guillaume@ubuntu:~/0x04$ ./10-main.py
Best score: Molly
Best score: None
guillaume@ubuntu:~/0x04$ 
```

#### Mandatory 11 ####
11. **Multiply by using map**
* Write a function that returns a list with all values multiplied by a number without using any loops.
	* Prototype: `def mutiply_list_map(my_list=[], number=0):`
	* Returns a new list:
		* Same length as `my_list`
		* Each value should be multiplied by `number`
	* Initial list should not be modified
	* You are not allowed to import any module
	* You have to use `map`
	* Your file should be max 3 lines
```
guillaume@ubuntu:~/0x04$ cat 11-main.py
#!/usr/bin/python3
mutiply_list_map = __import__('11-mutiply_list_map').mutiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = mutiply_list_map(my_list, 4)
print(new_list)
print(my_list)

guillaume@ubuntu:~/0x04$ ./11-main.py
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
guillaume@ubuntu:~/0x04$ 
```
