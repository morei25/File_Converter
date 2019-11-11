###Pillow###

from PIL import *

from PIL import ImageTk
from PIL import Image
import PIL.Image

#### tkinter ####

import tkinter as tk

from tkinter import *
from tkinter import filedialog

#### OS Modules ####

import os, glob

#### Variablen ####

file_output = "/Users/morei/Desktop/Output"


#### Tkinter Einstellungen ####

root = tk.Tk()
root.withdraw()
root.iconbitmap('/Users/morei/Desktop')


#### Datei Auswahl ####

root.filename = filedialog.askopenfilenames(initialdir="/Users/morei/Desktop", title="Select your File")
print(root.filename)
root.file_output_path = filedialog.askdirectory(initialdir="/Users/morei/Desktop", title="Select your Output Path/Folder")

print(root.filename)

#### Datei Converter ####

def convert():
    i = PIL.Image.open(root.filename)
    fn, fext = os.path.splitext(root.filename)
    print("Starting Converting")
    file_name = os.path.basename(root.filename)
    file_name_split = os.path.splitext(file_name)
    file_name_final = os.path.splitext(file_name)[0]
    i.save("{}/{}.png".format(root.file_output_path, file_name_final))
    print("Succsesfully convertet")
    

#### Tkinter Fenster ####

window = Tk()
#window.geometry("812x524") # size of the window width:- 500, height:- 375
window.resizable(0, 0) # this prevents from resizing the window
window.title("File Converter")

#### Convert Image to png and after converting close the window/App ####

b = Button(window, text="Convert your File", command=lambda:[convert(),sys.exit()], bg = "red" )
b.config(bg = "red")
b.pack(side = LEFT)

c = Button(window, text = "Exit", command = sys.exit, bg = "Black")
c.config(bg = "Black")
c.pack(side = RIGHT)

window.mainloop()

 


#print("1")
#fenster()
#print("2")
#root.mainloop()

#print("3")

#def savePath(): # select the destination directory to save the images
#        destination.delete(0,END)
#        savePath = filedialog.askdirectory(initialdir=os.getcwd())
#        destination.insert(0,savePath)

#input_frame = Frame(window, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
#input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
#input_field.grid(row = 0, column = 0)
#input_field.pack(ipady = 10)