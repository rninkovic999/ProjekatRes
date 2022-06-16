import mysql.connector
from datetime import datetime
class Historical:
    def __init__(self):
        self.connector=mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root")
    def Forward(self,items):
        today = datetime.now()
        date = f"{today.month}/{today.year}";
        if self.connector.is_connected():
            for i in items:
                flag=False
                cursor = self.connector.cursor()
                cursor.execute(f"select * from res1.user where id={i.userId}")
                user=cursor.fetchone()
                print(user)
                if(user==None):
                    return
                else:
                    cursor.execute(f"select * from res1.electricity where userId={i.userId}")
                    if(cursor==None):
                        print(f"ELECTRICITY FOR USER {user[0]} NOT FOUND - ADDING INITIAL")
                        query="insert into res1.electricity (userId,deviceId,date,address,value) values (%s,%s,%s,%s,%s)"
                        val=(user[0],user[1],date,user[4],i.value)
                        cursor.execute(query,val)
                        self.connector.commit()
                        continue
                    for row in cursor:
                        print(row)
                        if(row[2]==date):
                            print(f"USER {user[0]} AND DATE {date} FOUND - UPDATING VALUE")
                            newValue=i.value+float(row[4])
                            query="update res1.electricity set value=%s \
                             where userId=%s and date=%s"
                            val=(newValue,user[0],date);
                            cursor.execute(query,val)
                            self.connector.commit()
                            flag=True
                            break
                    if(flag==False):
                        print(f"DATE {date} FOR USER {user[0]} NOT FOUND - ADDING NEW")
                        query="insert into res1.electricity (userId,deviceId,date,address,value) values (%s,%s,%s,%s,%s)"
                        val=(user[0],user[1],date,user[4],i.value)
                        cursor.execute(query,val)
                        self.connector.commit()
                        
                    