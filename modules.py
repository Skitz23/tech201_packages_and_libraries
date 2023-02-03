# Modules

import os
import math, datetime, sys

working_directory = os.getcwd()
print(working_directory)

def return_user_id():
    print(os.getpid())

def return_user_name():
    print(os.uname())

print(datetime.date.today())

print((sys.path))

print(math.remainder(1, 5))

# when you are building a program its really important to think whether you need to make an object/ class or simply a function

# Built in functions

# print()
# len()
# type()



