from tkinter import *

window = Tk()
btn = Button(window, bg="#FFDDDD", fg="#FF7171", text="버튼", width="80", height="2")
btn.pack()
window.mainloop()

#rgb(레드, 그린, 블루) -> 0 ~ 255까지를 나타냄(=1 바이트, 2^8) 2/4/8/16/32/128/256 색상표현 16진수
#16진수: 0 1 2 3 4 5 6 a b c d e f (=2^4) / 최대 0~ff까지 사용 / 값이 높을수록 빛이 많은 것(밝은색)
#FF0000(RED), #00FF00(GREEN), #0000FF(BLUE), #000000(BLACK), #FFFFFF(WHITE) (#을 넣어야지 색상)
#red, green, blue, yellow, purple, skyblue, rosegold 