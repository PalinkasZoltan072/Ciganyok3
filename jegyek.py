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
def main():
    nevek = []
    jegyek = []
    elegedettsegek = []
    beolvas(nevek,jegyek,elegedettsegek)
    jegyszamolas(jegyek)
    osszesjegy(jegyek)
main()