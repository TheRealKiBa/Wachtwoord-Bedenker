import random as rand

def bedenk():
    cijfers = int(input("How many numbers in your password?: "))
    wachtwoord = [rand.randint(1,9) for i in range(cijfers)]
    print("Dit is uw nieuwe wachtwoord: {}\n".format(wachtwoord))
    bedenk()
bedenk()
