from reader import Reader
if __name__ == "__main__":
    reader=Reader()
    ulaz=-1
    while(True):
        print('\nIzaberite opciju:\n\
	    1. Ispis svih user-a\n\
            2. Ispis svih merenja\n\
            3. Ispis svih merenja za odredjeni mesec\n\
            4. Ispis svih merenja za korisnika\n\
            5. Ispis svih merenja za adresu\n\
            6. Ispis svih merenja po gradu\n\
            7.Izlaz'
            )
        ulaz=int(input('Unesite komandu:'))
        if ulaz==1:
            reader.ReadAllUsers()
        elif ulaz==2:
            reader.ReadAllValues()
        elif ulaz==3:
            date=input("Unesite mesec i godinu u obliku mm/yyyy (pr:6/2022): ")
            reader.ReadAllValuesByDate(date)
        elif ulaz==4:
            id=int(input("Unesite id user-a:"))
            reader.ReadAllValuesByUserId(id)
        elif ulaz==5:
            addr=input("Unesite adresu: ")
            reader.ReadAllValuesByAddr(addr)
        elif ulaz==6:
            city=input("Unesite grad: ")
            reader.ReadAllValuesByCity(city)
        elif ulaz==7:
            exit()