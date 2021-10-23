
class Spendings():
    def __init__(self):
        pass
    
    @staticmethod
    def Calc(data):
        nmonth=12
        total={'Online':0,'Offline':0}
        for name,x in data['Spending'].items():
            p=1.0
            n=data['Years']*nmonth
           # print(total,x)
            
            for i in range(n):
                if(x['Need_in_online']== True ):
                    total['Online']+=(x['Cost']/x['Regularyty'])*p *(1/x['Num_groups'])
                if(x['Need_in_offline']== True):
                    total['Offline']+=(x['Cost']/x['Regularyty'])*p*(1/x['Num_groups'])
               # if(i%12==0):
                #    p*=(1+data['Inflation'])
        return total

    @staticmethod
    def Salary(data):
        total=0
        month=6
        p=1.0
        for x in data['num_of_subjects']:
            n = (x)/data['Avaliable_thours'] 
            total+=p*n*data['Salary']*month  
            p*=data['Inflation']
        return total

