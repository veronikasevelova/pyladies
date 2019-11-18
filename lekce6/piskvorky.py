import random
symbol_hrace = input("Napiš symbol, se kterým chceš hrát - buď x nebo o: ")
while symbol_hrace != "x" and symbol_hrace != "o":
    print("Musíš napsat malým písmem znak x nebo o, nic jiného nejdeeeeee.")
    symbol_hrace = input("Napiš symbol, se kterým chceš hrát - buď x nebo o: ")
else:
    if symbol_hrace == "x":
        symbol_pocitace = "o"
    elif symbol_hrace == "o":
        symbol_pocitace = "x"

def vyhodnot(herni_pole):
    herni_pole = "".join(herni_pole)
    if "xxx" in herni_pole:
        return "x"
    elif "ooo" in herni_pole:
        return "o"
    elif "-" not in herni_pole:
        return "!"
    elif "-" in herni_pole:
        return "-"
    else:
        print("Něco je špatně.")

def tah(herni_pole1, cislo_policka, symbol):
    herni_pole1[cislo_policka] = symbol
    herni_pole1 = "".join(herni_pole1)
    return herni_pole1


def tah_hrace(herni_pole2):
    pozice_hrace = int(input("Na kterou pozici chceš hrát?"))
    while 0 > pozice_hrace >= 20 or herni_pole2[pozice_hrace] != "-":
        print("Musíš zadat celé kladné číslo od 0 do 19 a na políčko, které je volné.")
        pozice_hrace = int(input("Tak znovu: Na kterou pozici chceš hrát?"))
    else:
        return tah(herni_pole2, pozice_hrace, symbol_hrace)


def tah_pocitace(herni_pole3):
    nahodne_cislo = random.randint(0, 19)
    while herni_pole3[nahodne_cislo] != "-":
        nahodne_cislo = random.randint(0, 19)
    else:
        return tah(herni_pole3, nahodne_cislo, symbol_pocitace)


def piskvokry_1d():
    hp = "--------------------"
    hp=list(hp)
    while True:
        print(tah_hrace(hp))
    
        if vyhodnot(hp) == "x":
            print("Vyhrál jsi.")
            break
        elif vyhodnot(hp) == "o":
            print("Prohrál jsi.")
            break
        elif vyhodnot(hp) == "!":
            print("remíza")
            break
    
 
        print(tah_pocitace(hp))
        if vyhodnot(hp) == "x":
            print("Vyhrál jsi.")
            break
        elif vyhodnot(hp) == "o":
            print("Prohrál jsi.")
            break
        elif vyhodnot(hp) == "!":
            print("remíza")
            break
        

piskvokry_1d()