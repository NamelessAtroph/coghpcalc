from tkinter import *
import tkinter.messagebox as box

#Base
global window
global lvl
global hp
global entry
global checked
global v2
global btn
global label
global box
window=Tk()
window.title("Cog Health Calculator")
window.resizable(0,0)
ico=PhotoImage(file='img/coggear.ico')
window.iconphoto(True, ico)
lvl=IntVar()
hp=IntVar()
entry=Entry(window)
checked=IntVar()
v2=Checkbutton(window,text='V2.0?',\
variable=checked,onvalue=1,offvalue=0)
btn=Button(window,text='Calculate')
label = Label(window,text='...',relief='groove',width=3)

#Calculator
def calc():
	'''Calculates health of a specified cog level'''
	lvl=entry.get()
	lvl=int(lvl)
	if checked.get()==1:
		if lvl<1 or lvl>12:
			box.showerror("Please choose a level that cogs can be.")
		elif lvl==12:
			hp=400
			label.configure(text=str(hp))
		else:
			hp=((lvl+1)*(lvl+2))*2
			label.configure(text=hp)
	else:
		if lvl<1 or lvl>12:
			box.showerror("Please choose a level that cogs can be.")
		elif lvl==12:
			hp=200
			label.configure(text=str(hp))
		else:
			hp=(lvl+1)*(lvl+2)
			label.configure(text=str(hp))

btn.configure(command=calc)

#Geometry
label.grid()
entry.grid()
v2.grid()
btn.grid()

#Run
window.mainloop()