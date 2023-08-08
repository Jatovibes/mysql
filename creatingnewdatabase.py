import mysql.connector as sql

db = sql.connect(
    host = 'localhost',
    user = 'root',
    password = 'Jato_boi123'
)

cursor = db.cursor()

cursor.execute('DROP DATABASE attendancemanager')
cursor.execute('')
db.commit()