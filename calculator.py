from tkinter import *


def Clear():
	textDisplay.delete(0,END)


root = Tk()
root.title("My_Calculator")
root.minsize(width = 300, height = 475)
root.maxsize(width = 300, height = 475)

frame = Frame(root,width = 1000, height = 10)
frame.pack()

num = StringVar()
textDisplay = Entry(frame,textvariable = num , bd=20, insertwidth =1 , font=30)
textDisplay.pack(side = TOP)

b1 = Button(frame, padx = 16 , pady =16 , bd=8, text = "1",fg = "black")
b1.pack(side = LEFT)

b2 = Button(frame, padx = 16 , pady =16 , bd=8, text = "2",fg = "black")
b2.pack(side = LEFT)

b3 = Button(frame, padx = 16 , pady =16 , bd=8, text = "3",fg = "black")
b3.pack(side = LEFT)

b4 = Button(frame, padx = 16 , pady =16 , bd=8, text = "(",fg = "black")
b4.pack(side = LEFT)

b4 = Button(frame, padx = 16 , pady =16 , bd=8, text = ")",fg = "black")
b4.pack(side = LEFT)

frame1 = Frame(root)
frame1.pack(side = TOP)
b5 = Button(frame1, padx = 16 , pady =16 , bd=8, text = "4",fg = "black")
b5.pack(side = LEFT)

b6 = Button(frame1, padx = 16 , pady =16 , bd=8, text = "5",fg = "black")
b6.pack(side = LEFT)

b7 = Button(frame1, padx = 16 , pady =16 , bd=8, text = "6",fg = "black")
b7.pack(side = LEFT)

b8 = Button(frame1, padx = 16 , pady =16 , bd=8, text = "+",fg = "black")
b8.pack(side = LEFT)

b8 = Button(frame1, padx = 16 , pady =16 , bd=8, text = "-",fg = "black")
b8.pack(side = LEFT)



frame2 = Frame(root)
frame2.pack(side = TOP)

b5 = Button(frame2, padx = 16 , pady =16 , bd=8, text = "7",fg = "black")
b5.pack(side = LEFT)

b5 = Button(frame2, padx = 16 , pady =16 , bd=8, text = "8",fg = "black")
b5.pack(side = LEFT)

b5 = Button(frame2, padx = 16 , pady =16 , bd=8, text = "9",fg = "black", command = Clear)
b5.pack(side = LEFT)

b5 = Button(frame2, padx = 16 , pady =16 , bd=8, text = "/",fg = "black")
b5.pack(side = LEFT)

b5 = Button(frame2, padx = 16 , pady =16 , bd=8, text = "*",fg = "black")
b5.pack(side = LEFT)


frame3 =Frame(root)
frame3.pack(side = TOP)

b5 = Button(frame3, padx = 16 , pady =16 , bd=8, text = ".",fg = "black")
b5.pack(side = LEFT)

b5 = Button(frame3, padx = 16 , pady =16 , bd=8, text = "0",fg = "black")
b5.pack(side = LEFT)

b5 = Button(frame3, padx = 16 , pady =16 , bd=8, text = "CE",fg = "black",command = Clear)
b5.pack(side = LEFT)

b5 = Button(frame3, padx = 16 , pady =16 , bd=8, text = "C",fg = "black",command = Clear)
b5.pack(side = LEFT)

b5 = Button(frame3, padx = 16 , pady =16 , bd=8, text = "=",fg = "black")
b5.pack(side = LEFT)

frame4 = Frame(root)
frame4.pack(side = TOP)

b8 = Button(frame4, padx = 16 , pady =16 , bd=8, text = "sin",fg = "black")
b8.pack(side = LEFT)

b8 = Button(frame4, padx = 16 , pady =16 , bd=8, text = "cos",fg = "black")
b8.pack(side = LEFT)

b8 = Button(frame4, padx = 16 , pady =16 , bd=8, text = "tan",fg = "black")
b8.pack(side = LEFT)

b8 = Button(frame4, padx = 16 , pady =16 , bd=8, text = "^",fg = "black")
b8.pack(side = LEFT)

frame5 = Frame(root)
frame5.pack(side = TOP)

b8 = Button(frame5, padx = 16 , pady =16 , bd=8, text = "cosec",fg = "black")
b8.pack(side = LEFT)

b8 = Button(frame5, padx = 16 , pady =16 , bd=8, text = "sec",fg = "black")
b8.pack(side = LEFT)

b8 = Button(frame5, padx = 16 , pady =16 , bd=8, text = "cot",fg = "black")
b8.pack(side = LEFT)

b8 = Button(frame5, padx = 16 , pady =16 , bd=8, text = "OFF",fg = "black",command=  root.quit)
b8.pack(side = LEFT)






















root.mainloop()