rodne_cislo = input("Napiš svoje rodné číslo: ")

if len(rodne_cislo) != 11:
    print(False)
else:
    cislice = rodne_cislo[0:6]
    lomitko = rodne_cislo[6]
    cislice_za_lomitkem = rodne_cislo[7:]
    cislo = cislice + cislice_za_lomitkem

    if len(cislice) != 6 and not cislice.isdigit():
        print(False)
        exit
    elif lomitko != "/":
        print(False)
        exit
    elif len(cislice_za_lomitkem) != 4 and not cislice_za_lomitkem.isdigit():
        print(False)
        exit
    elif int(cislo) % 11 != 0:
        print(False)
        exit
    else:
        rok = cislice[0:2]
        den = cislice[4:6]
        mesic = cislice[2:4]
        pohlavi = []
        if mesic[0] == '0' or mesic[0] == '1':
            pohlavi = 'muž'
        else:
            pohlavi = 'žena'

        if pohlavi == 'žena':
            mesic = int(mesic) - 50
        print("Rodné číslo jsi zadal ve správném formátu.")
        print("Tvoje datum narození je:", den+"."+ str(mesic)+".19"+ rok)
        print("Jsi:", pohlavi)


