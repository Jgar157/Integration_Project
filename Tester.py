from PlayerBase import PlayerBase

# Jairo Garciga
# This is a tester class that runs all of the other classes.

class Tester:

    inputed_name = input("What is your name?")
    A = PlayerBase(inputed_name)
    print("Hello, ", A.getPlayerName()+".")