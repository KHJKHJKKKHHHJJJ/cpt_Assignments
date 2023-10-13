import sqlite3
from tkinter import *
from tkinter import messagebox as ms

con = sqlite3.connect("C:/Users/scott/OneDrive - 우송대학교(WOOSONG UNIVERSITY)/,/a/md202310603")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS userData")
cur.execute("CREATE TABLE userData(id char(15), name char(20), email char(30), birthYear int)")

def ent_func():
    id = id_entry.get()
    name = name_entry.get()
    email = email_entry.get()
    birth = birth_entry.get()
    try:
        cur.execute(f"INSERT INTO userData VALUES('{id}','{name}','{email}', {birth})")
    except:
        ms.showerror("오류", "데이터 입력 오류가 발생함")
    birth_entry.delete(0,END);email_entry.delete(0,END);id_entry.delete(0,END);name_entry.delete(0,END)

def check_func():
    cur.execute("SELECT * FROM userData")
    count = 0
    id_Libox.delete(0,END);name_Libox.delete(0,END);email_Libox.delete(0,END);birth_Libox.delete(0,END)
    while True:
        row = cur.fetchone()
        if row == None:
            if count >= 1:
                break
            else:
                ms.showerror("오류", "데이터가 없습니다.")
                break
        id_Libox.insert(0,row[0]);name_Libox.insert(0,row[1]);email_Libox.insert(0,row[2]);birth_Libox.insert(0,row[3])
        count += 1
    id_Libox.insert(0,"-----------");id_Libox.insert(0,"사용자 ID")
    email_Libox.insert(0,"-----------");email_Libox.insert(0,"사용자이름")
    name_Libox.insert(0,"-----------");name_Libox.insert(0,"이메일")
    birth_Libox.insert(0,"-----------");birth_Libox.insert(0,"출생연도")

win = Tk()
win.title("GUI 데이터 입력")

ent_frame = Frame(win)
id_entry = Entry(ent_frame, width=10)
name_entry = Entry(ent_frame, width=10)
email_entry = Entry(ent_frame, width=10)
birth_entry = Entry(ent_frame, width=10)
ent_btn = Button(ent_frame, text="입력", command=ent_func)
check_btn = Button(ent_frame, text="조회", command=check_func)

Libox_frame = Frame(win)
id_Libox = Listbox(Libox_frame, bg="yellow", height=15)
name_Libox =Listbox(Libox_frame, bg="yellow", height=15)
email_Libox = Listbox(Libox_frame, bg="yellow", height=15)
birth_Libox = Listbox(Libox_frame, bg="yellow", height=15)

ent_frame.pack();id_entry.pack(side=LEFT, padx=15, pady=10);name_entry.pack(side=LEFT, padx=15, pady=10);email_entry.pack(side=LEFT, padx=15, pady=10);birth_entry.pack(side=LEFT, padx=15, pady=10);ent_btn.pack(side=LEFT, padx=10, pady=10);check_btn.pack(side=LEFT, padx=10, pady=10)

Libox_frame.pack(side=BOTTOM);id_Libox.pack(side=LEFT);name_Libox.pack(side=LEFT);email_Libox.pack(side=LEFT);birth_Libox.pack(side=LEFT)

win.mainloop()