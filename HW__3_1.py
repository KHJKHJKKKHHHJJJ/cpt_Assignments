from tkinter import *
win = Tk()
win.title("애완동물 선택하기")

dogpt = PhotoImage(file="C:/Users/Hanbit/OneDrive - 우송대학교(WOOSONG UNIVERSITY)/PyFiles/ref_data/exjpeg/dog.gif")
catpt = PhotoImage(file="C:/Users/Hanbit/OneDrive - 우송대학교(WOOSONG UNIVERSITY)/PyFiles/ref_data/exjpeg/cat.gif")
rabpt = PhotoImage(file="C:/Users/Hanbit/OneDrive - 우송대학교(WOOSONG UNIVERSITY)/PyFiles/ref_data/exjpeg/rabbit.gif")

def showpict():
    if chk.get() ==1:
        ptlabel.configure(image=dogpt)
    elif chk.get() == 2:
        ptlabel.configure(image=catpt)
    elif chk.get() == 3:
        ptlabel.configure(image=rabpt)
    else:
        ptlabel.configure(text= "동물을 선택하세요")

Title = Label(win, text="좋아하는 동물 투표", fg="blue", bg=None, font=("궁서체", 30))
chk = IntVar()
dogbt = Radiobutton(win, text="강아지", variable=chk, value=1)
catbt = Radiobutton(win, text="고양이", variable=chk, value=2)
rabbt = Radiobutton(win, text="토끼", variable=chk, value=3)
showbt = Button(win, text="사진 보기", command=showpict)
ptlabel = Label(win, image=None)

Title.pack()
dogbt.pack()
catbt.pack()
rabbt.pack()
showbt.pack()
ptlabel.pack()
win.mainloop()