from math import floor
from random import random
from queue import Queue
from threading import Thread
from time import sleep
from ElectricityDetails import ElectricityDetails


class DumpingBufferr:
    def __init__(self):
        self.queue=Queue()
    def Send(self,details):
        self.queue.put(details)
    def CheckQueue(self,historical):
        sendingItems=[]
        while(True):
            sleep(2)
            if(self.queue.qsize()>7):
                print("Getting 7 items from queue")
                for x in range(0, 7):
                    sendingItems.append(self.queue.get())
                historical.Forward(sendingItems)
                sendingItems.clear()
    
    def run(self,historical):
        t1 = Thread(target=self.CheckQueue,args=[historical])
        t1.start()
