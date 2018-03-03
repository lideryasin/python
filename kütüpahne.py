import os
kitapListe = list()

menu = """

[1] Kitap Ekle
[2] Kitap Al
[3] Tümünü Listele
[Q] Çıkış

"""

def kitaEkle(kitap:tuple,liste:list):
    liste.append(kitap)
    print("Kitap Eklendi ")
    print("Ana Menüye Göndemek için 'enter'e Basınız")
    input()


def kontrol(kitap:tuple,liste:list):
    if kitap in liste:
        return True

    else:
        return False


def kitapCıkar(kitap:tuple,liste:list):
    if kontrol(kitap,liste):
        liste.remove(kitap)
        print("kitap Çıkartırıldı")
        print("Ana Menüye Göndemek için 'enter'e Basınız")
        input()

    else:
        print("Aratığınız kitap mevcut değildir!")
        print("Ana Menüye Göndemek için 'enter'e Basınız")
        input()


def listele(liste:list):
    for i in liste:
        print("kitapın Adı : {}   Yazar : {}".format(i["0"],i["1"]))

    print("Ana Menüye Göndemek için 'enter'e Basınız")
    input()


while  True:
    os.system("cls")
    print(menu)

    secim = input("işleminizi Seçiniz : ")

    if secim =="1":
        kitap_isim = input("Kitabını İsimi Giriniz") 
        kitap_yazar = input("Yazarın İsmini Giriniz")
        kitap = (kitap_isim,kitap_yazar)
        kitaEkle(kitap,kitapListe)

    elif secim =="2":
        kitap_isim = input("Kitabını İsimi Giriniz") 
        kitap_yazar = input("Yazarın İsmini Giriniz")
        kitap = (kitap_isim,kitap_yazar)
        kitapCıkar(kitap,kitapListe)

    elif secim =="3":
        listele(kitapListe)

    elif secim =="q" or secim =="Q":
        print("Yine Bekleriz")
        quit()
    else:
        print("Hatalı Giriş Yaptınız")