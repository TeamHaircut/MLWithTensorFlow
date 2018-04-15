from Tkinter import *
from tkFileDialog import askopenfilename
import os


def predict_action():
    os.system('python /home/dan/Desktop/pythonDev/models/tutorials/image/imagenet/classify_image.py ' + "'"+e1.get()+"'")
    file = open("output.txt", "r") 
#    print file.read() 
    output.set(file.read())

def open_action():
   filename = askopenfilename(parent=master, initialdir='C:\\')
   head, tail = os.path.split(filename)
   filePath.set(tail)

master = Tk()

filePath = StringVar(None)
output = StringVar(None)

e1 = Entry(master,textvariable=filePath, state='disabled')
e1.grid(row=0, column=0)

b1 = Button(master, text="choose image file", command=open_action)
b1.grid(row=0, column=1)

b2 = Button(master, text="Predict", command=predict_action)
b2.grid(row=0, column=2)

l0 = Label(master, text="label", textvariable=output)
l0.grid(row=1)

mainloop( )

