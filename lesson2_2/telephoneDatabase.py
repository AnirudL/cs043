import os
from lesson2_2.database import Simpledb

print("""
Welcome to the Simple Database

There are four functions:

insert(filename,key,value)    =  Insert a key and value
select_one(filename,key)       =  Select a key and view the value
delete(filename,key)               =  Choose a key to delete the row from the file
modify(filename,key,value)  =  Choose a key and modify its value
""")
print('')
print("""
To get started, create a class and enter a filename in the parameters of Simpledb

Example:

example = Simpledb('filename.txt')
""")

