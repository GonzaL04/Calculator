from tkinter import *
from unittest import result

window = Tk()
window.title("Calculadora")

window.config(bg="#484747")

i = 0

#Input

i_text = Entry(window, font=("Calibri 20"))
i_text.grid (row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

#Functions
    
def clickButton(value):
    global i
    i_text.insert(i, value)
    i += 1

def Delete():
    i_text.delete(0, END)
    i = 0

def Operations ():
    equation = i_text.get()
    total = eval(equation)
    i_text.delete(0, END)
    i_text.insert(0, total)
    i = 0


#Button

button1 = Button(window, text = "1", width = 5, height = 2, command = lambda : clickButton(1))
button2 = Button(window, text = "2", width = 5, height = 2, command = lambda : clickButton(2))
button3 = Button(window, text = "3", width = 5, height = 2, command = lambda : clickButton(3))
button4 = Button(window, text = "4", width = 5, height = 2, command = lambda : clickButton(4))
button5 = Button(window, text = "5", width = 5, height = 2, command = lambda : clickButton(5))
button6 = Button(window, text = "6", width = 5, height = 2, command = lambda : clickButton(6))
button7 = Button(window, text = "7", width = 5, height = 2, command = lambda : clickButton(7))
button8 = Button(window, text = "8", width = 5, height = 2, command = lambda : clickButton(8))
button9 = Button(window, text = "9", width = 5, height = 2, command = lambda : clickButton(9))
button0 = Button(window, text = "0", width = 13, height = 2, command = lambda : clickButton(0))

buttonDel = Button(window, text = "AC", width = 5, height = 2, command = lambda : Delete())
buttonParenthesis1 = Button(window, text = "(", width = 5, height = 2, command = lambda : clickButton("("))
buttonParenthesis2 = Button(window, text = ")", width = 5, height = 2, command = lambda : clickButton(")"))
buttonDot = Button(window, text = ".", width = 5, height = 2, command = lambda : clickButton("."))

buttonDiv = Button(window, text = "/", width = 5, height = 2, command = lambda : clickButton("/"))
buttonMul = Button(window, text = "x", width = 5, height = 2, command = lambda : clickButton("*"))
buttonAdd = Button(window, text = "+", width = 5, height = 2, command = lambda : clickButton("+"))
buttonSub = Button(window, text = "-", width = 5, height = 2, command = lambda : clickButton("-"))
buttonTot = Button(window, text = "=", width = 5, height = 2, command = lambda : Operations())

#Buttons on window

buttonDel.grid(row = 1, column = 0, padx = 5, pady = 5)
buttonParenthesis1.grid(row = 1, column = 1, padx = 5, pady = 5)
buttonParenthesis2.grid(row = 1, column = 2, padx = 5, pady = 5)
buttonDiv.grid(row = 1, column = 3, padx = 5, pady = 5)

button7.grid(row = 2, column = 0, padx = 5, pady = 5)
button8.grid(row = 2, column = 1, padx = 5, pady = 5)
button9.grid(row = 2, column = 2, padx = 5, pady = 5)
buttonMul.grid(row = 2, column = 3, padx = 5, pady = 5)

button4.grid(row = 3, column = 0, padx = 5, pady = 5)
button5.grid(row = 3, column = 1, padx = 5, pady = 5)
button6.grid(row = 3, column = 2, padx = 5, pady = 5)
buttonAdd.grid(row = 3, column = 3, padx = 5, pady = 5)

button1.grid(row = 4, column = 0, padx = 5, pady = 5)
button2.grid(row = 4, column = 1, padx = 5, pady = 5)
button3.grid(row = 4, column = 2, padx = 5, pady = 5)
buttonSub.grid(row = 4, column = 3, padx = 5, pady = 5)

button0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
buttonDot.grid(row = 5, column = 2, padx = 5, pady = 5)
buttonTot.grid(row = 5, column = 3, padx = 5, pady = 5)



window.mainloop()