#wizard.py
#created by: connor cute
from staff import Staff

class Wizard:
    def __init__(self, name, staff):
        self._name = name
        self._staff = staff
    
    def getName(self):
        return self._name
    
    def getStaff(self):
        return self._staff
    
    def getPower(self):
        return self._staff.getPower()
    
    def __repr__(self):
        return "Wizard " + str(self._name) + " with staff of power " + str(self._staff.getPower())
    