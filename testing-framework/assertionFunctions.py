def is_in_list(lst, value):
    is_exist = False
    for x in lst:
        if isinstance(x, list):
            is_exist = is_in_list(x, value)
        else:
            if x == value:
                is_exist = True
        if is_exist:
            return is_exist
    return is_exist

def is_in_dict_keys(d, value):
    is_exist = False
    keys = d.keys()
    for key in keys:
        if isinstance(key, dict):
            is_exist = is_in_dict_keys(key, value)
        else:
            if key == value:
                is_exist = True
        if is_exist:
            return is_exist
    return is_exist

def is_in_dict_values(d, x):
    is_exist = False
    values = d.values()
    for value in values:
        if isinstance(value, dict):
            is_exist = is_in_dict_values(value, x)
        else:
            if value == x:
                is_exist = True
        if is_exist:
            return is_exist
    return is_exist

likes = {"color": "blue", "fruit": "apple", "pet": "dog"}
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter',[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 'Saturn', 'Uranus', 'Neptune']

if is_in_list(planets, 19):
    print("was found")
else:
    print("not found")