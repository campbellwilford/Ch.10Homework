import random

class PayrollDeduction:
    
    def __init__(self,description, date, charge_amount,ID):
        self.__description = description
        self.__date = date
        self.__charge_amount = charge_amount
        self.__ID = ID

    def getdescription(self):

        return self.__description
        
