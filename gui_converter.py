import kivy
from kivy.app import App
from kivy.uix.button import Button
####Pillow###

from PIL import Image
import os

#### Variablen 

file_auswahl = input("Give me your filename: ")
mysuffix = (".JPG", ".jpg")
myfilepath = input("Please enter the commplet Path for you File: ")
file_output = "/Users/morei/Desktop/Converter/Output/"
fiel_input = "/Users/morei/Desktop/Converter/Input/"
file_format = input("Wich File format do you want example formats ( JPG/JPEG, PNG, PSD, PDF) ?")

class Checker(App):
    
    def build(self):
        btn = Button(text = "Check your Files !",
                    font_size ="20sp", 
                    background_color =(1, 1, 1, 1), 
                    color =(1, 1, 1, 1), 
                    size =(32, 32), 
                    size_hint =(.2, .2), 
                    pos =(300, 250))  

        btn.bind(on_press = self.check)
        return btn

    def check(self,event):
        for f in os.listdir(myfilepath):
            if f.endswith(mysuffix):
                print(f)

    
    def convert(him):
        bot = Button(text = " Convert your File ",
                    font_size ="20sp", 
                    background_color =(1, 1, 1, 1), 
                    color =(1, 1, 1, 1), 
                    size =(32, 32), 
                    size_hint =(.2, .2), 
                    pos =(300, 250))
        bot.bind(on_press = him.change)
        return btn 

    def change(him, event):
     if os.path.isfile(myfilepath + file_auswahl):
        print("This File exists and i gonna be starting converting it! ")
        i = Image.open(myfilepath + file_auswahl)
        fn, fext = os.path.splitext(file_auswahl)
        print("Starting Converting")
        i.save(file_output + '{}.png'.format(fn))
        print("Succsesfully convertet")


root = Checker()
root.run()
