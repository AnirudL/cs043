from lesson2_2.database import Simpledb

db = Simpledb("recipes.txt")
db.insert("relish", "Pickled cucumber and sugar")
print(db.select_one("relish"))