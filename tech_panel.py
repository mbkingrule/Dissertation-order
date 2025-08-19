import json
from datetime import datetime
import os


class prof:
     def __init__(self, id):
          self.id= id
          self.course=[]
          self.c_prof= None
          self.c_refree= None
          self.c_get= []
          self.ref_get = []
     def add_course(self, c_id):
          pass

pas_path="save_directory_tech/pas.json"
stu_pas_path="save_directory_student/pas.json"
req_path="main_directory/course_req.json"
project_path="main_directory/projects_directory"

with open(stu_pas_path, "r") as file:
     student= json.load(file)
with open(req_path, "r") as file:
     requests = json.load(file)
with open(pas_path, "r") as file:
     teachers = json.load(file)

def read_req():
     for req in requests:
          yield req

def stu_to_name(id):
     for stu in student:
          if id == stu["student_id"]:
               return stu["name"]

def stu_req_m(ID):
     for tech in teachers:
          if ID == tech["ID"]:
               if tech["assigned_students"] >= 5:
                    print("\nprof you reach limits\n")
                    return None
     print("\n*** request panel ***\n")
     print ("choose the request id for actions")
     counter=1
     for req in requests:
          if ID == req["to_prof"] and req["status"] == None:
               print(f"req: {counter}\n"
                     f"student name: {stu_to_name(req["name"])}\n"
                     f"course id: {req["req_course"]}\n"
                     f"req time: {req["time_req"]}\n"
                     f"for prof: {req["to_prof"]}\n"
                     f"staus: {req["status"]}\n"
                     f"request id: {req["req_id"]}")
               counter+=1
          print("\n")
     if counter == 1:
          print("\nyou don't have any pending request")
     tar=input("enter 'x' for exit\n")
     while True:
          item=next(read_req())
          if tar == item["req_id"]:
               print("\nfor accept 'a' and for reject 'r' exit 'x'" )
               choice=input()
               if choice == "a":
                    item["status"]="accepted"
                    item["time_req"]=str(datetime.now())
                    for tech in teachers:
                         if tech["ID"] == ID:
                              tech["assigned_students"]+=1
               elif choice == "r":
                    item["status"]="rejected"
               elif choice == "x":
                    break
               else:
                    print("enter valid char!")
                    continue
          with open(pas_path, "w") as f:
               json.dump(teachers, f, indent=4)
          with open(req_path, "w") as f:
               json.dump(requests, f, indent=4)
          print("your action sved succesfully!")
          break

def open_pdf_by_name(search_name):
    for filename in os.listdir(project_path):
        if filename.lower().endswith(".pdf") and search_name.lower() in filename.lower():
            file_path = os.path.join(project_path, filename)
            print(f"Opening: {file_path}")
            os.startfile(file_path)
            return
    print("No matching PDF found.")


def my_course(ID):
     for req in requests:
          if req["to_prof"] == ID and req["status"] == "accepted":
               if req["upload_status"] == True:
                    sta="project presented"
               else:
                    sta="project not presented"
               print(f"student name: {stu_to_name(req["name"])}\n"
                     f"course id: {req["req_course"]}\n"
                     f"req time: {req["time_req"]}\n"
                     f"for prof: {req["to_prof"]}\n"
                     f"staus: {req["status"]}\n"
                     f"request id: {req["req_id"]}\n"
                     f"project status : {sta}")
          print("\n")
     tar_1=input("enter the request id for actions")
     for req in requests:
          if req["req_id"] == tar_1:
               print(f"*** action menu ***\n"
                     f"request from {stu_to_name(req["name"])}\n")
               while True:
                    tar_2=input(f"1-open project file\n2-select time to present\n"
                                f"3-select refeeri\n4-exit")
                    if tar_2 == "1":
                         open_pdf_by_name(req["name"])
                    elif tar_2 == "2":
                         pass
                    elif tar_2 == "3":
                         pass
                    elif tar_2 == "4":
                         break
def prof_menu(id):
     print("\n*** techers panel ***")
     for prof in teachers:
         if prof["professor_id"] == id:
               id_3=prof["ID"]
               print(f"Hello {prof["name"]}\nwelcome to your panel\n")
     print("choose and enter the number")
    
     while True:
          choice=input("1-guide prof\n2-referee prof\n3-courses action\n4-exit\n")
          if choice == "1":
               stu_req_m(id_3)
          elif choice == "2":
               pass
          elif choice == "3":
               my_course(id_3)
          elif choice =="4":
               break
     return None
     
def pas_enter():
    id=input("exit = x\nenter your teaching ID: ")
    if id.lower() == "x":
            return None

    for prof in teachers:
        if prof["professor_id"] == id:
            print(f"welcome {prof['name']}")
            pas=input("please enter your password: ")
            if prof["password"] == pas:
                return id
            else:
                print("wrong password")
                pas_enter()
    else:
        print("teacher ID not found please try again")

if __name__ == "__main__":
     print("please run the main program!")