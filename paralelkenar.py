def sagSlas(adet):
    for i in range(int(adet)):
        print("/", end="")


def solSlas(adet):
    for i in range(int(adet)):
        print("\\", end="")

def satirAtla(adet):
    for i in range(int(adet)):
        print()

def bosluk(adet):
    for i in range(int(adet)):
        print(" ", end="")

def ustKisim(cap):
    baslangicBosluk = cap/2-1 
    for i in range(int(cap/2)):
        bosluk(baslangicBosluk-i)
        sagSlas(1)
        bosluk(i*2)
        solSlas(1)
        satirAtla(1)

def altKisim(cap):
    baslangicBosluk = cap-2
    for i in range(int(cap/2)):
        bosluk(i)
        solSlas(1)
        bosluk(baslangicBosluk - i*2)
        sagSlas(1)
        satirAtla(1)


ustKisim(10)
altKisim(10)

      