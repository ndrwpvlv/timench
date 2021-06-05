# Timench
**Timench** is measure execution time class-based library for working with multiple functions 

Basic usage code:
```python
from timench import Timench


def factorial(n: int):
    if n == 1:
        return n
    if n < 1:
        return 'Enter number bigger or equal 1'
    f = 1
    for _ in range(1, n + 1):
        f *= _
    return f


tch = Timench()
repeats = 1000

tch.add_func(factorial.__name__, factorial)
tch.run(factorial.__name__, repeats, 1000)
print(tch.get_report(factorial.__name__))
tch.write_reports()
```
Output example:
```
Running: factorial
---
Total time = 0.419085 sec
Best loop time = 0.000344992 sec
Average loop time = 0.000419085 sec
Repeats = 1000
```