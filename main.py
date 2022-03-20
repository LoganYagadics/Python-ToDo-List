from tkinter import *
from tkinter import messagebox


def new_task():
    task = entry_box.get()
    if task != "" and not is_duplicate(task):
        list_box.insert(END, task)
        entry_box.delete(0, "end")
        file = open("tasks.txt", "a")
        file.write(task + "\n")
        file.close()
    else:
        messagebox.showwarning("warning", "Tasks can not be left blank or duplicate existing tasks.")


def delete_task():
    task = ""

    for i in list_box.curselection():
        task = list_box.get(i)

    list_box.delete(ANCHOR)

    file = open("tasks.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("tasks.txt", "w")

    new_lines = []
    for line in lines:
        if line != task+"\n":
            new_lines.append(line)

    file.writelines(new_lines)


def load_tasks():
    file = open("tasks.txt","r")
    task_list = file.readlines()
    file.close()

    for item in task_list:
        list_box.insert(END, item.strip())

def is_duplicate(task):
    for x in range(list_box.size()):
        if task == list_box.get(x):
            return True

    return False

root = Tk()
root.geometry('600x500+600+250')
root.title('Python To-Do List')
root.config(bg='#333333')
root.resizable(width=False, height=False)


frame = Frame(root)
frame.pack(pady=10)

list_box = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#888888',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    bg='#444444'

)
list_box.pack(side=LEFT, fill=BOTH)

scroll_bar = Scrollbar(frame)
scroll_bar.pack(side=RIGHT, fill=BOTH)

list_box.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=list_box.yview)

entry_box = Entry(root, font=('times', 24), bg="#222222")
entry_box.pack(pady=20)

button_frame = Frame(root)
button_frame.config(bg="#333333")
button_frame.pack(pady=20)

addTaskButton = Button(
    button_frame,
    text="Add Task",
    font=('times', 14),
    bg='#444444',
    padx=20,
    pady=10,
    command=new_task
)
addTaskButton.pack(fill=BOTH, expand=True, side=LEFT, padx=10)


deleteTaskButton = Button(
    button_frame,
    text="Delete Task",
    font=('times', 14),
    bg='#222222',
    padx=20,
    pady=10,
    command=delete_task
)
deleteTaskButton.pack(fill=BOTH, expand=True, side=LEFT, padx=10)

load_tasks()
root.mainloop()



