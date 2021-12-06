from tkinter import *
window = Tk()
window.title("tk")

f1 = Frame(window)
f2 = Frame(window)

l1 = Label(f1, text="너비")
l2 = Label(f1, text="높이")
entry1 = Entry(f1)
entry2 = Entry(f1)
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
f1.grid(row=0, column=0)

l3 = Label(window, text="이미지")
l3.grid(row=0, column=1)

btn1 = Button(window, text="이미지 저장")
btn1.grid(row=1, column=0)

btn2 = Button(f2, text="확대")
btn3 = Button(f2, text="축소")
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
f2.grid(row=1, column=1)

window.mainloop()