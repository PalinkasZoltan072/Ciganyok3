from random import randint
nevek = ["Zsombor","viki","Gina","Máté","Soma","Feri","Lilla","Levi","Pista","Dominik","Zoli","Viktor"]
print("írjon majd be egy számot(listahossz) min 1, max 500")
n = int(input())
m = len(nevek)
véletlennév = []
véletlenjegy = []
for i in range(n):
    a = randint(0,m)
    véletlennév.append(nevek[a])

