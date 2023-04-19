import random

nevek = ["Lilla", "Gina", "Soma", "Szavanna", "Viktor", "Levente", "Ferenc", "Csaba", "Delfina", "Dominik", "Zsombor", "Izaura", "Zsolt", "Norbert", "Fanni", "Dominika", "Luca", "Patrik", "Eszter", "Attila", "Anna", "Klaudia", "Krisztina", "Bence", "Csenge", "Kevin", "Martin"]
jegyek = [1, 2, 3, 4, 5]
elegedettseg = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0]

def beleir(n, j, e):
    fw = open("jegyek.txt", "w")
    for i in range(600):
        randomnevek = random.choice(nevek)
        randomjegyek = random.choice(jegyek)
        elegedettsegek = random.choice(elegedettseg)
        fw.write(randomnevek + " " + str(randomjegyek) + " " + str(elegedettsegek) + "\n")
    fw.close()


def main():
    beleir(nevek, jegyek, elegedettseg)
main()
