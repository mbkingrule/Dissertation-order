import json
from datetime import datetime

def get_prof_c(c_id):
    '''convert course id to professor id'''
    for course in courses:
        course["course_id"] == c_id
        return course["professor_id"]
    
class Student_c:
    '''make class for student and request method'''
    def __init__(self, id):
        self.id = id
        self.course_id = None
        self.course_req_T= None
        self.course_req_P= None
        self.accepted= None

    def enroll_course(self, course_id):
        self.course_id = course_id
        self.course_req_T = str(datetime.now())
        self.course_req_P = get_prof_c(course_id)
    def to_dict(self):
        return{
            "name": self.id,
            "req_course": self.course_id,
            "time_req": self.course_req_T,
            "to_prof": self.course_req_P,
            "status": self.accepted
        }

'''intruduce path of json files'''
pas_path_stu="save_directory_student/pas.json"
course_path="main_directory/courses.json"
pas_path_prof="save_directory_tech/pas.json"
req_path="main_directory/course_req.json"

'''open json files for use in function'''
with open(pas_path_stu, "r") as file:
        students = json.load(file)
with open(pas_path_prof, "r") as file:
        professor = json.load(file)
with open(course_path, "r") as file:
    courses = json.load(file)



def id_name_prof(id):
    '''convert prof id to name professor'''
    for prof in professor:
        if prof["ID"] == id:
            return prof["name"]
    return "unknown"

def pas_enter():
    '''check password for enter to student panel'''
    while True:
        student_id = input("Type 'x' to exit\nEnter your student ID: ")
        if student_id.lower() == "x":
            return None

        for student in students:
            if student["student_id"] == student_id:
                print(f"Hello {student['name']}")
                password = input("Enter your password: ")
                if student["password"] == password:
                    return student_id
                else:
                    print("Wrong password, try again.")
                    break
        else:
            print("Student ID not found, try again.")


def get_course(student_id):
    '''student request ending course here'''
    counter=1
    for course in courses:
        if course["capacity"] == course["enrolled"]:
            continue
        print("\n")
        print(f"{counter}course\n"
              f"course ID: {course["course_id"]}\n"
              f"title: {course["title"]}\n"
              f"professor: {id_name_prof(course['professor_id'])}\n"
              f"year: {course["year"]}\n"
              f"semester: {course["semester"]}\n"
              f"capacity: {course["capacity"]}\n"
              f"enrolled: {course["enrolled"]}\n"
              f"units: {course["units"]}\n"
              f"sessions: {course["sessions"]}\n"
              f"resources: {course["resources"]}")
    print("select the course you want\nenter the ID course: ")
    selected_course=input()
    stu=Student_c(student_id)
    stu.enroll_course(selected_course)
    try:
        with open(req_path, "r") as file:
            request_l = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        request_l = []
    request_l.append(stu.to_dict())

    with open(req_path, "w") as file:
        json.dump(request_l, file, indent=4)

    

def stu_menu(student_id):
    '''main menu for student'''
    for student in students:
        if student["student_id"] == student_id:
            print("*** Student Panel ***")
            print(f"Name: {student["name"]}")
            break
    print("1-choose course\n2-choosing status\n3-exit to main")
    choice= input()
    if choice == '1':
        get_course(student_id)
    elif choice == '3':
        return None
