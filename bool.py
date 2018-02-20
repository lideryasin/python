

"""

and ---- ve 
or ---- veya
not ----- değil

"""

sayi = int(input("Sayi Gir: "))

sayi2 = int(input("Sayi2 Gir: "))

if sayi > 5:
	if sayi % 2 == 0:
		print("Doğru")


//kolay yolu

if sayi > 5 and sayi % 2 == 0: //and (ve demek)
	print("doğru")


if sayi > 5 or sayi2 == 5: // veya demek
	print("doğru")

else:
	print("En az girisin 5 olması lazım!")


if not bool(isim):
	print("Doğru!") // değer giresen doğru yazar ama girmezsen retrun yapar


