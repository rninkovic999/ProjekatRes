import mysql.connector
from datetime import datetime
class Reader:
    def __init__(self):
        self.connector=mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root")
    def ReadAllUsers(self):
        #today = datetime.now()
        #date = f"{today.month}/{today.year}";
        if self.connector.is_connected():
            query="select * from res1.user"
            cursor = self.connector.cursor()
            cursor.execute(query)
            print('Users:\n')
            for u in cursor:
                print(f"UserId:{u[0]}, DeviceId:{u[1]}, Name:{u[2]}, Lastname:{u[3]}, Address: {u[4]}")
    def ReadAllValues(self):
        #today = datetime.now()
        #date = f"{today.month}/{today.year}";
        if self.connector.is_connected():
            query="select * from res1.electricity"
            cursor = self.connector.cursor()
            cursor.execute(query)
            print('Values:\n')
            for u in cursor:
                print(f"UserId:{u[0]}, DeviceId:{u[1]}, Date:{u[2]}, Address:{u[3]}, Value: {u[4]}")
    
    def ReadAllValuesByUserId(self,id):
        #today = datetime.now()
        #date = f"{today.month}/{today.year}";
        if self.connector.is_connected():
            query=f"select * from res1.electricity where userId={id}"
            cursor = self.connector.cursor()
            cursor.execute(query)
            print('Values:\n')
            for u in cursor:
                print(f"UserId:{u[0]}, DeviceId:{u[1]}, Date:{u[2]}, Address:{u[3]}, Value: {u[4]}")
    def ReadAllValuesByDate(self,date):
        if self.connector.is_connected():
            query=f"select * from res1.electricity where date='{date}'"
            cursor = self.connector.cursor()
            cursor.execute(query)
            print('Values:\n')
            for u in cursor:
                print(f"UserId:{u[0]}, DeviceId:{u[1]}, Date:{u[2]}, Address:{u[3]}, Value: {u[4]}")
    def ReadAllValuesByAddr(self,addr):
        if self.connector.is_connected():
            query=f"select * from res1.electricity where address='{addr}'"
            cursor = self.connector.cursor()
            cursor.execute(query)
            print('Values:\n')
            for u in cursor:
                print(f"UserId:{u[0]}, DeviceId:{u[1]}, Date:{u[2]}, Address:{u[3]}, Value: {u[4]}")
         


    def ReadAllValuesByCity(self,city):
        if self.connector.is_connected():
            query=f"select * from res1.electricity where address like '%{city}%'"
            cursor = self.connector.cursor()
            cursor.execute(query)
            print('Values:\n')
            for u in cursor:
                print(f"UserId:{u[0]}, DeviceId:{u[1]}, Date:{u[2]}, Address:{u[3]}, Value: {u[4]}")

                    