'''main page'''
import tech_panel
import student_panel

def tech_panel_call():
    '''go to professor panel'''
    res= tech_panel.pas_enter()
    if res == True:
        tech_panel.prof_menu()
    if res == False:
        print("wrong information")
        
def student_panel_call():
    '''go to student panel'''
    student_id = student_panel.pas_enter()
    if student_id:
        student_panel.stu_menu(student_id)
    else:
        print("Exit or login failed.")


def main_menu():
    '''choosing the rool acces'''
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