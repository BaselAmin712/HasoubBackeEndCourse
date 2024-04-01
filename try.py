def find_min_max(ls):
    ''' getting list int and returning the max value and the min value
        all elements must be from int type if not relevant message will apear
    '''
    if ls:
        if type(ls[0]) is int:
            min = ls[0]
            max = ls[0]
            for value in ls:
                try:
                    if type(value) is int:
                        if value < min:
                            min = value

                        if value > max:
                            max = value
                except Exception as e:
                    print(e)
            print(f"the min value is {min}\nthe max value is {max}")
        else:
            print(f"the first value is not integer")
        


ls = [{},2,"base"]

find_min_max(ls)

# print(type({}))
            