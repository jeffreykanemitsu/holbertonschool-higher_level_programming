<p align="center">
<a href="https://www.holbertonschool.com/"><img src="https://s3.amazonaws.com/bloc-global-assets/almanac-assets/bootcamps/logos/000/002/676/original/Holberton-School.png?1467187334"/>
</a>
</p>

![Python](https://img.shields.io/badge/python-v3.4-blue.svg)

# 0x09. Python - Everything is object  #

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
          * [Mandatory 13](#mandatory-13)
          * [Mandatory 14](#mandatory-14)
          * [Mandatory 15](#mandatory-15)
          * [Mandatory 16](#mandatory-16)
          * [Mandatory 17](#mandatory-17)
          * [Mandatory 18](#mandatory-18)
          * [Mandatory 19](#mandatory-19)
          * [Mandatory 20](#mandatory-20)
          * [Mandatory 21](#mandatory-21)
          * [Mandatory 22](#mandatory-22)
          * [Mandatory 23](#mandatory-23)
          * [Mandatory 24](#mandatory-24)
          * [Mandatory 25](#mandatory-25)
          * [Mandatory 26](#mandatory-26)
          * [Mandatory 27](#mandatory-27)
          * [Mandatory 28](#mandatory-28)

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

<p>At the end of this project you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<ul>
<li>Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))</li>
<li>What is an object</li>
<li>What is the difference between a class and an object or instance</li>
<li>What is the difference between immutable object and mutable object</li>
<li>What is a reference</li>
<li>What is an assignment</li>
<li>What is an alias</li>
<li>How to know if two variables are identical</li>
<li>How to know if two variables are linked to the same object</li>
<li>How to display the variable identifier (which is the memory address in the CPython implementation)</li>
<li>What is mutable and immutable</li>
<li>What are the builtin mutable types</li>
<li>What are the builtin immutable types</li>
<li>How does Python pass variables to functions</li>
</ul>

### Compilation ###
All your files will be interpreted/compiled on Ubuntu 14.04 LTS using 'python3' (version 3.4.3)

### Requirements for Python ###
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `PEP 8` style
* All your files must be executable
* The length of your files will be tested using `wc`

### Requirements for txt answer files ###

<ul>
<li>Only one line</li>
<li>No Shebang</li>
<li>All your files should end with a new line</li>
</ul>

<p>Example:</p>

<pre><code>$ cat anwser.txt
Yes
$
</code></pre>

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
0. **Who I am?**
 <p>What function would you use to print the type of an object?
Write the name of the function in the file, without the <code>()</code></p>

#### Mandatory 1 ####
1. **Where are you?**
<p>How to get variable identifier (which is the memory address in the CPython implementation)?
Write the name of the function in the file, without the <code>()</code></p>

#### Mandatory 2 ####
2. **Right count**
<p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>
<pre><code>&gt;&gt;&gt; a = 89
&gt;&gt;&gt; b = 100
</code></pre>

#### Mandatory 3 ####
3. **Right count =**
<p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>
<pre><code>&gt;&gt;&gt; a = 89
&gt;&gt;&gt; b = 89
</code></pre>

#### Mandatory 4 ####
4. **Right count =**
<p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>
<pre><code>&gt;&gt;&gt; a = 89
&gt;&gt;&gt; b = a
</code></pre>

#### Mandatory 5 ####
5. **Right count =+**
  <p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>
<pre><code>&gt;&gt;&gt; a = 89
&gt;&gt;&gt; b = a + 1
</code></pre>

#### Mandatory 6 ####
6. **Is equal**
  <p>What should those 3 lines print:</p>

<pre><code>&gt;&gt;&gt; s1 = &quot;Holberton&quot;
&gt;&gt;&gt; s2 = s1
&gt;&gt;&gt; print(s1 == s2)
</code></pre>

#### Mandatory 7 ####
7. **Is the same**
  <p>What should those 3 lines print:</p>

<pre><code>&gt;&gt;&gt; s1 = &quot;Holberton&quot;
&gt;&gt;&gt; s2 = s1
&gt;&gt;&gt; print(s1 is s2)
</code></pre>

#### Mandatory 8 ####
8. **Is really equal**
  <p>What should those 3 lines print:</p>

<pre><code>&gt;&gt;&gt; s1 = &quot;Holberton&quot;
&gt;&gt;&gt; s2 = &quot;Holberton&quot;
&gt;&gt;&gt; print(s1 == s2)
</code></pre>

#### Mandatory 9 ####
9. **Is really the same**
  <p>What should those 3 lines print:</p>

<pre><code>&gt;&gt;&gt; s1 = &quot;Holberton&quot;
&gt;&gt;&gt; s2 = &quot;Holberton&quot;
&gt;&gt;&gt; print(s1 is s2)
</code></pre>

#### Mandatory 10 ####
10. **And with a list, is it equal**
<p>What should those 3 lines print:</p>

<pre><code>&gt;&gt;&gt; l1 = [1, 2, 3]
&gt;&gt;&gt; l2 = [1, 2, 3] 
&gt;&gt;&gt; print(l1 == l2)
</code></pre>

#### Mandatory 11 ####
11. **And with a list, is it the same**
  <p>What should those 3 lines print:</p>

<pre><code>&gt;&gt;&gt; l1 = [1, 2, 3]
&gt;&gt;&gt; l2 = [1, 2, 3] 
&gt;&gt;&gt; print(l1 is l2)
</code></pre>

#### Mandatory 12 ####
12. **And with a list, is it really equal**
  <p>What should those 3 lines print:</p>

<pre><code>&gt;&gt;&gt; l1 = [1, 2, 3]
&gt;&gt;&gt; l2 = l1
&gt;&gt;&gt; print(l1 == l2)
</code></pre>

#### Mandatory 13 ####
13. **And with a list, is it really the same**
 <p>What should print those 3 lines:</p>

<pre><code>&gt;&gt;&gt; l1 = [1, 2, 3]
&gt;&gt;&gt; l2 = l1
&gt;&gt;&gt; print(l1 is l2)
</code></pre>

#### Mandatory 14 ####
14. **List append**
  <p>What does this script print?</p>

<pre><code>l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
</code></pre>

#### Mandatory 15 ####
15. **List add**
  <p>What does this script print?</p>

<pre><code>l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
</code></pre>

#### Mandatory 16 ####
16. **Integer incrementation**
  <p>What does this script print?</p>

<pre><code>def increment(n):
    n += 1

a = 1
increment(a)
print(a)
</code></pre>

#### Mandatory 17 ####
17. **List incrementation**
  <p>What does this script print?</p>

<pre><code>def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
</code></pre>

#### Mandatory 18 ####
18. **List assignment**
  <p>What does this script print?</p>

<pre><code>def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
</code></pre>

#### Mandatory 19 ####
19. **Copy a list object**
  <p>Write a function <code>def copy_list(l):</code> that returns a <strong>copy</strong> of a list.</p>

<ul>
<li>The input list can contain any type of objects</li>
<li>Your file should be maximum 3-line long (no documentation needed)</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x09$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__(&#39;19-copy_list&#39;).copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

guillaume@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/0x09$ wc -l 19-copy_list.py 
3 19-copy_list.py
guillaume@ubuntu:~/0x09$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

#### Mandatory 20 ####
20. **Tuple or not?**
 <pre><code>a = ()
</code></pre>

<p>Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.</p>


#### Mandatory 21 ####
21. **Tuple or not?**
<pre><code>a = (1, 2)
</code></pre>

<p>Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.</p>


#### Mandatory 22 ####
22. **Tuple or not?**
  <pre><code>a = (1)
</code></pre>

<p>Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.</p>

#### Mandatory 23 ####
23. **Tuple or not?**
 <pre><code>a = (1, )
</code></pre>

<p>Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.</p>

#### Mandatory 24 ####
24. **Richard Sim's special #0**
  <p>What does this script print?</p>

<pre><code>a = (1)
b = (1)
a is b
</code></pre>

<p><em>Who is <a href="https://twitter.com/richard_d_sim">Richard Sim</a>?</em></p>

#### Mandatory 25 ####
25. **Richard Sim's special #1**
  <p>What does this script print?</p>

<pre><code>a = (1, 2)
b = (1, 2)
a is b
</code></pre>

#### Mandatory 26 ####
26. **Richard Sim's special #2**
  <p>What does this script print?</p>

<pre><code>a = ()
b = ()
a is b
</code></pre>

#### Mandatory 27 ####
27. **Richard Sim's special #3**
  <pre><code>&gt;&gt;&gt; id(a)
139926795932424
&gt;&gt;&gt; a
[1, 2, 3, 4]
&gt;&gt;&gt; a = a + [5]
&gt;&gt;&gt; id(a)
</code></pre>

<p>Will the last line of this script print <code>139926795932424</code>? Answer with <code>Yes</code> or <code>No</code>.</p>

#### Mandatory 28 ####
28. **Richard Sim's special #4**

  <pre><code>&gt;&gt;&gt; a
[1, 2, 3]
&gt;&gt;&gt; id (a)
139926795932424
&gt;&gt;&gt; a += [4]
&gt;&gt;&gt; id(a)
</code></pre>

<p>Will the last line of this script print <code>139926795932424</code>? Answer with <code>Yes</code> or <code>No</code>.</p>

#### Mandatory 29 ####
29. **Python3: Mutable, Immutable... everything is object!**
  <p>Write a blog post about everything you did just learn / this project is covering. Your blog post should be articulated this way (one paragraph per item):</p>

<ul>
<li>Introduction</li>
<li>id and type</li>
<li>mutable objects</li>
<li>immutable objects</li>
<li>why does it matter and how differently does Python treat mutable and immutable objects</li>
<li>how arguments are passed to functions and what does that imply for mutable and immutable objects</li>
</ul>

<p><em>If you worked on advanced tasks, please also include what you did learn in those tasks in the blog post.</em></p>

<p>Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top.
Publish your blog post on Medium or LinkedIn, and share it at least on Twitter and LinkedIn.</p>

