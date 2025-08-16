import json

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
     print("*** request panel ***")
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
     if counter == 1:
          print("you don't have any pending request")
     tar=input("enter 'x' for exit\n")
     while True:
          item=next(read_req())
          if tar == item["req_id"]:
               print("for accept 'a' and for reject 'r' exit 'x'" )
               choice=input()
               if choice == "a":
                    item["status"]="accepted"
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

def my_course(ID):
     for req in requests:
          if req["to_prof"] == ID and req["status"] == "accepted":
               print(f"student name: {stu_to_name(req["name"])}\n"
                     f"course id: {req["req_course"]}\n"
                     f"req time: {req["time_req"]}\n"
                     f"for prof: {req["to_prof"]}\n"
                     f"staus: {req["status"]}\n"
                     f"request id: {req["req_id"]}")
     
     
def prof_menu(id):
     print("*** techers panel ***")
     for prof in teachers:
         if prof["professor_id"] == id:
               id_3=prof["ID"]
               print(f"Hello {prof["name"]}\nwelcome to your panel")
     print("choose and enter the number")
    
     while True:
          choice=input("1-guide prof\n2-referee prof\n3-on going courses\n4-exit\n")
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