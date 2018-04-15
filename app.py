from Tkinter import *
from tkFileDialog import askopenfilename
from PIL import ImageTk, Image
import os

def predict_action():
    os.system('python /home/dan/Desktop/pythonDev/models/tutorials/image/imagenet/classify_image.py ' + "'"+e1.get()+"'")
    file = open("output.txt", "r")
    output.set(file.read())

def open_action():
   filename = askopenfilename(parent=master, initialdir='C:\\')
   head, tail = os.path.split(filename)
   filePath.set(tail)
   loadImage(tail)

   output.set('test')

def loadImage(Tail):
   img = Image.open(Tail)
   img = img.resize((250, 250), Image.ANTIALIAS) #The (250, 250) is (height, width)
   filename = ImageTk.PhotoImage(img)
   canvas = Canvas(master,height=250,width=250)
   canvas.image = filename  # <--- keep reference of your image
   canvas.create_image(0,0,anchor='nw',image=filename)
   canvas.grid(row=1)

master = Tk()

filePath = StringVar(None)
output = StringVar(None)

e1 = Entry(master,textvariable=filePath, width='30', state='disabled')
e1.grid(row=0, column=0)

b1 = Button(master, text="choose image file", command=open_action)
b1.grid(row=0, column=1)

b2 = Button(master, text="Predict", command=predict_action)
b2.grid(row=0, column=2)

l0 = Label(master, text="label", textvariable=output)
l0.grid(row=2)


mainloop( )

