# importing whole module
from tkinter import *
from tkinter.ttk import *
#import system time module
from time import strftime
 
# creating tkinter window
root = Tk()
root.title('Digital Clock')
root.resizable(0,0)
 
#Time Display Function

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)
 
 
#Styling The Clock Widgets
lbl = Label(root, font=('calibri', 40, 'bold'),
            background='purple',
            foreground='white')
 
#Set Allignment of clock in tkinter
lbl.pack(anchor='center')
time()
 
mainloop()