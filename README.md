# tech201_packages_and_libraries


# what is a library in python?

A Python library is a collection of related modules. It codes that can be used repeatedly in different programs. A python library is a simpler and easier because we don't need to write the same code again for different programs.

# What is module in Python?
A module is a collection of code or functions that uses the . py extension. A Python library is a set of related modules or packages bundled together

# What is PIP?
PIP is a package manager for Python packages, or modules if you like.

# What is a Package?
A package contains all the files you need for a module.
Modules are Python code libraries you can include in your project.


# How to install packages in python?

(1) First, type Command Prompt in the Windows search box

(2) Next, open the Command Prompt, and you’ll see the following screen with your user name (to avoid any permission issues, you may consider to run the Command Prompt as an administrator):

(3) In the Command Prompt, type “cd\” as this command will ensure that your starting point has only the drive name:

(4) Press Enter. Now you’ll see the drive name of C:\>

(5) Locate your Python Scripts path. The Scripts folder can be found within the Python application folder, where you originally installed Python.

Here is an example of a Python Scripts path:

C:\Users\Ron\AppData\Local\Programs\Python\Python39\Scripts

(6) In the Command Prompt, type cd followed by your Python Scripts path:

(7) Press Enter

(8) Now, type the pip install command to install your Python package.

(9) Finally, press Enter, and you’ll notice that the package will be installed:






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