from math import floor
from random import random
import random
from queue import Queue
from threading import Thread
from ElectricityDetails import ElectricityDetails
from time import sleep


class Writerr:
    def __init__(self, dumpingBuf):
        self.id=0
        self.dumpingBuffer=dumpingBuf
    def Generate(self):
        while(True):
            sleep(random())
            id=random.randint(0, 9)   #generates random user id
            value=random()*1000      #generates random electricity usage value
            details=ElectricityDetails(id,value)
            print(f"New value-> userId:{id}  value:{value}")
            self.dumpingBuffer.Send(details)
           # queue.put(details)
    def run(self,dumpingBuffer):
        t1 = Thread(target=self.Generate)
        t1.start()
