import tkinter as tk
import tech_panel
import student_panel

def tech_panel_call():
    tech_panel.start()

def student_panel_call():
    student_panel.start()

window = tk.Tk()
window.title("** main menu **")
window.geometry("400x200")

ask_user = tk.Label(window, text="select your passion", font=("Arial", 14))
ask_user.pack(pady=10)

ans_frame = tk.Frame(window)
ans_frame.pack()

ans_1 = tk.Button(window, text="student", command=student_panel_call)
ans_2 = tk.Button(window, text="techer", command=tech_panel_call)

ans_1.pack(side="left", padx=20)
ans_2.pack(side="left", padx=20)

window.mainloop()