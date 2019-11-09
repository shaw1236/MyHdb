from MyHdb import MyHdb

hdb = MyHdb()
hdb.execute("SELECT 'Hello Python World' FROM DUMMY")
print(hdb.fetchone())
