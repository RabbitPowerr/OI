
class Spendings():
    def __init__(self):
        pass
    
    @staticmethod
    def Calc(data):
        nmonth=12
        years= data['Years']
        total={'Online':0,'Offline':0}
        for name,x in data['Spending'].items():
            p=1.0
            n=4*nmonth
            #print(x)
            for i in range(n):
                if(x['Need_in_online']== True ):
                    total['Online']+=(x['Cost']/x['Regularyty'])*p
                if(x['Need_in_offline']== True):
                    total['Offline']=(x['Cost']/x['Regularyty'])*p
                if(i%12==0):
                    p*=(1+data['Inflation'])
        return total

    @staticmethod
    def Salary(data):
        total=0
        month=6
        p=1.0
        for x in data['num_of_subjects']:
            n = x/2
            total+=p*n*data['Salary']*month  
            p*=data['Inflation']
        return total

