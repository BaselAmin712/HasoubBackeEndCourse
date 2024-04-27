class Student():
    def __init__(self, name, id, age, classes):
        self.name = name
        self.id = id
        self.age = age
        self.classes = classes

    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id,
            "age": self.age,
            "classes": self.classes,
        }
    
    def cmp_students(dict_student1, dict_student2):
        if dict_student1["id"] == dict_student2["id"]:
            return True
        return False