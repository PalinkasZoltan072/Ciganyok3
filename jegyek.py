def beolvas(nevek, jegyek, elegedettsegek):
    fr = open("jegyek.txt", "r")
    sor = fr.readline()
    while sor != "":
        sor = sor.split()
        nev = sor[0].strip()
        jegy = int(sor[1])
        elegedettseg = float(sor[2])
        nevek.append(nev)
        jegyek.append(jegy)
        elegedettsegek.append(elegedettseg)
        sor = fr.readline()
    #print(jegyek)
    fr.close()


def jegyszamolas(jegyek):
    f = len(jegyek)
    z = 0
    for i in range(f):
        if jegyek[i] == 5:
            z += 1
    print(z,"darab ötös van")
    return z


def osszesjegy(jegyek):
    f = len(jegyek)
    db = 0
    for i in range(f):
        db += jegyek[i]
    print(db,"az összes jegy összege")
    return db


def legalacsonyabb(elegedettsegek):
    kivalogat = []
    f = len(elegedettsegek)
    for i in range(f):
        if elegedettsegek[i] <= 5:
            kivalogat.append(elegedettsegek[i])
    print("Az 5 alatti elégedetségek ezek:","\n",kivalogat)
    return kivalogat

def kereses(nevek, jegyek):
    x = int(input("Ki kapott elsőnek ilyen jegyet: "))
    n = len(jegyek)
    i = 0
    while i < n and not(x == jegyek[i]):
        i += 1
    if i < n:
        print("Elsőnek", nevek[i], "kapott ilyen jegyet, ami=",x)


def maxi(nevek, elegedettsegek):
    maxim = 0
    for i in range(1, len(elegedettsegek)):
        if elegedettsegek[i] > elegedettsegek[maxim]:
            maxim = i   
    print(nevek[maxim], elegedettsegek[maxim])

def megszamolas(nevek:list):
    u = input("egy nevet kérek a listából:")
    l = 0
    for i in range(len(nevek)):
        if nevek[i] == u:
            l += 1
     
    print(u, "nevu embernek", l, "darab jegye van")

def top3(nevek, jegyek, nevek2, lista):
    Li = 0
    Gi = 0
    So = 0
    Sza= 0
    Vi = 0
    Le = 0
    Fe = 0
    Csa= 0
    De = 0 
    Do1= 0
    Zsom=0 
    Iz = 0
    Zsol=0
    No = 0
    Fa = 0
    Do2= 0
    Lu = 0
    Pa = 0
    Esz= 0
    At = 0
    An = 0
    Kl = 0
    Kr = 0
    Be = 0
    Cse= 0
    Ke = 0
    Ma = 0
    for i in range(len(nevek)):
        if nevek[i] == "Lilla" and jegyek[i] == 1:
            Li += 1
        elif nevek[i] == "Gina" and jegyek[i] == 1:
            Gi += 1
        elif nevek[i] == "Soma" and jegyek[i] == 1:
            So += 1
        elif nevek[i] == "Szavanna" and jegyek[i] == 1:
            Sza += 1
        elif nevek[i] == "Viktor" and jegyek[i] == 1:
            Vi += 1
        elif nevek[i] == "Levente" and jegyek[i] == 1:
            Le += 1
        elif nevek[i] == "Ferenc" and jegyek[i] == 1:
            Fe += 1
        elif nevek[i] == "Csaba" and jegyek[i] == 1:
            Csa += 1
        elif nevek[i] == "Delfina" and jegyek[i] == 1:
            De += 1
        elif nevek[i] == "Dominik" and jegyek[i] == 1:
            Do1 += 1
        elif nevek[i] == "Zsombor" and jegyek[i] == 1:
            Zsom += 1
        elif nevek[i] == "Izaura" and jegyek[i] == 1:
            Iz += 1
        elif nevek[i] == "Zsolt" and jegyek[i] == 1:
            Zsol += 1
        elif nevek[i] == "Norbert" and jegyek[i] == 1:
            No += 1
        elif nevek[i] == "Fanni" and jegyek[i] == 1:
            Fa += 1
        elif nevek[i] == "Dominika" and jegyek[i] == 1:
            Do2 += 1
        elif nevek[i] == "Luca" and jegyek[i] == 1:
            Lu += 1
        elif nevek[i] == "Patrik" and jegyek[i] == 1:
            Pa += 1
        elif nevek[i] == "Eszter" and jegyek[i] == 1:
            Esz += 1
        elif nevek[i] == "Attila" and jegyek[i] == 1:
            At += 1
        elif nevek[i] == "Anna" and jegyek[i] == 1:
            An += 1
        elif nevek[i] == "Klaudia" and jegyek[i] == 1:
            Kl += 1
        elif nevek[i] == "Krisztina" and jegyek[i] == 1:
            Kr += 1
        elif nevek[i] == "Bence" and jegyek[i] == 1:
            Be += 1
        elif nevek[i] == "Csenge" and jegyek[i] == 1:
            Cse += 1
        elif nevek[i] == "Kevin" and jegyek[i] == 1:
            Ke += 1
        elif nevek[i] == "Martin" and jegyek[i] == 1:
            Ma += 1
        
    for i in range(len(nevek2)):
        if 
        




def main():
    lista = []
    nevek = []
    jegyek = []
    nevek2 = ["Lilla", "Gina", "Soma", "Szavanna", "Viktor", "Levente", "Ferenc", "Csaba", "Delfina", "Dominik", "Zsombor", "Izaura", "Zsolt", "Norbert", "Fanni", "Dominika", "Luca", "Patrik", "Eszter", "Attila", "Anna", "Klaudia", "Krisztina", "Bence", "Csenge", "Kevin", "Martin"]
    elegedettsegek = []
    beolvas(nevek,jegyek,elegedettsegek)
    jegyszamolas(jegyek)
    osszesjegy(jegyek)
    legalacsonyabb(elegedettsegek)
    kereses(nevek, jegyek)
    maxi(nevek, elegedettsegek)
    megszamolas(nevek)
    top3(nevek, jegyek, nevek2, lista)
    
main()