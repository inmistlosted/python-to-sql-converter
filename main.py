from Py2SQL.Py2SQL import Py2SQL
from Py2SQL.Py2SQL import Database
from entity.Dog import Dog
from entity.Dog2 import Dog2

if __name__ == '__main__':
    db = Database('localhost', 3050, 'D:/4kurs/1semestr/metaProgramming/Labs/Lab3/db/TEST.FDB', 'SYSDBA', 'admin')
    dbms = Py2SQL()
    dbms.db_connect(db)
    print(dbms.db_engine())
    print(dbms.db_name())
    print(dbms.db_size())
    print(dbms.db_tables())
    print(dbms.db_table_structure('DOGS'))
    print(dbms.db_table_size('CATS'))

    dog = Dog(1, "Toto", 12, "black")
    print(dbms.find_object('DOGS', dog))
    print(dbms.find_objects_by('DOGS', age = 12, id = 1))

    attrs = ['age']
    print(dbms.find_class(Dog2))
    print(dbms.find_classes_by('age', 'id'))
    df = dbms.create_object('DOGS', 2)
    print(df.color)
    objects = dbms.create_objects('DOGS', 1, 2)
    print(objects[0].color)

    dbms.create_class('DOGS', 'mod1')
    dbms.create_hierarchy('OWNER', 'pack1')