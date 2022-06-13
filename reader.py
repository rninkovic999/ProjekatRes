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
         
            # for i in items:
            #     flag=False
            #     cursor = self.connector.cursor()
            #     cursor.execute(f"select * from res1.user where id={i.userId}")
            #     user=cursor.fetchone()
            #     print(user)
            #     if(user==None):
            #         return
            #     else:
            #         cursor.execute(f"select * from res1.electricity where userId={i.userId}")
            #         if(cursor==None):
            #             print(f"ELECTRICITY FOR USER {user[0]} NOT FOUND - ADDING INITIAL")
            #             query="insert into res1.electricity (userId,deviceId,date,address,value) values (%s,%s,%s,%s,%s)"
            #             val=(user[0],user[1],date,user[4],i.value)
            #             cursor.execute(query,val)
            #             self.connector.commit()
            #             continue
            #         for row in cursor:
            #             print(row)
            #             if(row[2]==date):
            #                 print(f"USER {user[0]} AND DATE {date} FOUND - UPDATING VALUE")
            #                 newValue=i.value+float(row[4])
            #                 query="update res1.electricity set value=%s \
            #                  where userId=%s and date=%s"
            #                 val=(newValue,user[0],date);
            #                 cursor.execute(query,val)
            #                 self.connector.commit()
            #                 flag=True
            #                 break
            #         if(flag==False):
            #             print(f"DATE {date} FOR USER {user[0]} NOT FOUND - ADDING NEW")
            #             query="insert into res1.electricity (userId,deviceId,date,address,value) values (%s,%s,%s,%s,%s)"
            #             val=(user[0],user[1],date,user[4],i.value)
            #             cursor.execute(query,val)
            #             self.connector.commit()
                        
                    