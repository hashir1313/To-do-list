import  tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("To Do List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

def add_task():
    task = task_entry.get()
    task_entry.delete(0, END)
    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(task + "\n")
        task_list.append(task)
        listbox.insert( END, task)

def delete_task():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                 taskfile.write(task+"\n")
        listbox.delete( ANCHOR)

def open_task_file():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task != "\n":
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file = open("tasklist.txt", "w")
        file.close()



# Top 
Image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, Image_icon)
top_frame = Frame(root, width=400, height=80, bg="#32405b")
top_frame.place(x=0, y=0)
note_Image = PhotoImage(file="icon.png")
Label(top_frame, image=note_Image, bg="#32405b").place(x=30 , y=25)
heading = Label(top_frame, text="All Tasks", font=("Consolas", 20),fg="white", bg="#32405b")
heading.place(x=130, y=25)

# Add  to list 
add_frame = Frame(root, width=400, height=50)
add_frame.place(x=0, y=80)
task = StringVar()
task_entry = Entry(add_frame, width=18, font=("Consolas", 20), bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()
button_add = Button(add_frame, text="Add", font=("Consolas", 20), width=6, bg="#5a95ff", fg="#fff", bd=0, command=add_task)
button_add.place(x=310, y=0)

# Delete from list
del_frame = Frame(root, width=400, height=50)
del_frame.place(x=0, y=130)
button_delete = Button(del_frame, text="Delete", font=("Consolas", 20), width=27, bg="#5a95ff", fg="#fff", bd=0, command=delete_task)
button_delete.place(x=0, y=0)

# List
list_frame = Frame(root)
list_frame.place(x=0, y=180)
listbox = Listbox(list_frame, font=("Consolas", 18), bg="#32405b", width=29, height=16, bd=0, fg="white", selectbackground="#5a95ff", cursor="hand2")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
open_task_file()

root.mainloop()