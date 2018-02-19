print("""

	[1] Toplama
	[2] Çıkartma
	[3] Bölme
	[4] Çarpma
	[Q] Çıkış

	""")

giris = input("Seçiminiz: ")

if giris =="1":
	x = input("ilk sayı : ")
	x = float(x)
	y = input("ikinci sayı: ")
	y = float(y)

	print("işlemin sonuçu: ", x + y)

elif giris =="2":
	x = input("ilk sayı : ")
	x = float(x)
	y = input("ikinci sayı: ")
	y = float(y)

	print("işlemin sonuçu: ", x - y)

elif giris =="3":
	x = input("ilk sayı : ")
	x = float(x)
	y = input("ikinci sayı: ")
	y = float(y)

	print("işlemin sonuçu: ", x / y)

elif giris =="4":
	x = input("ilk sayı : ")
	x = float(x)
	y = input("ikinci sayı: ")
	y = float(y)

	print("işlemin sonuçu: ", x * y)


elif giris == "5":
	x = input("Taban: ")
	y = input("Kuvet: ")

	x = float(x)
	y = int(x)

	print("işlem sonucu: ",x**y)


elif giris == "q" or giris =="Q":
	print("Çıkılıyor....")
	quit()

else:
	print("Hatalı Girdin")
	quit()