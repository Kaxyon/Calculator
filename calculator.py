from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('Calculator')
root.geometry('250x400+820+300')
root.resizable(False, False)
root.wm_iconbitmap('calculator.ico')

######### Function
val = ''
A = 0
operator = ''


def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)

def btn_plus_isclicked():
    global val
    global A
    global operator
    A = int(val)
    operator = '+'
    val = val + "+"
    data.set(val)

def btn_minus_isclicked():
    global val
    global A
    global operator
    A = int(val)
    operator = '-'
    val = val + "-"
    data.set(val)

def btn_multiply_isclicked():
    global val
    global A
    global operator
    A = int(val)
    operator = '*'
    val = val + "*"
    data.set(val)

def btn_divide_isclicked():
    global val
    global A
    global operator
    A = int(val)
    operator = '/'
    val = val + "/"
    data.set(val)

def btn_c_isclicked():
    global val
    global A
    global operator
    val = ''
    A = 0
    operator = ''
    data.set(val)

def btn_equal_isclicked():
    global val
    global A
    global operator
    val2 = val
    if operator == '+':
        x = int((val2.split('+')[1]))
        C = A + x
        data.set(C)
        val = str(C)
    elif operator == '-':
        x = int((val2.split('-')[1]))
        C = A - x
        data.set(C)
        val = str(C)
    elif operator == '*':
        x = int((val2.split('*')[1]))
        C = A * x
        data.set(C)
        val = str(C)
    elif operator == '/':
        x = int((val2.split('/')[1]))
        if x == 0:
            messagebox.showerror('Error', 'Division by Zero not Allowed')
            A = ''
            val = ''
            data.set(val)
        else:
            C = (A / x)
            data.set(C)
            val = str(C)


###### Label
data =StringVar()

label = Label(
    root, 
    text='Label',
    anchor=SE,
    font='Verdana, 22',
    bg='#ffffff',
    fg='#489C97',
    textvariable=data
)
label.pack(expand=True, fill=BOTH)




row1 = ttk.Frame(root)
row1.pack(expand=True, fill=BOTH)

row2 = ttk.Frame(root)
row2.pack(expand=True, fill=BOTH)

row3 = ttk.Frame(root)
row3.pack(expand=True, fill=BOTH)

row4 = ttk.Frame(root)
row4.pack(expand=True, fill=BOTH)




###### ROW 1

btn1 = Button(
    row1,
    text='1',
    font='Verdana, 22',
    # bg='#000000',
    fg='#489C97',
    relief=GROOVE,
    border=0,
    command=btn_1_isclicked
)
btn1.pack(side=LEFT, expand=True, fill=BOTH)

btn2 = Button(
    row1,
    text='2',
    font='Verdana, 22',
    # bg='#000000',
    fg='#489C97',
    relief=GROOVE,
    border=0,
    command=btn_2_isclicked
)
btn2.pack(side=LEFT, expand=True, fill=BOTH)

btn3 = Button(
    row1,
    text='3',
    font='Verdana, 22',
    # bg='#000000',
    fg='#489C97',
    relief=GROOVE,
    border=0,
    command=btn_3_isclicked
)
btn3.pack(side=LEFT, expand=True, fill=BOTH)

btn4 = Button(
    row1,
    text='+',
    font='Verdana, 22',
    # bg='#000000',
    fg='#489C97',
    relief=GROOVE,
    border=0,
    command=btn_plus_isclicked
)
btn4.pack(side=LEFT, expand=True, fill=BOTH)


###### ROW 2

btn1 = Button(
    row2,
    text='4',
    font='Verdana, 22',
    # bg='#000000',
    fg='#489C97',
    relief=GROOVE,
    border=0,
    command=btn_4_isclicked
)
btn1.pack(side=LEFT, expand=True, fill=BOTH)

btn2 = Button(
    row2,
    text='5',
    font='Verdana, 22',
    # bg='#000000',
    fg='#489C97',
    relief=GROOVE,
    border=0,
    command=btn_5_isclicked
)
btn2.pack(side=LEFT, expand=True, fill=BOTH)

btn3 = Button(
    row2,
    text='6',
    font='Verdana, 22',
    # bg='#000000',
    fg='#489C97',
    relief=GROOVE,
    border=0,
    command=btn_6_isclicked
)
btn3.pack(side=LEFT, expand=True, fill=BOTH)

btn4 = Button(
    row2,
    text='-',
    font='Verdana, 22',
    # bg='#000000',
    fg='#489C97',
    relief=GROOVE,
    border=0,
    command=btn_minus_isclicked
)
btn4.pack(side=LEFT, expand=True, fill=BOTH)


###### ROW 3

btn1 = Button(
    row3,
    text='7',
    font='Verdana, 22',
    # bg='#000000',
    fg='#489C97',
    relief=GROOVE,
    border=0,
    command=btn_7_isclicked
)
btn1.pack(side=LEFT, expand=True, fill=BOTH)

btn2 = Button(
    row3,
    text='8',
    font='Verdana, 22',
    # bg='#000000',
    fg='#489C97',
    relief=GROOVE,
    border=0,
    command=btn_8_isclicked
)
btn2.pack(side=LEFT, expand=True, fill=BOTH)

btn3 = Button(
    row3,
    text='9',
    font='Verdana, 22',
    # bg='#000000',
    fg='#489C97',
    relief=GROOVE,
    border=0,
    command=btn_9_isclicked
)
btn3.pack(side=LEFT, expand=True, fill=BOTH)

btn4 = Button(
    row3,
    text='*',
    font='Verdana, 22',
    # bg='#000000',
    fg='#489C97',
    relief=GROOVE,
    border=0,
    command=btn_multiply_isclicked
)
btn4.pack(side=LEFT, expand=True, fill=BOTH)

###### ROW 4

btn1 = Button(
    row4,
    text='C',
    font='Verdana, 22',
    # bg='#000000',
    fg='#489C97',
    relief=GROOVE,
    border=0,
    command=btn_c_isclicked
)
btn1.pack(side=LEFT, expand=True, fill=BOTH)

btn2 = Button(
    row4,
    text='0',
    font='Verdana, 22',
    # bg='#000000',
    fg='#489C97',
    relief=GROOVE,
    border=0,
    command=btn_0_isclicked
)
btn2.pack(side=LEFT, expand=True, fill=BOTH)

btn3 = Button(
    row4,
    text='=',
    font='Verdana, 22',
    # bg='#000000',
    fg='#489C97',
    relief=GROOVE,
    border=0,
    command=btn_equal_isclicked
)
btn3.pack(side=LEFT, expand=True, fill=BOTH)

btn4 = Button(
    row4,
    text='/',
    font='Verdana, 22',
    # bg='#000000',
    fg='#489C97',
    relief=GROOVE,
    border=0,
    command=btn_divide_isclicked
)
btn4.pack(side=LEFT, expand=True, fill=BOTH)

root.mainloop()