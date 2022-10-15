from tkinter import *

window = Tk()
window.geometry('500x500')
window.resizable(False, False)
window.configure(bg='#222831')
window.title('To Do List')
blankText = ""

def add_task():
    currentTask = textInput.get()
    if currentTask != "":
        tasks.append(currentTask)
        lb_tasks.insert("end", currentTask)
        file1 = open("SaveFile.txt", "a")
        file1.write(currentTask)
        file1.write("\n")
        file1.close()

# def sort_asc():
#     tasks.sort()
#     update_tasks()

tasks = []

lb_tasks = Listbox(window, bg="#393E46")
lb_tasks.place(x=180, y=50, height=300, width=300)

file1 = open("SaveFile.txt", "r")
content = file1.readlines()
for currentTask in content:
    temp_tasks = currentTask.split("\n")
    lb_tasks.insert("end", temp_tasks[0])
    tasks.append(temp_tasks[0])


sort = Button(window, text="Sort Tasks", bg="#00FFF5", fg="black", width=15, command=sort_asc)
sort.place(x=35, y=70)

plot_graph = Button(window, text="Plot Graph", bg="#00FFF5", fg="black", width=15)
plot_graph.place(x=35, y=120)

deleteOne = Button(window, text="Mark As Done", bg="#00FFF5", fg="black", width=15)
deleteOne.place(x=35, y=170)

deleteAll = Button(window, text="Delete all tasks", bg="#00FFF5", fg="black", width=15)
deleteAll.place(x=35, y=220)

textInput = Entry(window, width=49)
textInput.place(x=180, y=375)

add = Button(window, text="Add Task", bg="#00FFF5", fg="black", width=15, command=add_task)
add.place(x=265, y=425)

window.mainloop()
