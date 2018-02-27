karakter = {"ad" : "Yasin",
    "güç" : 100,
    "silah" : "Taramalı biksi",
    "can" : 100 }

karakter2 = {"ad" : "yakup",
    "güç" : 70,
    "silah" : "kucuk tabança",
    "can" :100}


def vur(vuran:dict,vurulan:dict):
    eksilen = vuran["güç"]
    vurulan["can"] = vurulan["can"] - eksilen

    vur(karakter,karakter2)
    vur(karakter2,karakter)

print("karakter 1 can : {}".format(karakter["can"]))
print("karakter 2 can : {}".format(karakter["can"]))