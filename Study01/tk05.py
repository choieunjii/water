from tkinter import *
window = Tk()

b1 = Button(window, text="박스 #1", bg="red", fg="white") #Button : 객체(첫글자가 대문자)를 만들어라
b2 = Button(window, text="박스 #2", bg="green", fg="white")
b3 = Button(window, text="박스 #3", bg="orange", fg="white")
b4 = Button(window, text="박스 #4", bg="pink", fg="white")

b1.grid(row=0, column=0) #0행0열 #grid : (소문자)실행하라!, 격자배치관리자(grid): 위젯(버튼, 레이블 등)을 테이블 형태로 배치
b2.grid(row=0, column=1) #0행1열 # row(행), column(열)
b3.grid(row=1, column=0) #1행0열
b4.grid(row=1, column=1) #1행1열

window.mainloop()