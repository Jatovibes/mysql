import datetime
import mysql.connector as sql
from dotenv import load_dotenv
import os

load_dotenv('password.env')

user = os.environ.get('user')
password = os.environ.get('password')
host = os.environ.get('host')



class StudentNotFound(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Student:
    def __init__(self, id, fname, lname, phonenumber):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.phonenumber = phonenumber
    
    def __str__(self) -> str:
        return self.fname

class DB:
    def __init__(self) -> None:
        self.__db = sql.connect(
            host=host,
            user=user,
            password=password,
            database='attendancesystem'
        )
        self.studentT = 'student'
        self.presentT = 'present'
        self.__cursor = self.__db.cursor()

    def add_new_student(self, student: Student):
        self.__cursor.execute(f'INSERT INTO {self.studentT} (fname, lname, phonenumber) VALUES (%s, %s, %s)', (student.fname, student.lname, student.phonenumber))      
        self.__db.commit()
    
    def all_student(self):
        self.__cursor.execute(f'SELECT * FROM {self.studentT}')
        return self.__cursor.fetchall()
    
    def update_fname(self, fname, id):
        self.__cursor.execute(f'UPDATE student SET fname = "{fname}" WHERE id = {id}')
        self.__db.commit()
        

    def update_lname(self, lname, id):
        self.__cursor.execute(f'UPDATE student SET lname = "{lname}" WHERE id = {id}')
        self.__db.commit()
        
    def update_phonenumber(self, phonenumber, id):
        self.__cursor.execute(f'UPDATE student SET phonenumber = "{phonenumber}" WHERE id = {id}')
        self.__db.commit()    

    def get_present(self, sid: id):
        self.__cursor.execute(f'INSERT INTO {self.presentT}  VALUES (%s,%s,%s) (sid.1,2,3')





class AttendanceSystem:
    def __init__(self) -> None:
        self.db = DB()
        self.attendance_record = {}
        self.student_record = []
        

    def add_student(self, student: Student):
        for student in self.db.all_student():
            if student[1] == student.fname and student[2] == student.lname:
                raise Exception
        else:
            self.db.add_new_student(student)
            print('success')

    def display_student(self):
        return self.db.all_student()

    def update_fname(self, fname , id):
        self.db.update_fname(fname,id)
        print('Fname updated')
    
    def update_lname(self, lname, id):
        self.db.update_lname(lname,id)
        print('Lname updated')

    def update_phonenumber(self,phonenumber,id):
        self.db.update_phonenumber(phonenumber,id)
        print('Phonenumber has been updated')
  
    def mark_attendance(self, id):
        date = datetime.datetime.now().date()
        for student in self.student_record:
            if student.id == id:
                if date in self.attendance_record.keys():
                    self.attendance_record[date].append(student)
                else:
                    self.attendance_record[date] = [student]
                break
        else:
            raise StudentNotFound     
        


    
        
# student1 = Student(1, 'Henry', 'Scott', '090909789')
# student2 = Student(2, 'James', 'John', '234566')


manager = AttendanceSystem()
manager.update_fname('Ashley', 10)

