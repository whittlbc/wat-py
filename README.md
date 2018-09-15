# wat

Simple interactive breakpoint library with automatic variable injection, providing access to **both** local and global variables.

**Better than** `print` because you can actually interact with your variables.<br>
**Better than** `code.interact` because you get both local and global variables.<br>
**Better than anything else** because it's short and sweet, has no dependencies, and works with both Python 2 & 3.<br>

# Installation

```
$ pip install wat-py
```

# Quickstart

```python
from wat import wat

wat() # set interactive breakpoint
```

# Usage

### Set a breakpoint

Setting an interactive breakpoint is as easy as calling `wat()` from whatever line you want.

Example:
```python
# Example app.py file
from wat import wat
import urllib

a = 1
b = 2


def do_something():
  a = 10
  c = 3
  wat()
  # more code-sauce


if __name__ == '__main__':
  do_something()
```

Running `app.py` will call the `do_something` function and pause code execution right after `c` is defined.
An interactive console will appear, giving you access to all vars (both local and global) that `do_something` would 
otherwise have access to at the time of the breakpoint:

```python
$ python app.py
(wat Interactive Console)
>>> a
10                          # local var overwrites global var
>>> b
2                           # global var
>>> c
3                           # local var
>>> urllib
<module 'urllib' from ...>  # imported module still available
```

### Leave interactive console & proceed with code execution

`Ctrl+D`

### Leave interactive console without executing any more code

`exit()`

# Reason

The built-in `code.interact` method Python provides requires you to pass in the specific variables you want to have 
available in the interactive console, which gives you the option of passing in `locals()`, `globals()`, or manually 
creating a dict with the combination of both local and global vars (which no one wants to do every single time they want to set a breakpoint). I got sick of writing `import code; code.interact(local=locals())` whenever I needed to set a 
breakpoint, realizing I needed some global vars from the import statements at the top of my file, and then having to 
manually re-import those global vars.

# License

MIT
