from tkinter import *
window = Tk()
f = Frame(window)
window.geometry("600x100")

b1 = Button(f, text="박스 #1", bg="red", fg="white")
b2 = Button(f, text="박스 #2", bg="green", fg="black")
b3 = Button(f, text="박스 #3", bg="orange", fg="white")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)

l = Label(window, text="이 레이블은 버튼들 위에 배치된다.")

l.pack()
f.pack()

window.resizable(0, 0) # 크기조정불가
window.mainloop()