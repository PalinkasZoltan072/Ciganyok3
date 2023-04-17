def beolvas(nevek, jegyek, elegedettsegek):
    fr = open("jegyek.txt," "r")
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
    fr.close()

def main():
    beolvas(nevek, jegyek, elegedettsegek)
main()