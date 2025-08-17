'''main page'''
import tech_panel
import student_panel

def tech_panel_call():
    '''go to professor panel'''
    tech_id= tech_panel.pas_enter()
    if tech_id:
        tech_panel.prof_menu(tech_id)
    else:
        print("Exit or login failed.")
        
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
        print("""*** main menu ***\nselect your passion\nselect the number\n1-student\n2-teacher\n3-exit""")
        tar = input()
        if tar == "1":
            student_panel_call()
        elif tar == "2":
            tech_panel_call()
        elif tar == "3":
            break
        else:
            print("enter a valid number!")
            
if __name__ == "__main__":
    main_menu()