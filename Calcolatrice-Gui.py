from tkinter import *
from tkinter import ttk
import tkinter as tk
from decimal import Decimal

operazione = 0
num_1 = 0
num_2 = 0
risultato = "NaN"



def num1():
    global num_1
    global num_2
    if operazione == 0:
     num_1 = str(num_1) + "1"
    else:
     num_2 = str(num_2) + "1"

def num2():
    global num_1
    global num_2
    if operazione == 0:
     num_1 = str(num_1) + "2"
    else:
     num_2 = str(num_2) + "2"

def num3():
    global num_1
    global num_2
    if operazione == 0:
     num_1 = str(num_1) + "3"
    else:
     num_2 = str(num_2) + "3"

def num4():
    global num_1
    global num_2
    if operazione == 0:
     num_1 = str(num_1) + "4"
    else:
     num_2 = str(num_2) + "4"

def num5():
    global num_1
    global num_2
    if operazione == 0:
     num_1 = str(num_1) + "5"
    else:
     num_2 = str(num_2) + "5"

def num6():
    global num_1
    global num_2
    if operazione == 0:
     num_1 = str(num_1) + "6"
    else:
     num_2 = str(num_2) + "6"

def num7():
    global num_1
    global num_2
    if operazione == 0:
     num_1 = str(num_1) + "7"
    else:
     num_2 = str(num_2) + "7"

def num8():
    global num_1
    global num_2
    if operazione == 0:
     num_1 = str(num_1) + "8"
    else:
     num_2 = str(num_2) + "8"

def num9():
    global num_1
    global num_2
    if operazione == 0:
     num_1 = str(num_1) + "9"
    else:
     num_2 = str(num_2) + "9"

def num0():
    global num_1
    global num_2
    if operazione == 0:
     num_1 = str(num_1) + "0"
    else:
     num_2 = str(num_2) + "0"

def numpunto():
    global num_1
    global num_2
    if operazione == 0:
     num_1 = str(num_1) + "."
    else:
     num_2 = str(num_2) + "."

def plus():
  global operazione
  operazione = 1

def meno():
  global operazione
  operazione = 2

def diviso():
  global operazione
  operazione = 3

def per():
  global operazione
  operazione = 4
  
    
def excoperazione():
  global operazione
  global risultato
  global num_1
  global num_2
  if operazione == 1:
    risultato = (Decimal(num_1)) + (Decimal(num_2))
  if operazione == 2:
    risultato = (Decimal(num_1)) - (Decimal(num_2))
  if operazione == 3:
    risultato = (Decimal(num_1)) / (Decimal(num_2))
  if operazione == 4:
    risultato = (Decimal(num_1)) * (Decimal(num_2))
    


  print(num_2)
  print(num_1)
  print(risultato)

  text = risultato
  text_output = tk.Label(window, text=text, fg="black", font=("Helvetica", 16))
  text_output.grid(row=2, column=2)
  
  if risultato > 0:
    num_2 = 0
    num_1 = 0
    operazione = 0
  

def cancel():
  global num_1, num_2, operazione, risultato
  num_2 = 0
  num_1 = 0
  operazione = 0
  risultato = 0
  text = risultato
  text_output = tk.Label(window, text=text, fg="black", font=("Helvetica", 16))
  text_output.grid(row=2, column=2)

 


window = tk.Tk()
root = Tk()
window.resizable(False, False)
window.title("Calcolatrice")
root.withdraw()

ttk.Label(text=" ").grid(column=1, row=1)
ttk.Label(text="risultato:").grid(column=1, row=2)
ttk.Label(text=" ").grid(column=1, row=3)


ttk.Button(text=0, command=num0).grid(column=2, row=7)
ttk.Button(text=1, command=num1).grid(column=1, row=4)
ttk.Button(text=2, command=num2).grid(column=2, row=4)
ttk.Button(text=3, command=num3).grid(column=3, row=4)
ttk.Button(text=4, command=num4).grid(column=1, row=5)
ttk.Button(text=5, command=num5).grid(column=2, row=5)
ttk.Button(text=6, command=num6).grid(column=3, row=5)
ttk.Button(text=7, command=num7).grid(column=1, row=6)
ttk.Button(text=8, command=num8).grid(column=2, row=6)
ttk.Button(text=9, command=num9).grid(column=3, row=6)
ttk.Button(text="+", command=plus).grid(column=4, row=4)
ttk.Button(text="-", command=meno).grid(column=4, row=5)
ttk.Button(text="*", command=per).grid(column=4, row=6)
ttk.Button(text="/", command=diviso).grid(column=4, row=7)
ttk.Button(text="=", command=excoperazione).grid(column=3, row=7)
ttk.Button(text=".", command=numpunto).grid(column=1, row=7)
ttk.Button(text="C", command=cancel).grid(column=1, row=3)
root.mainloop()