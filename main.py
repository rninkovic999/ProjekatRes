from math import floor
from random import random
from queue import Queue
from threading import Thread
import mysql.connector
from ElectricityDetails import ElectricityDetails
from writer import Writerr
from dumpingBuffer import DumpingBufferr
from historical import Historical



if __name__ == "__main__":
    dumpingBuffer=DumpingBufferr()
    historical=Historical()
    writer=Writerr(dumpingBuffer)
    writer.run(dumpingBuffer)
    dumpingBuffer.run(historical)
