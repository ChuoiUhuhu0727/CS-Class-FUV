# import
import tkinter as tk

# create main window 
window = tk.Tk()
window.title('Hello calculator')
window.geometry('400x200')

# create entry
n1 = tk.Entry(window, width=30, justify='right', font=('Consolas', 10))
n1.pack()

n2 = tk.Entry(window, width=30, justify='right', font=('Consolas', 10))
n2.pack()

# create button Addition
def do_add():
    val1 = int(n1.get())
    val2 = int(n2.get())
    val1 += val2;
    n1.delete(0, tk.END)
    n2.delete(0, tk.END)
    n1.insert(0, str(val1))
    
button_add = tk.Button(window, text='Add', command=do_add)
button_add.pack()

# create button Subtraction
def do_sub():
    val1 = int(n1.get())
    val2 = int(n2.get())
    val1 -= val2;
    n1.delete(0, tk.END)
    n2.delete(0, tk.END)
    n1.insert(0, str(val1))

button_sub = tk.Button(window, text='Subtract', command=do_sub)
button_sub.pack()

# create button Multiplication
def do_mul():
    val1 = int(n1.get())
    val2 = int(n2.get())
    val1 *= val2;
    n1.delete(0, tk.END)
    n2.delete(0, tk.END)
    n1.insert(0, str(val1))

button_mul = tk.Button(window, text='Multiply', command=do_mul)
button_mul.pack()

# create button Division
def do_div():
    val1 = int(n1.get())
    val2 = int(n2.get())
    val1 /= val2;
    n1.delete(0, tk.END)
    n2.delete(0, tk.END)
    n1.insert(0, str(val1))

button_div = tk.Button(window, text='Divide', command=do_div)
button_div.pack()

# create button Power
def power(x, n):
    s = 1.0;
    for i in range(n):
        s *= x;
    return s;

def do_pow():
    x = float(n1.get())  
    n = int(n2.get())  
    y = power(x, n);               
    n1.delete(0, tk.END)  
    n2.delete(0, tk.END)  
    n1.insert(0, str(y)) 
    
btnPower = tk.Button(frame, text = "Power", command = do_pow)
btnPower.grid(row=1, column=0, padx=10, pady = 10)

# create button Factorial
def factorial(n):
    p = 1
    for i in range(n):
        p *= (i+1)
    return p

def do_factorial():
    val1 = int(float(n1.get()))
    y = factorial(n)
    n1.delete(0, tk.END)
    n2.delete(0, tk.END)
    n1.insert(0, str(y))

button_fac = tk.Button(window, text='Factorial', command=do_factorial)
button_fac.pack()

# Loop
window.mainloop()