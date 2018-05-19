from wizard import Wizard
from staff import Staff
from training import battle


def main():
    staff1 = Staff(50)
    staff2 = Staff(75)
    staff3 = Staff(50)
    staff4 = Staff(-10)
    
    #Testing Staff.getPower()
    print()
    print("Testing Staff.getPower().")
    print("Test Staff.getPower(), expected 50 was", staff1.getPower())
    print("Test Staff.getPower(), expected 75 was", staff2.getPower())
    print("Test Staff.getPower(), expected 50 was", staff3.getPower())
    print("Test Staff.getPower(), expected 25 was", staff4.getPower())
    print()
    
    #Testing Staff == and !=
    print("Testing Staff == and !=.")
    print("Test Staff ==, expected True  was", staff1 == staff3)
    print("Test Staff ==, expected False was", staff2 == staff3)
    print("Test Staff !=, expected True  was", staff1 != staff4)
    print("Test Staff !=, expected False was", staff1 != staff3)
    print()
    
    #Testing Staff string representation
    print("Testing Staff string representation.")
    print('Expected "Staff of power 50." was "%s"' %  str(staff1))
    print('Expected "Staff of power 75." was "%s"' %  str(staff2))
    print()
    
    wizard1 = Wizard("Hermione", staff1)
    wizard2 = Wizard("Ron", staff2)
    
    #Testing Wizard.getName()
    print("Testing Wizard.getName()")
    print("Expected Hermione  was", wizard1.getName())
    print("Expected Ron was", wizard2.getName())
    print()
    
    #Testing Wizard.getStaff()
    print("Testing Wizard.getStaff()")
    print('Expected "Staff of power 50." was "%s"' %  str(wizard1.getStaff()))
    print('Expected "Staff of power 75." was "%s"' %  str(wizard2.getStaff()))
    print()
    
    #Testing Wizard.getPower()
    print("Testing Wizard.getPower().")
    print("Test Wizard.getPower(), expected 50 was", wizard1.getPower())
    print("Test Wizard.getPower(), expected 75 was", wizard2.getPower())
    print()
    
    #Testing Wizard string representation.
    print("Testing Wizard string representation.")
    print('Expected "Wizard Hermione with staff of power 50."\n     was "%s"' %  str(wizard1))
    print('Expected "Wizard Ron with staff of power 75."\n     was "%s"' %  str(wizard2))
    print()
    
    #some battles
    #Expected: Hermione defeats Draco
    battle(Wizard("Hermione", Staff(1000)), Wizard("Draco", Staff(250)))
    print()
    
    #Expected: Ron defeats Draco
    battle(Wizard("Draco", Staff(500)), Wizard("Ron", Staff(1500)))
    print()
    
    #Expected: It's a draw
    battle(Wizard("Hermione", Staff(1)), Wizard("Harry", Staff(1)))
    print()
    
    #Expected: Unknown!
    battle(Wizard("Harry", Staff(100)), Wizard("Hermione", Staff(100)))
    print()    
    
main()




