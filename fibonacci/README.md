## Problem Statement
An initial attempt at writing a function that computes Fibonacci numbers is given below:

```ptyhon
def fibonacci( term_n ) :
    if term_n == 1:
        return 1
    output = [1]
    x=0
    while x < term_n:
        output[x] = output[x] + output[x - 1]
    return output[term_n]
```

Please
a) debug this code and identify what would need to be fixed, and
b) indicate what comments you would make if you saw this code pushed to PR.
