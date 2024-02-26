from Item import *

class Bag():
    def __init__(self):
        self.items = []
        self.current_weight = 0
        self.max_weight = 80
        self.current_items = 0
        self.max_items = 6
    
    def __str__(self):
        res = ""
        i = 0
        for item in self.items:
            i += 1
            res = res + f"{i})\n" + str(item) + "\n"
        return f"items: \n{res}\n"
         
    def can_add(self,item):
        if self.current_items == self.max_items \
        or item.weight + self.current_weight > self.max_weight or self.is_in_the_bag(item):
            return False
        return True

    def is_in_the_bag(self,item):
        return item in self.items
        
    def add_item(self,item):
        if self.can_add(item):
            self.items.append(item)
            self.current_items += 1
            self.current_weight += item.weight
            print("item was added successfully.")
        else:
            print("the bag is full, or this item already in the bag, try another item or remove one.")
    
    def remove_item(self,item):
        if self.is_in_the_bag(item):
            self.items.remove(item)
            self.current_items -= 1
            self.current_weight -= item.weight
            print("item was deleted successfully.")
        else:
            print("the item is not in the bag.")

all_items = [UniversalCharger(), Passport(), Sunglasses(), Sneakers(), Smartphone(),
 Laptop(), Smartwatch(), Compass()]

def print_all_items():
    i = 0
    for item in all_items:
        i += 1
        print(f"{i}) {item.name}.")

player_bag = Bag()

while True:
    print("your bag:\n", player_bag)
    if input("do you want to edit your bag? yes/no?") == "yes":
        if input("do you want to add item? yes/no?") == "yes":
            print_all_items()
            item_num = int(input("enter item number:"))
            player_bag.add_item(all_items[item_num - 1])
        if input("do you want to remove item? yes/no?") == "yes":
            print_all_items()
            item_num = int(input("enter item number:"))
            player_bag.remove_item(all_items[item_num - 1])
    else:
        print("your bag:\n", player_bag)
        break
