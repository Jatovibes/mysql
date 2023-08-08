import mysql.connector as sql

db = sql.connect(
    host = 'localhost',
    user = 'root',
    password = 'Jato_boi123',
    database = 'attendancesystem'
)

cursor = db.cursor()

# # cursor.execute('SELECT * FROM student')
# cursor.execute('INSERT INTO student(fname,lname,phonenumber) VALUES ("Jerry","fisher","09078645678")')
# db.commit()

# cursor.execute('SELECT * FROM student')
# cursor.execute('SELECT * FROM student WHERE phonenumber = 07046789567')

cursor.execute('UPDATE student SET' )
data = cursor.fetchall()
print(data)
