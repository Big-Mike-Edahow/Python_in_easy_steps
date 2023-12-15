# tk_check.py

from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title( 'Check Button Example' )

frame = Frame( window )

var_1 = IntVar()
var_2 = IntVar()
var_3 = IntVar()

book_1 = Checkbutton(frame , text = 'HTML' , variable = var_1 , onvalue = 1 , offvalue = 0)
book_2 = Checkbutton(frame , text = 'CSS' , variable = var_2 , onvalue = 1 , offvalue = 0)
book_3 = Checkbutton(frame , text = 'JS' , variable = var_3 , onvalue = 1 , offvalue = 0)

def dialog() :
	str = 'Your Choice:\n\n'
	if var_1.get() == 1 : str += 'HTML in easy steps \n'
	if var_2.get() == 1 : str += 'CSS in easy steps \n'
	if var_3.get() == 1 : str += 'JavaScript in easy steps \n'
	box.showinfo('Selection' , str)

btn = Button(frame , text = 'Choose' , command = dialog)

btn.pack(side = RIGHT , padx = 10)
book_1.pack(side = LEFT)
book_2.pack(side = LEFT)
book_3.pack(side = LEFT)
frame.pack(padx = 50, pady = 50)

window.mainloop()

