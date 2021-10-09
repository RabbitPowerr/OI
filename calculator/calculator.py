from calculator.salary import Salary 

class Calculator():
    def __init__(self):
        pass

    @staticmethod
    def Get_price(data):
        cost = Salary.Calc(data['Salary'])
        return cost / data['Num_students']
