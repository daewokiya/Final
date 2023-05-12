from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Final 1')
root.geometry("255x250")
root.resizable(False, False)

previous_expression = ""
expression = ""


def press(num):
    global expression, equation
    # Adds the contents to the equation/expression
    expression = expression + str(num)
    equation.set(expression)


def equalPress():
    global expression
    # When pressing the equals sign, evaluate the function and then convert to string
    try:
        total = str(eval(expression))
        previous_answer = '= ' + str(total)
        previous_expression.set(previous_answer)
        equation.set(total)
        expression = ""

    # General error handling
    except:
        equation.set(" Error ")
        expression = ""


def clear():
    global expression
    # When pressing the clear button, delete all from the expression and equation
    expression = ""
    equation.set("")


def calculate(*args):
    if choices.get() == 'meters':
        try:
            value = float(inp.get())
            result.set(str(int(value * 3.281 * 10000.0 + 0.5) / 10000.0))
            units.set('feet')
        except:
            convClear()
            result.set('ERROR')
    if choices.get() == 'feet':
        try:
            value = float(inp.get())
            result.set(str(int(value * 0.3048 * 10000.0 + 0.5) / 10000.0))
            units.set('meters')
        except:
            convClear()
            result.set('ERROR')


def convClear():
    inp.set('')
    choice.set('')
    result.set('')
    units.set('')


notebook = ttk.Notebook(root)
notebook.pack(pady=5)

frame1 = Frame(notebook, width=255, height=220, bg='#858585')
frame2 = Frame(notebook, width=255, height=220, bg='#858585')

frame1.pack(fill="both", expand=1)
frame2.pack(fill="both", expand=1)

notebook.add(frame1, text='Calculator')
notebook.add(frame2, text='Converter')

# Entry and previous answer display
equation = StringVar()
expression_field = Entry(frame1, width=25, bd=9, textvariable=equation, bg='white', fg='black',
                         font=('Noto Sans Mono', 12), justify=RIGHT)
expression_field.grid(row=1, column=0, columnspan=4, pady=1, padx=2, sticky=W)

previous_expression = StringVar()
preAns_field = Label(frame1, textvariable=previous_expression, bg='#858585', fg='#ff9900',
                     font=('Noto Sans Mono Bold', 10))
preAns_field.grid(row=0, column=0, sticky=E, columnspan=4)

# Add number and decimal button
button1 = Button(frame1, text='1', fg='black', bg='white', command=lambda: press(1), height=1, width=7)
button1.grid(row=4, column=0, pady=2)

button2 = Button(frame1, text='2', fg='black', bg='white', command=lambda: press(2), height=1, width=7)
button2.grid(row=4, column=1, pady=2)

button3 = Button(frame1, text='3', fg='black', bg='white', command=lambda: press(3), height=1, width=7)
button3.grid(row=4, column=2, pady=2)

button4 = Button(frame1, text='4', fg='black', bg='white', command=lambda: press(4), height=1, width=7)
button4.grid(row=5, column=0, pady=2)

button5 = Button(frame1, text='5', fg='black', bg='white', command=lambda: press(5), height=1, width=7)
button5.grid(row=5, column=1, pady=2)

button6 = Button(frame1, text='6', fg='black', bg='white', command=lambda: press(6), height=1, width=7)
button6.grid(row=5, column=2, pady=2)

button7 = Button(frame1, text='7', fg='black', bg='white', command=lambda: press(7), height=1, width=7)
button7.grid(row=6, column=0, pady=2)

button8 = Button(frame1, text='8', fg='black', bg='white', command=lambda: press(8), height=1, width=7)
button8.grid(row=6, column=1, pady=2)

button9 = Button(frame1, text='9', fg='black', bg='white', command=lambda: press(9), height=1, width=7)
button9.grid(row=6, column=2, pady=2)

button0 = Button(frame1, text='0', fg='black', bg='white', command=lambda: press(0), height=1, width=7)
button0.grid(row=7, column=1, pady=2)

decimal = Button(frame1, text='.', fg='black', bg='white', command=lambda: press('.'), height=1, width=7)
decimal.grid(row=7, column=0, pady=2)

# add formula buttons
clear = Button(frame1, text='Clear', fg='black', bg='#e68a00', command=clear, height=1, width=7)
clear.grid(row=3, column=0, pady=2)

equal = Button(frame1, text='=', fg='black', bg='#00b3b3', command=equalPress, height=1, width=7)
equal.grid(row=7, column=2, pady=2)

addition = Button(frame1, text='+', fg='black', bg='white', command=lambda: press(" + "), height=1, width=7)
addition.grid(row=3, column=3, pady=2)

subtraction = Button(frame1, text='-', fg='black', bg='white', command=lambda: press(" - "), height=1,
                     width=7)
subtraction.grid(row=4, column=3, pady=2)

multiplication = Button(frame1, text='*', fg='black', bg='white', command=lambda: press(" * "), height=1,
                        width=7)
multiplication.grid(row=5, column=3, pady=2)

division = Button(frame1, text='/', fg='black', bg='white', command=lambda: press(" / "), height=1, width=7)
division.grid(row=6, column=3, pady=2)

exponent = Button(frame1, text='**', fg='black', bg='white', command=lambda: press(' ** '), height=1,
                  width=7)
exponent.grid(row=7, column=3, pady=2)

left_parentheses = Button(frame1, text='(', fg='black', bg='white', command=lambda: press('('), height=1,
                          width=7)
left_parentheses.grid(row=3, column=1, pady=2)

right_parentheses = Button(frame1, text=')', fg='black', bg='white', command=lambda: press(')'), height=1,
                           width=7)
right_parentheses.grid(row=3, column=2, pady=2)

inp = StringVar()
choice = StringVar()
result = StringVar()
units = StringVar()

FMFrame = LabelFrame(frame2, text='Enter Feet / Meters', font=('Noto Sans Mono', 10), bg='#858585')
FMFrame.grid(row=0, column=0, padx=20, pady=20, columnspan=4)

input1 = Entry(FMFrame, width=10, textvariable=inp, font=('Noto Sans Mono', 10))
input1.grid(row=1, column=0, padx=5, pady=5)
choices = ttk.Combobox(FMFrame, width=7, textvariable=choice, values=('meters', 'feet'), font=('Noto Sans Mono', 10) ,
                       state="readonly")
choices.grid(row=1, column=1, padx=5, pady=5)

equalFrame = LabelFrame(FMFrame, text='Is equal to', font=('Noto Sans Mono', 10), bg='#858585')
equalFrame.grid(row=2, column=0, padx=20, pady=20, columnspan=4)
Label(equalFrame, textvariable=result, font=('Noto Sans Mono', 10), bg='#858585').grid(row=0, column=0, sticky='e')
Label(equalFrame, textvariable=units, font=('Noto Sans Mono', 10), bg='#858585').grid(row=0, column=1, sticky='w')

Button(frame2, text='Calculate', command=calculate, font=('Noto Sans Mono', 10), bg='#00b3b3').grid(row=2, column=0)
Button(frame2, text='Clear', command=convClear, font=('Noto Sans Mono', 10), bg='#e68a00').grid(row=2, column=2)

for child in frame2.winfo_children():
    child.grid_configure(padx=35, pady=5)

root.mainloop()
