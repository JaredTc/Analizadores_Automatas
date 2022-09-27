import re

texto = "int numero =43;"
texto2 = "char numero =43;"
texto3 = "double numero =43;"
texto4 = "for a in range ()"
texto5 = "while() numero =43;"
texto6 = "if() numero =43;"
if re.findall("int [ a-zA-Z0-9_=]+;",texto):
    print("Correcto")
else:
    print("No es correcto")

if re.findall("char[ a-zA-Z0-9_=]+;",texto2):
    print("Correcto")
else:
    print("No es correcto")

if re.findall("double[ a-zA-Z0-9_=]+;",texto3):
    print("Correcto")
else:
    print("No es correcto")

if re.findall("for a in range ()",texto4):
    print("Correcto")
else:
    print("No es correcto")
if re.findall("while['('')'  a-zA-Z0-9_=]+;",texto5):
    print("Correcto")
else:
    print("No es correcto")
if re.findall("if['('')' a-zA-Z0-9_=]+;",texto6):
    print("Correcto")
else:
    print("No es correcto")
    