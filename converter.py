print("Wellcome to the types converter")
current_type,value = input("Please enter two values first one for the current type(F,C,MPH,KPH,kg,stone,lbs) and the second one the value itself.").split()
print(current_type,value)
value = float(value)
match current_type:
    case 'F':
        res = (value-32)*(5/9)
        print(res,'C')
    case 'C':
        res = (value*(9/5))+32
        print(res,'F')
    case 'MPH':
        res = value*1.609344
        print(res,'KPH')
    case 'KPH':
        res = value / 1.609344
        print(res,'MPH')
    case 'kg':
        res1 = value*2.20462
        res2 = value*0.157473
        print(res1,'lbs')
        print(res2,'stone')
    case 'stone':
        res1 = value*14
        res2 = value/0.157473
        print(res1,'lbs')
        print(res2,'kg')
    case 'lbs':
        res1 = value/14
        res2 = value/2.20462
        print(res1,'stone')
        print(res2,'kg')
    case _:
        print('wrong input')