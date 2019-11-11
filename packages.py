from distutils.core import setup

setup(name="File_Converter",
      version="1.0",
      description="Python File Converter",
      author="Daniel Moreira Marques",
      author_email="Moreira-Marques1@gmx.de")
try:
    import PIL
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'PIL'])
    import PIL

try:
    import tkinter
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'tkinter'])
    import tkinter

print("Succesfull installed requierd Packages")