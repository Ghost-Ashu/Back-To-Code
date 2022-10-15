from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
import re
import os.path
import numpy as np
import matplotlib.pyplot as plt


file_exists = os.path.exists('SaveFile.txt')
if file_exists == False:
    file1 = open("SaveFile.txt",'w')
    file1.close()

status = ["Completed", "Not Completed"]
window = Tk()
window.geometry('1000x1000')
window.resizable(False, False)
window.configure(bg='#222831')
window.title('To Do List')
style = ttk.Style(window)
style.theme_use("clam")
style.configure("Treeview", font=('Calibri', 15, 'bold'), background="#393E46", fieldbackground="#393E46",
                foreground="white")
f = ('Calibri', 13, 'bold')
hour_string = StringVar()
min_string = StringVar()
last_value_sec = ""
last_value = ""
personal = 0
work = 0

def count():
    choice = var.get()
    global personal
    global work
    if choice == 1:
        personal+=1
        print(personal)
    elif choice == 2:
        work+=1
        print(work)


def display_msg():
    date = cal.get_date()
    m = min_sb.get()
    h = sec_string.get()
    s = sec.get()
    t = f"The task is added for {date} at {m}:{h}:{s}."
    msg_display.config(text=t)


def add_task():
    current_task = textInput.get()
    current_task = current_task.title()
    if current_task != "":
        lb_tasks.insert('', 'end', text="", values=(
        current_task, cal.get_date(), "{}:{}:{}".format(min_sb.get(), sec_string.get(), sec.get())))
        file1 = open("SaveFile.txt", "a")
        file1.write(current_task)
        file1.write("@")
        file1.write(cal.get_date())
        file1.write("@")
        file1.write(min_sb.get())
        file1.write(":")
        file1.write(sec_string.get())
        file1.write(":")
        file1.write(sec.get())
        file1.write("\n")
        file1.close()
        display_msg()
    else:
        conf = messagebox.showinfo("Invalid Entry", "Please enter a task")
        print(conf)
    textInput.delete(0, 'end')


def sortTasks():
    lines = open("SaveFile.txt", "r").readlines()
    lines.sort(key=lambda line: line.split("@")[1:])
    file2 = open("SaveFile.txt", "w")
    for i in lines:
        file2.write(i)
    file2.close()
    file1 = open("SaveFile.txt", "r+")
    content = file1.readlines()
    for item in lb_tasks.get_children():
        lb_tasks.delete(item)
    for currentTask in content:
        temp_tasks = re.split('["@""\n"]', currentTask)
        lb_tasks.insert('', 'end', text="", values=(temp_tasks[0], temp_tasks[1], temp_tasks[2]))
    file1.close()


def delete_all():
    conf = messagebox.askquestion(
        'Delete all?', 'Are you sure to delete all task?')
    print(conf)
    if conf.upper() == "YES":
        for item in lb_tasks.get_children():
            lb_tasks.delete(item)
        file1 = open("SaveFile.txt", 'w')
        file1.close()
    else:
        pass

def mark_as_done():
    selected_items = lb_tasks.selection()
    curItem = lb_tasks.focus()
    index = lb_tasks.index(curItem)
    for selected_item in selected_items:
        lb_tasks.delete(selected_item)
    l1 = []
    with open(r"SaveFile.txt", 'r') as fp:
        l1 = fp.readlines()
    with open(r"SaveFile.txt", 'w') as fp:
        for number, line in enumerate(l1):
            if number not in [index, index]:
                fp.write(line)


def plot_graph():
    category = ['Personal', 'Work']
    data = [personal, work]
    fig = plt.figure(figsize=(10, 7))
    plt.pie(data, labels=category)
    plt.show()


# Making a treeview to display tasks
lb_tasks = ttk.Treeview(window, column=("c1", "c2", "c3"), show='headings', height=20)
lb_tasks.column("# 1", anchor=CENTER, width=250)
lb_tasks.heading("# 1", text="TASK")
lb_tasks.column("# 2", anchor=CENTER, stretch=NO)
lb_tasks.heading("# 2", text="DATE")
lb_tasks.column("# 3", anchor=CENTER, stretch=NO, width=150)
lb_tasks.heading("# 3", text="TIME")
lb_tasks.place(x=310, y=50)
vsb = ttk.Scrollbar(window, orient="vertical", command=lb_tasks.yview)
vsb.place(x=912, y=50, height=428)
lb_tasks.configure(yscrollcommand=vsb.set)

# Loading tasks saved previously
file1 = open("SaveFile.txt", "r")
content = file1.readlines()
for currentTask in content:
    temp_tasks = re.split('["@""\n"]', currentTask)
    lb_tasks.insert('', 'end', text="", values=(temp_tasks[0], temp_tasks[1], temp_tasks[2]))

#Buttons
sort = Button(window, font=f, text="Sort Tasks", bg="#00FFF5", fg="black", width=15, command=sortTasks)
sort.place(x=90, y=70)

plot_graph = Button(window, font=f, text="Plot Graph", bg="#00FFF5", fg="black", width=15, command=plot_graph)
plot_graph.place(x=90, y=130)

deleteOne = Button(window, font=f, text="Mark As Done", bg="#00FFF5", fg="black", width=15, command=mark_as_done)
deleteOne.place(x=90, y=190)

deleteAll = Button(window, font=f, text="Delete all tasks", bg="#00FFF5", fg="black", width=15,command=delete_all)
deleteAll.place(x=90, y=250)

cal = Calendar(showweeknumbers=False)
cal.place(x=40, y=320)

min_sb = Spinbox(window, from_=0, to=23, wrap=True, textvariable=hour_string, font=f, width=2, justify=CENTER, )
min_sb.place(x=75, y=530)

sec_string = Spinbox(window, from_=0, to=59, wrap=True, textvariable=min_string, font=f, width=2, justify=CENTER)
sec_string.place(x=125, y=530)

sec = Spinbox(window, from_=0, to=59, wrap=True, textvariable=sec_string, width=2, font=f, justify=CENTER)
sec.place(x=175, y=530)

msg = Label(window, text="HH       MM       SS", font=f, bg="#222831", fg="white")
msg.place(x=75, y=560)

if last_value == "59" and min_string.get() == "0":
    hour_string.set(int(hour_string.get()) + 1 if hour_string.get() != "23" else 0)
    last_value = min_string.get()

if last_value_sec == "59" and sec_string.get() == "0":
    min_string.set(int(min_string.get()) + 1 if min_string.get() != "59" else 0)

if last_value == "59":
    hour_string.set(int(hour_string.get()) + 1 if hour_string.get() != "23" else 0)
    last_value_sec = sec_string.get()

textInput = Entry(window, font=f, width=67)
textInput.place(x=310, y=500)

var = IntVar()
rb1 = Radiobutton(text='Personal', variable=var,
                          bg="#00FFF5", fg="black",value=1, command=count)
rb1.place(x=310,y=550)
rb2 = Radiobutton(text='Work', variable=var,
                          bg="#00FFF5",fg="black",value=2, command=count)
rb2.place(x=410,y=550)

add = Button(window, font=f, text="Add Task", bg="#00FFF5", fg="black", width=15, command=lambda: add_task())
add.place(x=540, y=600)

msg_display = Label(window, font=f, text="", bg="#222831", fg="white")
msg_display.place(x=710, y=600)

window.mainloop()