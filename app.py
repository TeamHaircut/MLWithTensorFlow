from Tkinter import *
from tkFileDialog import askopenfilename
import os


def predict_action():
    os.system('python /home/dan/Desktop/pythonDev/models/tutorials/image/imagenet/classify_image.py ' + "'"+e1.get()+"'")

def open_action():
   filename = askopenfilename(parent=master, initialdir='C:\\')
   head, tail = os.path.split(filename)
   filePath.set(tail)
#  f = open(filename)
#  f.read()

master = Tk()

filePath = StringVar(None)

e1 = Entry(master,textvariable=filePath, state='disabled')
e1.grid(row=0, column=1)

b1 = Button(master, text="choose image file", command=open_action)
b1.grid(row=0, column=2)

b2 = Button(master, text="Predict", command=predict_action)
b2.grid(row=0, column=3)

mainloop( )

