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

root.filename = filedialog.askopenfilename(initialdir="/Users/morei/Desktop", title="Select your File")
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
window.title("File Converter")

#### Convert Image to png and after converting close the window/App ####

b = Button(window, text="Convert your File", command=lambda:[convert(),sys.exit()], bg = "red" )
b.config(bg = "red")
b.pack(side = LEFT)

c = Button(window, text = "Exit", command = sys.exit, bg = "Black")
c.config(bg = "Black")
c.pack(side = RIGHT)


window.mainloop()

 


