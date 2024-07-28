import random as rand
wachtwoord = []

def bedenk():
    cijfers = int(input("Hoeveel cijfers moet het wachtwoord hebben?: "))
    for i in range(cijfers):
        randomnum = rand.randint(1, 9)
        wachtwoord.append(randomnum)
    tuple(wachtwoord)
    print("Dit is uw nieuwe wachtwoord: {}\n".format(wachtwoord))
    bedenk()

bedenk()