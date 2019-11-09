from MyHdb import MyHdb

hdb = MyHdb()

hdb.execute("SELECT pstyv, kurztext from $TJHAPT")
records = hdb.fetchmany(3)   #fetchone(), fetchall()
print(records)