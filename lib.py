import json
import re

prof_path = "save_directory_tech/pas.json"
stu_path = "save_directory_student/pas.json"
req_path = "main_directory/course_req.json"
project_path = "main_directory/projects_directory"
present_path = "main_directory/presents.json"
course_path = "main_directory/courses.json"
lib_info_path = "main_directory/lib_info.json"

with open(prof_path, "r") as f:
    teachers= json.load(f)
with open(stu_path, "r") as f:
    students= json.load(f)
with open(req_path, "r") as f:
    requests= json.load(f)
with open(course_path, "r") as f:
    courses= json.load(f)
with open(present_path, "r") as f:
    presents= json.load(f)
with open(lib_info_path, "r", encoding="utf-8") as f:
    data= json.load(f)

class Dissertation:
    def __init__(self):
        self.subject = None
        self.writer = None
        self.year = None
        self.semester = None
        self.examiner = []
        self.supervisor = None
        self.score = None
    def to_dict(self):
        return {
            "subject": self.subject,
            "writer": self.writer,
            "year": self.year,
            "semester": self.semester,
            "examiners": self.examiner,
            "supervisor": self.supervisor,
            "score": self.score
        }
    def update_save(self):
        for proj in presents:
            if proj["scores"]["supervisor"] is not None and\
                  proj["scores"]["internal_examiner"] is not None and\
                  proj["scores"]["external_examiner"] is not None:
                c_id_match=re.search(r"(C\d+)", proj["request_id"], re.IGNORECASE)
                if c_id_match:
                    c_id = c_id_match.group()
                    for course in courses:
                        if c_id == course["course_id"]:
                            self.subject = course["title"]
                            self.year = course["year"]
                            self.semester = course["semester"]
                    self.writer = proj["student_id"]
                    self.supervisor = proj["supervisor"]
                    self.examiner = [proj["internal_examiner"], proj["external_examiner"]]
                    mid_score = proj["scores"]["supervisor"]+ \
                    proj["scores"]["internal_examiner"]+ \
                    proj["scores"]["external_examiner"]
                    mid_score = mid_score // 3
                    self.score = mid_score
                    info= self.to_dict()
                    data.append(info)
        with open(lib_info_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

def stu_name(ID):
    for stu in students:
        if stu["student_id"] == ID:
            return stu["name"]

def prof_name(ID):
    for prof in teachers:
        if prof["ID"] == ID:
            return["name"]

def full_list():
    for dis in data:
        print(f"subject: {dis["subject"]}\n"
                  f"writer: {stu_name(dis["writer"])}\n"
                  f"year: {dis["year"]}\n"
                  f"semester: {dis["semester"]}\n"
                  f"examiners: {prof_name(dis["examiners"][0])}, {prof_name(dis["examiners"][1])}\n"
                  f"supervisor: {dis["supervisor"]}\n"
                  f"score: {dis["score"]}")
 
def search_sup():
    print("enter name or id: ")
    tar = input()
    for dis in data:
        sup_name= prof_name(dis["supervisor"])
        if tar in sup_name or tar == dis["supervisor"]:
            print(f"subject: {dis["subject"]}\n"
                  f"writer: {stu_name(dis["writer"])}\n"
                  f"year: {dis["year"]}\n"
                  f"semester: {dis["semester"]}\n"
                  f"examiners: {prof_name(dis["examiners"][0])}, {prof_name(dis["examiners"][1])}\n"
                  f"supervisor: {dis["supervisor"]}\n"
                  f"score: {dis["score"]}")
            
def search_sub():
    print("enter subject you want: ")
    tar = input()
    for dis in data:
        sub_name = dis["subject"]
        if tar in sub_name:
            print(f"subject: {dis["subject"]}\n"
                  f"writer: {stu_name(dis["writer"])}\n"
                  f"year: {dis["year"]}\n"
                  f"semester: {dis["semester"]}\n"
                  f"examiners: {prof_name(dis["examiners"][0])}, {prof_name(dis["examiners"][1])}\n"
                  f"supervisor: {dis["supervisor"]}\n"
                  f"score: {dis["score"]}")



def menu():
    d=Dissertation()
    d.update_save()
    print("*** projects lib menu ***")
    while True:
        print("\n1-search by supervisor\n"
            "2-search by subject\n"
            "3-search by writer\n"
            "4-full list\n"
            "5-exit\n")
        tar= input()
        if tar == "1":
            search_sup()
        elif tar == "2":
            search_sub()
        elif tar == "3":
            pass
        elif tar == "4":
            full_list()
        elif tar == "5":
            break
        else:
            print("\nenter a valid menu number!!")
    return None

menu()
'''if __name__ == "__main__":
    print("run the main program!!")'''
        