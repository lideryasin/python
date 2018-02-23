def ucgenmi(a,b,hipotenüs):
    if a**2 + b**2 == hipotenüs**2:
        return "Bu Bir Üçgendir!"

    else:
        return "bu bir üçgen değildir!"

print(ucgenmi(2,5,7))