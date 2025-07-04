# First Commands with Python

This class taught how to apply the first commands in Python, from print() to the declaration of Primitive Data Types. In addition, it taught how to correctly install Python, VS Code, Git and finally, how to use Github, allowing the scripts developed to be versioned and shared on GitHub.

# Main Points of the Class:

**Data Types**

Python supports several data types, including, but not limited to:

* Integers (`int`)
* Floating point numbers (`float`)
* Strings (`str`)
* Lists (`list`)
* Tuples (`tuple`)
* Dictionaries (`dict`)
* Booleans (`bool`)

The language determines the data type of a variable at the time of assignment, which allows great flexibility, but also requires attention to avoid type errors.

**Variable Names**

Python has some rules and conventions for variable names:

* Names can contain letters, numbers, and underscores (`_`), but they cannot begin with a number.

* Variable names are case-sensitive, which means that `variable`, `Variavel`, and `VARIaVEL` are considered three different variables.

* There are some reserved words that cannot be used as variable names, such as `if`, `for`, `class`, and others.

* It is recommended to follow the _snake_case_ convention for variable names that consist of more than one word, such as `username` or `total_orders`.

**Dynamicity and Reassignment**

A key feature of Python variables is the ability to reassign them to different data types:

```python
x = 100 # x is an integer
x = "Python" # x is now a string
```

This demonstrates Python's dynamic typing, but it also highlights the importance of managing data types carefully to avoid confusion or errors in more complex programs.

**Variable Scope**

The scope of a variable determines where it is accessible within the code. Variables defined within a main block are globally accessible, while variables defined within functions are local to those functions unless explicitly declared as `global`.

Understanding variables and data types is essential to Python programming, as it allows you to manipulate data effectively and create dynamic, flexible programs. Python's ability to infer data types makes the language accessible to beginners while still offering powerful functionality to experienced programmers.