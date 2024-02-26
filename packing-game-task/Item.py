class Item:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    
class Devices(Item):
    def __init__(self, name, weight ,brand):
        super().__init__(name, weight)
        self.brand = brand
        self.category = "Devices"

class RegularItems(Item):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.category = "Regular Items"

class UniversalCharger(Devices):
    def __init__(self):
        super().__init__("universal charger", 12, "Lenovo")
        self.color = "Black"
        self.size = "Medium"
        self.price = 50
    def __str__(self):
        return f"name: {self.name}\nweight: {self.weight}\nbrand: {self.brand}\ncolor: {self.color}\
            \nsize: {self.size}\nprice: {self.price}\n"

class Passport(RegularItems):
    def __init__(self):
        super().__init__("Passport", 1)
        self.color = "Blue"
        self.cost = 50
    def __str__(self):
        return f"name: {self.name}\nweight: {self.weight}\ncolor: {self.color}\ncost: {self.cost}\n"
        
class Sunglasses(RegularItems):
    def __init__(self):
        super().__init__("Sunglasses", 10)
        self.color = "Black"
        self.origin = "Italy"
        self.haveCase = "yes"
    def __str__(self):
        return f"name: {self.name}\nseight: {self.weight}\ncolor: {self.color}\norigin: {self.origin}\
            \nhave case: {self.haveCase}\n"

class Sneakers(RegularItems):
    def __init__(self):
        super().__init__("Sneakers", 14)
        self.brand = "NewBalance"
        self.boughtfrom = "Spain"
        self.haveCase = "yes"
        self.new = False
    def __str__(self):
        return f"name: {self.name}\nweight: {self.weight}\nbrand: {self.brand}\nbought from: {self.boughtfrom}\
            \nhave case: {self.haveCase}\nnew: {self.new}\n"

class Smartphone(Devices):
    def __init__(self):
        super().__init__("Smartphone", 27, "Apple")
        self.operatingSystem = "IOS"
        self.storage = "128 GB"
        self.display = "AMOLED"
        self.camera = "DualLens"
        self.materials = ["lithium", "plastic"]
    def __str__(self):
        return f"name: {self.name}\nweight: {self.weight}\nbrand: {self.brand}\nOperating System: {self.operatingSystem}\
            \nstorage: {self.storage}\ndisplay: {self.display}\ncamera: {self.camera}\nmaterials: {self.materials}\n"

class Laptop(Devices):
    def __init__(self):
        super().__init__("Laptop", 60, "Dell")
        self.graphics = "NVIDIA GeForce4"
        self.storage = "512 GB SSD"
        self.RAM = "16 GB"
        self.processor = "Intel i7"
    def __str__(self):
        return f"name: {self.name}\nweight: {self.weight}\nbrand: {self.brand}\ngraphics: {self.graphics}\
            \nstorage: {self.storage}\nRAM: {self.RAM}\nprocessor: {self.processor}\n"

class Smartwatch(Devices):
    def __init__(self):
        super().__init__("Smartwatch", 44, "Samsung")
        self.display = "Touchscreen"
        self.batteryLife = "3 days"
        self.fitnessFeatures = "Heart Rate Monitor"
        self.connectivity = "Bluetooth"
    def __str__(self):
        return f"name: {self.name}\nweight: {self.weight}\nbrand: {self.brand}\ndisplay: {self.display}\
            \nbattery life: {self.batteryLife}\nfitness features: {self.fitnessFeatures}\nconnectivity: {self.connectivity}\n"
        
class Compass(RegularItems):
    def __init__(self):
        super().__init__("Compass", 4)
        self.accuracy = "high"
        self.brand = "Samsung"
        self.price = 50
        self.materials = ["iron", "plastic"]
    
    def __str__(self):
        return f"name: {self.name}\nweight: {self.weight}\naccuracy: {self.accuracy}\nbrand: {self.brand}\
            \nprice: {self.price}\nmaterials: {self.materials}\n"

