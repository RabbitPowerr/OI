import json

from calculator.calculator import *

with open('param.json') as f:
    param = json.load(f)


print(Calculator.Get_price(param))
print("total value : ebal Kirilla Cheremuskina and  our smart Teacher")