from tkinter import *
from tkinter import messagebox as ms
win = Tk()

def add_task():
    task = U_entry.get()
    if  task.strip() == 0:
        ms.showerror("추가 버튼","값이 입력되지 않았습니다.")
    else:
        taskLibox.insert(0, task)
        U_entry.delete(0,END)

def del_task():
    task_selected = taskLibox.curselection()
    taskLibox.delete(task_selected)       

notice = Label(win, text="Add a Task")
U_entry = Entry(win)
taskLibox = Listbox(win)
addbt = Button(win, command=add_task, text="add task")
delbt = Button(win, command=del_task, text="Delete Task")

notice.pack()
U_entry.pack()
addbt.pack()
taskLibox.pack()
delbt.pack()
win.mainloop()