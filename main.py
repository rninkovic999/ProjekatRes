from math import floor
from random import random
from queue import Queue
from threading import Thread

from ElectricityDetails import ElectricityDetails

queue=Queue()

def DumpingBuffer():
    sendingItems=[]
    while(True):
        if(queue.qsize()>7):
            for x in range(0, 7):
                sendingItems.add(queue.get())
def Writer():
    while(True):
        id=floor(random()*10)    #generates random user id
        value=random()*1000      #generates random electricity usage value
        details=ElectricityDetails(id,value)
        queue.put(details);

if __name__ == "__main__":
    writerThread=Thread(target=Writer,args=())
    dumpingBufferThread=Thread(target=DumpingBuffer,args=())