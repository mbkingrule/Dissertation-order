import json
from datetime import datetime
import os
import tkinter as tk
from tkcalendar import Calendar

pas_path = "save_directory_tech/pas.json"
stu_pas_path = "save_directory_student/pas.json"
req_path = "main_directory/course_req.json"
project_path = "main_directory/projects_directory"
present_path = "main_directory/presents.json"

with open(stu_pas_path, "r") as file:
    student = json.load(file)
with open(req_path, "r") as file:
    requests = json.load(file)
with open(pas_path, "r") as file:
    teachers = json.load(file)
with open(present_path, "r") as file:
    presents = json.load(file)


class DefenseSession:
    def __init__(self, request_id, student_id, supervisor):
        self.request_id = request_id
        self.student_id = student_id
        self.date = None
        self.supervisor = supervisor
        self.internal_examiner = None
        self.external_examiner = None
        self.scores = {
            "supervisor": None,
            "internal_examiner": None,
            "external_examiner": None,
        }

    def set_date(self, date):
        self.date = date

    def set_examiner(self, int_ex, ext_ex):
        self.internal_examiner = int_ex
        self.external_examiner = ext_ex

    def save_to_json(self):
        data = {
            "request_id": self.request_id,
            "student_id": self.student_id,
            "date": self.date,
            "supervisor": self.supervisor,
            "internal_examiner": self.internal_examiner,
            "external_examiner": self.external_examiner,
            "scores": self.scores,
        }

        if os.path.exists(present_path):
            with open(present_path, "r", encoding="utf-8") as f:
                try:
                    presents = json.load(f)
                    if not isinstance(presents, list): 
                        presents = []
                except json.JSONDecodeError:
                    presents = []
        else:
            presents = []

        presents.append(data)

        with open(present_path, "w", encoding="utf-8") as f:
            json.dump(presents, f, ensure_ascii=False, indent=4)

        print(f"Defense session saved to {present_path}")

    def __str__(self):
        return (
            f"Request ID: {self.request_id}\n"
            f"Student ID: {self.student_id}\n"
            f"Date: {self.date}\n"
            f"Supervisor: {self.supervisor}, Score: {self.scores['supervisor']}\n"
            f"Internal Examiner: {self.internal_examiner}, Score: {self.scores['internal_examiner']}\n"
            f"External Examiner: {self.external_examiner}, Score: {self.scores['external_examiner']}\n"
            f"Total Score: {self.get_total_score()}"
        )


def get_date_from_user():
    selected_date = {"value": None}  

    def on_select():
        selected_date["value"] = cal.get_date()
        root.destroy() 

    root = tk.Tk()
    root.title("Select a Date")

    cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.pack(pady=10)

    tk.Button(root, text="Select", command=on_select).pack(pady=5)

    root.mainloop()
    return selected_date["value"]


def id_name_prof(id):
    """convert prof id to name professor"""
    for prof in teachers:
        if prof["ID"] == id:
            return prof["name"]
    return "unknown"


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
    print("choose the request id for actions")
    counter = 1
    for req in requests:
        if ID == req["to_prof"] and req["status"] == None:
            print(
                f"req: {counter}\n"
                f"student name: {stu_to_name(req["name"])}\n"
                f"course id: {req["req_course"]}\n"
                f"req time: {req["time_req"]}\n"
                f"for prof: {req["to_prof"]}\n"
                f"staus: {req["status"]}\n"
                f"request id: {req["req_id"]}"
            )
            counter += 1
        print("\n")
    if counter == 1:
        print("\nyou don't have any pending request")
    tar = input("enter 'x' for exit\n")
    while True:
        item = next(read_req())
        if tar == item["req_id"]:
            print("\nfor accept 'a' and for reject 'r' exit 'x'")
            choice = input()
            if choice == "a":
                item["status"] = "accepted"
                item["time_req"] = str(datetime.now())
                for tech in teachers:
                    if tech["ID"] == ID:
                        tech["assigned_students"] += 1
            elif choice == "r":
                item["status"] = "rejected"
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
        if (
            filename.lower().endswith(".pdf")
            and search_name.lower() in filename.lower()
        ):
            file_path = os.path.join(project_path, filename)
            print(f"Opening: {file_path}")
            os.startfile(file_path)
            return
    print("No matching PDF found.")


def set_score_sup(request_id):
    tar = request_id
    for proj in presents:
        if proj["request_id"] == tar:
            sco = input("enter your score as a number")
            sco = int(sco)
            proj["scores"]["supervisor"] = sco
    with open(present_path, "w") as f:
        json.dump(presents, f, indent=4)


def set_score_exm(ID):
    for proj in presents:
        if proj["internal_examiner"] == ID or proj["external_examiner"] == ID:
            print(
                f"student id: {stu_to_name(proj["student_id"])}\n"
                f"request id: {proj["request_id"]}\n"
                f"supervisor: {id_name_prof(proj["supervisor"])}"
            )
    print("select the request id you want to score it")
    tar = input()
    for proj in presents:
        if proj["request_id"] == tar:
            if proj["internal_examiner"] == ID:
                sco = input("enter your score as a number")
                sco = int(sco)
                proj["scores"]["internal_examiner"] = sco
            elif proj["external_examiner"] == ID:
                sco = input("enter your score as a number")
                sco = int(sco)
                proj["scores"]["external_examiner"] = sco
    with open(present_path, "w") as f:
        json.dump(presents, f, indent=4)


def my_course(ID):
    for req in requests:
        if req["to_prof"] == ID and req["status"] == "accepted":
            if req["upload_status"] == True:
                sta = "project presented"
            else:
                sta = "project not presented"
            print(
                f"student name: {stu_to_name(req["name"])}\n"
                f"course id: {req["req_course"]}\n"
                f"req time: {req["time_req"]}\n"
                f"for prof: {req["to_prof"]}\n"
                f"staus: {req["status"]}\n"
                f"request id: {req["req_id"]}\n"
                f"project status : {sta}"
            )
        print("\n")
    tar_1 = input("enter the request id for actions")
    for req in requests:
        if req["req_id"] == tar_1:
            session = DefenseSession(req["req_id"], req["name"], req["to_prof"])
            print(f"*** action menu ***\n" f"request from {stu_to_name(req["name"])}\n")
            while True:
                tar_2 = input(
                    f"1-open project file\n2-select time to present\n"
                    f"3-select refeeri\n4-set score\n5-exit\n"
                )
                if tar_2 == "1":
                    open_pdf_by_name(req["name"])
                elif tar_2 == "2":
                    time = get_date_from_user()
                    session.set_date(time)
                elif tar_2 == "3":
                    for prof in teachers:
                        if prof["ID"] != ID:
                            if prof["assigned_refer"] <= 10:
                                print(
                                    f"name: {prof["name"]}\n"
                                    f"ID: {prof["ID"]}\n"
                                    f"remainig slot: {10 - prof["assigned_refer"]}"
                                )
                    examiner1 = input("enter the  int examiner ID: ")
                    examiner2 = input("enter the  ext examiner ID: ")
                    session.set_examiner(examiner1, examiner2)
                    session.save_to_json()
                    break
                elif tar_2 == "4":
                    set_score_sup(req["req_id"])
                elif tar_2 == "5":
                    break
        break


def prof_menu(id):
    print("\n*** techers panel ***")
    for prof in teachers:
        if prof["professor_id"] == id:
            id_3 = prof["ID"]
            print(f"Hello {prof["name"]}\nwelcome to your panel\n")
    print("choose and enter the number")

    while True:
        choice = input(
            "1-guide prof\n2-referee prof\n3-courses action\n4-set score\n5-exit\n"
        )
        if choice == "1":
            stu_req_m(id_3)
        elif choice == "2":
            pass
        elif choice == "3":
            my_course(id_3)
        elif choice == "4":
            set_score_exm(id_3)
        elif choice == "5":
            break
    return None


def pas_enter():
    id = input("exit = x\nenter your teaching ID: ")
    if id.lower() == "x":
        return None

    for prof in teachers:
        if prof["professor_id"] == id:
            print(f"welcome {prof['name']}")
            pas = input("please enter your password: ")
            if prof["password"] == pas:
                return id
            else:
                print("wrong password")
                pas_enter()
    else:
        print("teacher ID not found please try again")


if __name__ == "__main__":
    print("please run the main program!")
