from math import floor
from random import random
from queue import Queue
from threading import Thread
import mysql.connector
from ElectricityDetails import ElectricityDetails
from writer import Writerr
from dumpingBuffer import DumpingBufferr
from historical import Historical
###upit za insertovanje usera u bazu
# insert into res1.user (id,meterId,name,lastname,address) values (10,10,'Marko','Markovic','Puskinova 21')
queue=Queue()

# def DumpingBuffer():
#     sendingItems=[]
#     while(True):
#         if(queue.qsize()>7):
#             for x in range(0, 7):
#                 sendingItems.add(queue.get())
# def Writer():
#     while(True):
#         id=floor(random()*10)    #generates random user id
#         value=random()*1000      #generates random electricity usage value
#         details=ElectricityDetails(id,value)
#         queue.put(details);

if __name__ == "__main__":
    dumpingBuffer=DumpingBufferr()
    historical=Historical()
    writer=Writerr(dumpingBuffer)
    writer.run(dumpingBuffer)
    dumpingBuffer.run(historical)
    #historical=Historical()
    #writer.run(dumpingBuffer)
    #dumpingBuffer.run(historical)
    print("hi")
    #writerThread=Thread(target=runWriter,args=[writer])
    # print("hi")
    # dumpingBufferThread=Thread(target=dumpingBuffer.CheckQueue,args=[historical])
    # print("hi")
    # writerThread.start()
    # dumpingBufferThread.start()
    # mydb=mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     passwd="root",
    #     database='res1'
    # )
    # print(mydb)
    # if mydb.is_connected():
    #     db_Info = mydb.get_server_info()
    #     print("Connected to MySQL Server version ", db_Info)
    #     cursor = mydb.cursor()
    #     #cursor.execute("insert into res1.user (id,meterId,name,lastname,address) values (2,2,'Maya','Miller',' 6755 Downtown west street')")
    #     #mydb.commit()
    #     cursor.execute("select * from res1.user where id=1")
    #     print(cursor.fetchone())
        #record = cursor.fetchone()
        #print("You're connected to database: ", record)
   # writerThread=Thread(target=Writer,args=())
    #dumpingBufferThread=Thread(target=DumpingBuffer,args=())