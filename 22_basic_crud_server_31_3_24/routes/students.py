from fastapi import APIRouter
import utils.db_funcs as fns
from pydantic import BaseModel
from student import Student

router = APIRouter()

@router.get("/students/")
def get_all_students():
    all_students_json = fns.load_db()
    return all_students_json
    
@router.get("/get-student/{student_id}")
def get_student_by_id(student_id:str):
    all_students_json = fns.load_db()
    for student in all_students_json:
        if student["id"] == student_id:
            return student

@router.get("/get-students-in-class/{class_name}")
def get_students_in_class(class_name:str):
    students_in_class = []
    all_students_json = fns.load_db()
    for student in all_students_json:
        if class_name in student["classes"]:
            students_in_class.append(student)
    return students_in_class

class Item(BaseModel):
    name: str
    id: str
    age: int
    classes: list

@router.post("/add-student/")
def add_student(item: Item):
    if fns.add_item_to_db(item.dict(), Student.cmp_students):
        return f"student with id: {item.id} was added"
    else:
        return "Item already exists!"
    