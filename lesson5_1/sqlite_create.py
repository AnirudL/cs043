#sqlite_create.py

import sqlite3

connection = sqlite3.connect('business.db')
connection.execute('CREATE TABLE products (prodname, price, weight)')
#This line creates the first table, called products, which holds the name, price, and weight of the product.
connection.execute('CREATE TABLE users (name, password, email)')
#This line creates a second table, called users, which holds the name, password, and email of the user.