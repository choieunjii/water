from tkinter import *

w = Tk()
label1= Label(w, text="label1", bg="#FF0000")
label2= Label(w, text="label2", bg="#00FF00")
label3= Label(w, text="label3", bg="#0000FF")
label1.pack(side=BOTTOM)
label2.pack(side=BOTTOM)
label3.pack(side=BOTTOM)

w.mainloop()