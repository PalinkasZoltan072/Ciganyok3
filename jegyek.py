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
    return jegyek
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
def main():
    nevek = []
    jegyek = []
    elegedettsegek = []
    beolvas(nevek,jegyek,elegedettsegek)
    jegyszamolas(jegyek)
    osszesjegy(jegyek)
    legalacsonyabb(elegedettsegek)
main()