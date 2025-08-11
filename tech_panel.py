import json

pas_path="D:/UNIVERSTIY/ai project/python/ending_project/save_directory_tech/pas.json"


def prof_menu():
    print("*** techers panel ***")
    

def pas_enter():

    with open(pas_path, "r") as file:
        teachers = json.load(file)

    id=input("exit = x\nenter your teaching ID: ")
    
    for prof in teachers:
        if id == "x":
            return
        if prof["professor_id"] == id:
            print(f"welcome {prof['name']}")
            pas=input("please enter your password: ")
            if prof["password"] == pas:
                return True
            else:
                print("wrong password")
                pas_enter()
    return False
