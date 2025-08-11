import json

class Student:
    def __init__(self, name):
        self.name = name
        self.thesis_status = ""
        self.courses_taken = ""
        self.enrollment_date = None
        self.defense_ready = False
        self.thesis_file = None
        self.defense_status = ""

pas_path="D:/UNIVERSTIY/ai project/python/ending_project/save_directory_student/pas.json"
with open(pas_path, "r") as file:
        students = json.load(file)


def stu_menu():
    for  student in students:
        if student["student_id"] == id:
            stu= Student(student["name"])
    print("*** student panel ***")
    print(f"name={stu.name}")
    

def pas_enter():

    global id
    id=input("exit = x\nenter your student ID: ")
    
    for student in students:
        if id == "x":
            return
        if student["student_id"] == id:
            print(f"hello {student['name']}")
            pas=input("enter your password: ")
            if student["password"] == pas:
                return True
            else:
                print("wrong password")
                pas_enter()
    return False
