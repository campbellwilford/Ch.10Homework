import random

class Employee:
    
    def __init__(self,name,ID, department, job,salary):
        self.__name = name
        self.__ID = ID
        self.__department = department
        self.__job = job
        self.__salary = salary 

    
    def getName(self):
        return self.__name
    
    def getID(self):
        return self.__ID

    def getDepartment(self):
        return self.__department
    
    def getJob(self):
        return self.__job
    
    def getSalary(self):
        return self.__salary


