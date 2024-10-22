import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    password="1234",
    port="3306",
    database="q11"
)

cursor = mydb.cursor()

cursor.execute('''
    insert into employeedetails(name, department, position, salary) values
    ('a','a','a',1),
    ('b','b','b',2);
''')

mydb.commit()