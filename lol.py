from PIL import Image
import glob, os

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
#file_format = input("Wich File format do you want example formats ( JPG/JPEG, PNG, PSD, PDF) ?") 

#def find_file(file_auswahl):
    #options = [ i for i in comands if i.startswith(file_auswahl)]
    #if len(options):
    #    return options 
    #else: 
    #    return None

#find_file(file_auswahl)

def find_file(file_auswahl):
    os.chidr(myfilepath)
    for file in glob.glob("*.jpg"):
        print(file)

find_file()    

def check():
    for f in os.listdir(myfilepath):
        if f.endswith(mysuffix):
            print(f)

check()

def convert():
    for f in os.listdir('.'):
        if f.endswith(mysuffix):
            i = Image.open(f)
            fn, fext = os.path.splitext(f)
            print("Starting Converting")
            i.save('pngs/{}.png'.format(fn))
            print("Succsesfully convertet")


def change():
     if os.path.isfile(myfilepath + file_auswahl):
        print("This File exists and i gonna be starting converting it! ")
        i = Image.open(myfilepath + file_auswahl)
        fn, fext = os.path.splitext(file_auswahl)
        print("Starting Converting")
        i.save(file_output + '{}.png'.format(fn))
        print("Succsesfully convertet")

change()