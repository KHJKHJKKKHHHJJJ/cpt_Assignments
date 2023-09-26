from tkinter import *

fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]
photoList = [None] * 9
num = 0

def clickNext() :
       global num
       num += 1
       if num > 8 :
             num = 0
       pLabel.configure(text=fnameList[num])
def clickPrev() :
       global num
       num -= 1
       if num < 0 :
             num = 8
       pLabel.configure(text=fnameList[num])

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clickNext)

pLabel = Label(window, text=fnameList[num], font=("궁서체", 30))  

btnPrev.place(x = 100, y = 10)
btnNext.place(x = 600, y = 10)
pLabel.place(x = 290, y = 10)

window.mainloop()
