import json

pas_path="D:/UNIVERSTIY/ai project/python/ending_project/save_directory_student/pas.json"


def stu_menu():
    print("*** student panel ***")
    

def pas_enter():

    with open(pas_path, "r") as file:
        students = json.load(file)

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
