
import tech_panel
import student_panel

def tech_panel_call():
    res= tech_panel.pas_enter()
    if res == True:
        tech_panel.prof_menu()
    if res == False:
        print("wrong information")
def student_panel_call():
    res= student_panel.pas_enter()
    if  res == True:
        student_panel.stu_menu()
    if res == False:
        print("wrong enterance")

def main_menu():
    while True:
        print("""*** main menu ***\nselect your passion\nselect the number\n1-student\n2-teacher\nexit = X""")
        tar = input()
        if tar == "1":
            student_panel_call()
        elif tar == "2":
            tech_panel_call()
        elif tar.lower() == "x":
            break
        else:
            print("enter a valid number!")
if __name__ == "__main__":
    main_menu()