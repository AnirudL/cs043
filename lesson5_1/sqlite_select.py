#sqlite_select.py

import sqlite3

connection = sqlite3.connect('business.db')

cursor = connection.cursor()

product_cursor = cursor.execute('SELECT * FROM products')
product_list = product_cursor.fetchall()

for pname, weight in product_list:
    print('Product: {}\tWeight: {} kg'.format(pname, weight))