zvirata = ['pes', 'kočka', 'králík', 'had', 'andulka' ]
zvirata2 = ['andulka', 'medvěd', 'kočka', 'pes']

'''for i in zvirata:
    if len(i) < 5:
        print(i)'''

'''for i in zvirata:
    if i[0] == 'k' :
        print(i)'''

'''otazka = str(input("Napiš nějaké zvíře: "))

if otazka in zvirata:
    print(True)
else:
    print(False)'''

'''prunik = []
for i in zvirata:
    if i in zvirata2:
        prunik.append(i)

print(prunik)'''

'''rozdil = []
for i in zvirata2:
    if i not in zvirata:
        rozdil.append(i)
print(rozdil)'''

'''zvirata.sort()
print(zvirata)'''

'''print(sorted(zvirata))
print(zvirata)'''

slovnik = {}
for i in zvirata:
    key = i[1:]
    slovnik[key] = i

zvirata_serazena = []
for i in sorted(slovnik):
    zvirata_serazena.append(slovnik[i])
print(zvirata_serazena)

