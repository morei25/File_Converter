from PIL import Image
import os

#file_name = input.lower()

#for f in os.listdir('.'):
#    if f.endswith.(file_name):
#        f.lower()
#        i = Image.open(f)
#        fn, fext = os.path.splitext(f)
#        i.save('pngs/{}.png' .format(fn))

##image = Image.open('daniel_mm.jpg')
#image.show()

file_auswahl = input("Give me your filename: ")
mysuffix = (".JPG", ".jpg")
myfilepath = input("Please enter the commplet Path for you File: ")
file_output = "/Users/morei/Desktop/Converter_Output/"
file_format = input("Wich File format do you want example formats ( JPG/JPEG, PNG, PSD, PDF) ?") 

def find_file(file_auswahl):
    options = [ i for i in commands if i.startswith(file_auswahl)]
    if len(options):
        return options 
    else: 
        return None
    

def check():
    for f in os.listdir(myfilepath):
        if f.endswith(mysuffix):
            print(f)

check()




def change():
     if os.path.isfile(myfilepath + file_auswahl):
        print("This File exists and i gonna be starting converting it! ")
        i = Image.open(myfilepath + file_auswahl)
        fn, fext = os.path.splitext(file_auswahl)
        print("Starting Converting")
        i.save(file_output + '{}.png'.format(fn))
        print("Succsesfully convertet")

change()