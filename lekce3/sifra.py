plaintext = input("Co chceš zašifrovat?")
key = int(input("Napiš číslo:"))
ciphertext = ""

if key >= 0:
    for pi in plaintext:
        if 'a' <= pi <= 'z':
            c = (ord(pi)+key)
            if c > 122:
                c = c - 26
            pi = chr(c)

        elif 'A' <= pi <= 'Z': 
            c = (ord(pi)+key)
            if c > 90:
                c = c - 26            
            pi = chr(c)

        ciphertext = ciphertext + pi
            
    print("Zašifrovaná zpráva je:", ciphertext)
 
else:
    print("Musíš zadat celé kladné číslo, bejby")
    


