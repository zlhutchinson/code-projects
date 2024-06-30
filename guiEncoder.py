import time
import random
from tkinter import *
from tkinter.ttk import *

## Window setup
window = Tk()
window.title("Hutchinson Encoder")
window.geometry('306x200')

## In window text
lb0 = Label(window, text="A Simple Text Encoder", font=("Arial Bold", 20))
lb0.grid(column=0, row=0)
lbl = Label(window, text="Encrypt your secret information!", font=("Arial Bold", 12))
lbl.grid(column=0, row=1)
lb2 = Label(window, text="Cipher Key Number", font=("Arial",10))
lb2.grid(column=0, row=6)
lb3 = Label(window, text="", font=("Arial", 10))
lb3.grid(column=0, row=14)
lb4 = Label(window, text="Enter text here:", font=("Arial", 10))
lb4.grid(column=0, row=2)

## Combobox
combo = Combobox(window)
combo['values']= (0, 1, 2, 3,"N/A")
combo.current(4)
combo.grid(column=0, row=8)

## Text entry box
txt = Entry(window, width=20)
txt.grid(column=0, row=4)

## Initiates encoding/decoding process
def clicked():
    comboIn = combo.get()
    textIn = txt.get()
    output = ''
    
    if comboIn != "N/A":
        decoded = decipher(comboIn, textIn)
        for x in range(len(decoded)):
            output += decoded[x]
        
    else:
        keyNum = random.randint(0,3)
        encoded = cipher(keyNum, textIn)
        for x in range(len(encoded)):
            output += encoded[x]
        combo.current(keyNum)
        lb2.configure(text= 'Your New Cipher Key Number')
    txt.delete(0, 'end')
    txt.insert(0, output)

## Resets all fields
def clicked1():
    combo.current(4)
    lb2.configure(text= "Cipher Key Number")
    lb3.configure(text= '')
    txt.delete(0, 'end')

## Buttons
btn = Button(window, text="Submit", command=clicked)
btn.grid(column=0, row=10)
btn1 = Button(window, text="Reset", command=clicked1)
btn1.grid(column=0, row=12)

## Encoding Section
def cipher(num, text):
    newText = []
    if num == 0:
        for char in text:
            newChar = library0(char)
            newText.append(newChar)
        return newText
    elif num == 1:
        for char in text:
            newChar = library1(char)
            newText.append(newChar)
        return newText
    elif num == 2:
        for char in text:
            newChar = library2(char)
            newText.append(newChar)
        return newText
    elif num == 3:
        for char in text:
            newChar = library3(char)
            newText.append(newChar)
        return newText

## Decoding Section
def decipher(num, text):
    num = int(num)
    newText = []
    if num == 0:
        for char in text:
            newChar = unLibrary0(char)
            newText.append(newChar)
        return newText
    if num == 1:
        for char in text:
            newChar = unLibrary1(char)
            newText.append(newChar)
        return newText
    if num == 2:
        for char in text:
            newChar = unLibrary2(char)
            newText.append(newChar)
        return newText
    if num == 3:
        for char in text:
            newChar = unLibrary3(char)
            newText.append(newChar)
        return newText

###############################################################################
#Cipher Libraries
    
## Encoding Libraries
def library0(ch):
    orgList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~']
    libList = ['b','c','d','e','f','g','1','2','3','4','5','6','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~','7','8','9','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a']
    for x in range(len(orgList)):
        ch = ch.lower()
        if ch == orgList[x]:
            ch = libList[x]
            return ch
    else:
        return ch
def library1(ch):
    orgList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~']
    libList = ['c','d','e','f','g','h','i','j','k','l','m','n','o','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~','p','q','r','1','2','3','4','5','6','7','8','9','s','t','u','v','w','x','y','z','a','b']
    for x in range(len(orgList)):
        ch = ch.lower()
        if ch == orgList[x]:
            ch = libList[x]
            return ch
    else:
        return ch
def library2(ch):
    orgList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~']
    libList = ['d','e','f','g','h','i','j','k','l','m','n','o','1','2','3','4','5','6','7','8','9','p','q','r','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~','s','t','u','v','w','x','y','z','a','b','c']
    for x in range(len(orgList)):
        ch = ch.lower()
        if ch == orgList[x]:
            ch = libList[x]
            return ch
    else:
        return ch
def library3(ch):
    orgList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~']
    libList = ['e','f','1','2','3','4','5','6','7','8','9','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~','z','a','b','c','d']
    for x in range(len(orgList)):
        ch = ch.lower()
        if ch == orgList[x]:
            ch = libList[x]
            return ch
    else:
        return ch
    
## Decoding Libraries
def unLibrary0(ch):
    orgList = ['b','c','d','e','f','g','1','2','3','4','5','6','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~','7','8','9','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a']
    libList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~']
    for x in range(len(orgList)):
        ch = ch.lower()
        if ch == orgList[x]:
            ch = libList[x]
            return ch
    else:
        return ch
def unLibrary1(ch):
    orgList = ['c','d','e','f','g','h','i','j','k','l','m','n','o','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~','p','q','r','1','2','3','4','5','6','7','8','9','s','t','u','v','w','x','y','z','a','b']
    libList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~']
    for x in range(len(orgList)):
        ch = ch.lower()
        if ch == orgList[x]:
            ch = libList[x]
            return ch
    else:
        return ch
def unLibrary2(ch):
    orgList = ['d','e','f','g','h','i','j','k','l','m','n','o','1','2','3','4','5','6','7','8','9','p','q','r','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~','s','t','u','v','w','x','y','z','a','b','c']
    libList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~']
    for x in range(len(orgList)):
        ch = ch.lower()
        if ch == orgList[x]:
            ch = libList[x]
            return ch
    else:
        return ch
def unLibrary3(ch):
    orgList = ['e','f','1','2','3','4','5','6','7','8','9','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~','z','a','b','c','d']
    libList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~']
    for x in range(len(orgList)):
        ch = ch.lower()
        if ch == orgList[x]:
            ch = libList[x]
            return ch
    else:
        return ch

#End Libraries
###############################################################################

## Window function to maintain until user close
window.mainloop()