import random as rand

def bedenk():
    wachtwoord = []
    cijfers = int(input("How many numbers in your password?: "))
    for i in range(cijfers):
        randomnum = rand.randint(1, 9)
        wachtwoord.append(randomnum)
    print("Dit is uw nieuwe wachtwoord: {}\n".format(wachtwoord))
    bedenk()

bedenk()
