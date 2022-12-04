electricity=int(input("no of units consumed:",))
billToBepaid = 0

if electricity >= 0   and electricity < 100:
    billToBepaid= electricity*0.50
if electricity >= 100 and electricity < 150:
    billToBepaid= electricity*1.25
if electricity >= 150:
    billToBepaid= electricity*2.50
print("you should pay",billToBepaid,"Rs")