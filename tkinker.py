####Pillow###
from PIL import *
from PIL import ImageTk
import os
import PIL.Image
#### tkinter ####

import tkinter as tk

from tkinter import *
from tkinter import filedialog

#### Variablen 

file_auswahl = input("Give me your filename: ")
mysuffix = (".JPG", ".jpg")
#myfilepath = input("Please enter the commplet Path for you File: ")
file_output = "/Users/morei/Desktop/file_converter/Output/"
file_input = "/Users/morei/Desktop/file_converter/Input/"
#file_format = input("Wich File format do you want example formats ( JPG/JPEG, PNG, PSD, PDF) ?")


root = tk.Tk()
root.withdraw()
root.iconbitmap('/Users/morei/Desktop')

root.filename = filedialog.askopenfilename(initialdir="/Users/morei/Desktop", title="Select yout File")

my_file = Label(root, text=root.filename).pack()
my_image = ImageTk.PhotoImage(PIL.Image.open(root.filename))
my_image_label = Label(image=my_image).pack()

print(root.filename)

root.mainloop()

def check():
    for f in os.listdir(file_input):
        if f.endswith(mysuffix):
            print(f)


def change():
     if os.path.isfile(file_input + file_auswahl):
        print("This File exists and i gonna be starting converting it! ")
        i = Image.open(file_input + file_auswahl)
        fn, fext = os.path.splitext(file_auswahl)
        print("Starting Converting")
        i.save(file_output + '{}.png'.format(fn))
        print("Succsesfully convertet")

#change()