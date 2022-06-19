from ctypes.wintypes import HINSTANCE
from math import floor
from random import random
from queue import Queue
from threading import Thread
import mysql.connector
from ElectricityDetails import ElectricityDetails
from writer import Writerr
from dumpingBuffer import DumpingBufferr
from historical import Historical
from reader import Reader

def TestWriter():

    print("Pokusaj inicijalizacije bez Dumping Buffera:")
    try:
        writer = Writerr()
    except Exception as e:
        print(f'{e}\n')
    

    print("Pokusaj inicijalizacije sa Dumping Bufferom")
    dumpingBuffer=DumpingBufferr()
    try:
        writer = Writerr(dumpingBuffer)
    except Exception as e:
        print(f'{e}\n')
    else:
        print("Inicijalizacija uspesno izvrsena\n")
    
    print("Testiranje pokretanja Writer-a bez parametara i sa parametrom")
    try:
        writer.run()
    except Exception as e:
        print(f'{e}\n')
    else:
        print("Uspesno\n")

    try:
        dumpingBuffer = DumpingBufferr()
        writer = Writerr(dumpingBuffer)
    #    writer.run(dumpingBuffer)
    except Exception as e:
        print(f"{e}\n")
    else:
        print("Uspesno")
        print("Ako se pokrene writer.run(dumpingBuffer) bez stop ulazi u beskonacnu petlju")
    
    print("Testiranje slanja podataka u dumping Buffer")
    dumpingBuffer = DumpingBufferr()
    writer = Writerr(dumpingBuffer)

    print("Pogresni podaci")
    try:
        id = 5
        value = 52342342525
        adresa = "Svetosavska"
        detalji = ElectricityDetails(id, value, adresa)
        writer.dumpingBuffer.Send(detalji)
    except Exception as e:
        print(f'{e}\n')

    print("Dobri podaci")
    try:
        id = 7
        value = 113342342525
        detalji = ElectricityDetails(id, value)
        writer.dumpingBuffer.Send(detalji)
    except Exception as e:
        print(f'{e}\n')
    else:
        print("Uspesno poslati podaci\n")

    print("Komponenta Writer je uspesno testirana")


def TestDB():
    print("Inicijalizacija konstruktora sa parametrom")
    try:
        a = "IME PREZIME ADRESA TROSENJE"
        dBuffer = DumpingBufferr(a)
    except Exception as e:
        print(f'{e}\n')

    print("Inicijalizacija bez parametara")
    try:
        dBuffer = DumpingBufferr()
    except Exception as e:
        print(f'{e}\n')
    else:
        print("Uspesno\n")

    print("Testiranje slanja podataka iz dumpingBuffera u historical")

    dBuff = DumpingBufferr()
    items = []
    id = 5
    value = 123456789
    detalji = ElectricityDetails(id, value)
    historical = Historical()
    items.append(detalji)
    # nepotrebna je ovde inicijalizacija reda i testira se samo historical.Forward()

    try:
        historical.Forward(detalji)
    except Exception as e:
        print(f'{e}\n')

    try:
        historical.Forward(items)
    except Exception as e:
        print(f'{e}\n')
    else:
        print("Uspesno")

def TestHistorical():
    print("Inicijalizacija konstruktora sa parametrom")
    try:
        a = "IME PREZIME ADRESA TROSENJE "
        historical = Historical(a)
    except Exception as e:
        print(f'{e}\n')

    print("Inicijalizacija konstruktora bez parametara")
    try:
        historical = Historical()
    except Exception as e:
        print(f'{e}\n')
    else:
        print("Uspesno")
    print("Ostali testovi su u historicalTestovi.py")


    print("Sto se tice povezivanja sa bazom, komponente Historical i reader su u _init_ parametarski tacno definisane radi lakseg rada")
    print("Testirace se povezivanje sa netacnim i tacnim podacima\n")

    try:
        connector=mydb=mysql.connector.connect(
        host="localhost",
        user="root1",
        passwd="root")
    except Exception as e:
        print(f'{e}\n')


    try:
        connector=mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root")
    except Exception as e:
        print(f'{e}\n')
    else:
        print('Uspesno konektovani na bazu podataka')


def TestReader():
    print("Inicijalizacija konstruktora sa parametrima")
    try:
        a = "IME PREZIME"
        reader = Reader(a)
    except Exception as e:
        print(f'{e}\n')

    print("Inicijalizacija konstruktora bez parametara")
    try:
        reader = Reader()
    except Exception as e:
        print(f'{e}')
    else:
        print("Uspesno")

    print("Sto se tice povezivanja sa bazom, komponente Historical i reader su u _init_ parametarski tacno definisane radi lakseg rada")
    print("Testirace se povezivanje sa netacnim i tacnim podacima\n")

    try:
        connector=mydb=mysql.connector.connect(
        host="localhost",
        user="root1",
        passwd="root")
    except Exception as e:
        print(f'{e}\n')


    try:
        connector=mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root")
    except Exception as e:
        print(f'{e}\n')
    else:
        print('Uspesno konektovani na bazu podataka')

if __name__ == "__main__":
    ulaz = -1

    print('\nIzaberite sta zelite da testirate\n\
    1. Writer\n\
    2. Dumping Buffer\n\
    3. Historical\n\
    4. Reader\n')

    ulaz = int(input("Unesite komandu: "))
    if(ulaz==1):
        TestWriter()
    if(ulaz==2):
        TestDB()
    if(ulaz==3):
        TestHistorical()
    if(ulaz==4):
        TestReader()