from calculator.Spendings import Spendings 

class Calculator():
    def __init__(self):
        pass

    @staticmethod
    def Get_price(data):
        total=Spendings().Calc(data)
        cost_t= Spendings.Salary(data)
        #print(total)
        total['Online']+=cost_t
        total['Offline']+=cost_t
        #print(total)
        total['Online']/=data['Num_students']
        total['Offline']/=data['Num_students']
        return total
        
