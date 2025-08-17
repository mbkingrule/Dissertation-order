import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
import tkinter as tk
from tkinter import filedialog
import shutil
import os

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
            "status": self.accepted,
            "req_id": (self.id+self.course_id)
        }

'''intruduce path of json files'''
pas_path_stu="save_directory_student/pas.json"
course_path="main_directory/courses.json"
pas_path_prof="save_directory_tech/pas.json"
req_path="main_directory/course_req.json"
project_path="main_directory/projects_directory"

'''open json files for use in function'''
with open(pas_path_stu, "r") as file:
    students = json.load(file)
with open(pas_path_prof, "r") as file:
    professor = json.load(file)
with open(course_path, "r") as file:
    courses = json.load(file)
with open(req_path, "r") as file:
    requests= json.load(file)



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
    with open(req_path, "r") as file:
        requests= json.load(file)
    counter=1
    for req in requests:
        if student_id == req["name"]:
            if req["status"] == "accepted" or req["status"] is None:
                print("\nyou had taken a course\ngo to status page!")
                return None
            elif req["status"] == "rejected":
                continue
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
        counter+=1
    print("select the course you want\nenter the ID course: ")
    selected_course=input()
    for course in courses:
        if course["course_id"] == selected_course: 
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
            return None
    print("course id you entered is invalid")
    return None

def get_status(stu_id):
    with open (req_path, "r") as file:
        req_l = json.load(file)
    for req in req_l:
        if req["name"] == stu_id:
            if req["status"] != None:
                print(f"\nyour request is {req["status"]}")
            else:
                print("\nyour requst pending contact your prof!")
    return None

def passed_time_3m(str_time):
    time= datetime.strptime(str_time, "%Y-%m-%d %H:%M:%S.%f")
    now= datetime.now()
    M3P= time + relativedelta(months=3)
    if now <= M3P:
        return True
    else:
        return False

def save_pdf(base_name, folder_path):
    """
    Save a PDF file from user to a specified folder with a given name.
    """
    os.makedirs(folder_path, exist_ok=True)
    
    root = tk.Tk()
    root.withdraw()
    root.update()  # اجباری برای اینکه پنجره render بشه
    file_path = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )
    root.destroy()

    if file_path:
        destination = os.path.join(folder_path, base_name)
        shutil.copy(file_path, destination)
        return destination
    return None


def course_actions(student_id):
    with open(req_path, "r") as file:
      requests= json.load(file)
    for req in requests:
        if req["name"] == student_id:
            if req["status"]=="accepted":
                if passed_time_3m(req["time_req"]):
                    print("you can upload your project")
                    saved_path = save_pdf(student_id, project_path)
                    if saved_path:
                        print(f"File saved to {saved_path}")
                    else:
                        print("No file selected")
                else:
                    print("three months didn't pass after your req")
            else:
                print("Your request has not been accepted yet!")
    return None
    

def stu_menu(student_id):
    '''main menu for student'''
    for student in students:
        if student["student_id"] == student_id:
            print("*** Student Panel ***")
            print(f"Name: {student["name"]}")
            break
    while True:
        print("\n1-choose course\n2-see status\n3-course actions\n4-exit to main")
        choice= input()
        if choice == '1':
            get_course(student_id)
        elif choice == '2':
            get_status(student_id)
        elif choice == '3':
            course_actions(student_id)
        elif choice == '4':
            break
    return None

if __name__ == "__main__":
     print("please run the main program!")
