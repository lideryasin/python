

x = "abc"

if "b" in x:
	print("mevcut") //b harfi varsa mevcut yazacak yoksa bu harf yok diyecek

else:
	print("Bu harf yok Birader!")


	// i ikinci örnek not ile 

if "a" not in x: 
	print("a harfi yok hemşerim başka bir şey dene ")

else:
	print("a harf var buravo")


	// parola işleminde kullanma 

	parola = input("Parola Belirle")

if "_" not in parola:
	print("'_' (alt cizgi) kullanamazsın kardeş ")