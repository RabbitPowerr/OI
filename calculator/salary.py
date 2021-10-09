
from calculator.base import Base 

class Salary(Base):
    def __init__(self):
        pass

    @staticmethod
    def Calc(tsalary):
        nmonth =12
        gov_tax = 0.3
        return tsalary*nmonth*(1+gov_tax)

