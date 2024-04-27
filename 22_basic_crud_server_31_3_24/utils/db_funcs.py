import json

def load_db():
    with open("data/school.json") as school_file:
        return json.load(school_file)

def add_item_to_db(item, cmp_function):
    with open("data/school.json") as school_file:
        data = json.load(school_file)
    
    if is_item_exists(data, item, cmp_function):
        return False

    data.append(item)

    with open("data/school.json", "w") as school_file:
        json.dump(data, school_file)
    
    return True

def is_item_exists(items, item_to_check, cmp_function):
    for item in items:
        if cmp_function(item, item_to_check):
            return True
    return False