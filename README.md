# tech201_packages_and_libraries


# what is a library in python?

A Python library is a collection of related modules. It codes that can be used repeatedly in different programs. A python library is a simpler and easier because we don't need to write the same code again for different programs.

# What is module in Python?
A module is a collection of code or functions that uses the . py extension. A Python library is a set of related modules or packages bundled together


```class Fizzbuzz:

    def __init__(self, start_of_range, end_of_range):
        self.fizzrange = range(start_of_range, end_of_range + 1)
        self.fizzbuzz_list = []
        self._fizzbuzz_iterator()

    def _divisible_by(self, num1, num2):
        if num1 % num2 == 0:
            return True
        else:
            return False

    def _fizzbuzz_iterator(self):

        for num in self.fizzrange:
            if self._divisible_by(num, 15):
                self.fizzbuzz_list.append("fizzbuzz")
            elif self._divisible_by(num, 5):
                self.fizzbuzz_list.append("buzz")
            elif self._divisible_by(num, 3):
                self.fizzbuzz_list.append("fizz")
            else:
                self.fizzbuzz_list.append(num)
```

I created a Fizzbuzz Python file and imported the code onto another file called program.py

```
from app.fizzbuzz import Fizzbuzz

one_to_100 = Fizzbuzz(1, 100)

print(one_to_100.fizzbuzz_list)
```

The first line of the code shows me importing the code of Fizzbuzz. When I done this i made sure to use Capital F otherwise their would be an error on the system.

The second line of my code shows that i want fizzbuzz to go from 1-100

The third line of my code shows that I and listing fizzbuzz from 1-100 and this would run because my fizzbuzz code has list code

```
self.fizzbuzz_list = []
```