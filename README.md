# Project Euler Manager
**IN PROGRESS**
## Purpose
Project Euler (https://projecteuler.net/) is a collection of mathematical problems that generally depend on computation
rather than just theoretical reasoning. Solving the problems is a great way to learn more about programming as well as
more about mathematics.

When I was brand new to programming (coming from a math background) I enjoyed working on these problems. I still do, but
I thought it would be fun to combine all of my solutions into a single project. There is really no reason to do that,
but it has been fun so far.

This project allows the user to write their own solutions to the problems and run them and store the solution and time
taken to complete.
## Setup

### solution structure
The directory 'solutions' must contain the user's solution code split into a module corresponding to the decade the
problem is in with a function corresponding to the problem **mod** 10.
* e.g. problem 34 will be found in the module `_3.py` in the function `four`
* e.g. problem 120 will be found in the module `_12.py` in the function `zero`

**WARNING**:
The function `zero` found in `_0.py` is reserved for testing. See below.

### testing
In order to test the functions that call the problem solution code

```Python
def zero():
    """FOR USE TESTING"""
    return "Test function successfully completed"
```