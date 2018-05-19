#training.py
#created by: connor cute

from staff import Staff
from wizard import Wizard
from random import randint

def battle(wizard1, wizard2):
    
    print("Wizard %s has a staff of power %d." % (wizard1.getName(), wizard1.getPower()))
    print("Wizard %s has a staff of power %d." % (wizard2.getName(), wizard2.getPower()))
    
    wiz1Power = wizard1.getPower()
    wiz2Power = wizard2.getPower()
    
    wiz1Ranpow = randint(1, wiz1Power)
    wiz2Ranpow = randint(1, wiz2Power)
    
    print("%s battles with %d power." % (wizard1.getName(), wiz1Ranpow))
    print("%s battles with %d power." % (wizard2.getName(), wiz2Ranpow))
    
    wiz1finalPow = wiz1Power - wiz2Ranpow
    wiz2finalPow = wiz2Power - wiz1Ranpow
    
    if wiz1finalPow > wiz2finalPow:
        print("%s is left with %d power." % (wizard1.getName(), wiz1finalPow))
        if wiz2finalPow < 0:
            print("%s is left with 0 power." % wizard2.getName())
            print("%s defeats %s." % (wizard1.getName(), wizard2.getName()))
        else:
            print("%s is left with %d power." % (wizard2.getName(), wiz2finalPow))
            print("%s defeats %s." % (wizard1.getName(), wizard2.getName()))
            
    if wiz1finalPow < wiz2finalPow:
        if wiz1finalPow < 0:
            print("%s is left with 0 power." % wizard1.getName())
            print("%s is left with %d power." % (wizard2.getName(), wiz2finalPow))
            print("%s defeats %s." % (wizard1.getName(), wizard2.getName()))
        else:
            print("%s is left with %d power." % (wizard1.getName(), wiz1finalPow))
            print("%s is left with %d power." % (wizard2.getName(), wiz2finalPow))
            print("%s defeats %s." % (wizard2.getName(), wizard1.getName()))
        
    if wiz1finalPow == wiz2finalPow:
        if wiz2finalPow < 0 or wiz1finalPow < 0:
            print("%s is left with 0 power." % wizard1.getName())
            print("%s is left with 0 power." % wizard2.getName())
            print("It's a draw.")
        else:
            print("%s is left with %d power." % (wizard1.getName(), wiz1finalPow))
            print("%s is left with %d power." % (wizard2.getName(), wiz2finalPow))
            print("It's a draw.")
    
    return battle