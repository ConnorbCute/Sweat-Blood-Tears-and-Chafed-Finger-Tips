#staff.py
#created by: connor cute

class Staff:
    def __init__(self, power):
        if power < 0:
            self._power = 25
        else:
            self._power = power            
        
    def getPower(self):
        return self._power
    
    def __eq__(self, staff):
        if self._power == staff.getPower():
            return True
        else:
            return False
    
    def __ne__(self, staff):
        if self._power != staff.getPower():
            return True
        else:
            return False
        
    def __repr__(self):
        return "Staff of power " + str(self._power)