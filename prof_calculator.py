import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Hello Calculator")
window.geometry("400x300")  # Set window size

# Create entries (for user input)
num1 = tk.Entry(window, width=30, justify='right', font=("Consolas", 14))
num1.pack(pady = 5)
num2 = tk.Entry(window, width=30, justify='right', font=("Consolas", 14))
num2.pack(pady = 5)

# Calculate Addition
def do_add():
    n1 = int(num1.get())  
    n2 = int(num2.get())  
    n1 += n2;               
    num1.delete(0, tk.END)  
    num2.delete(0, tk.END)   
    num1.insert(0, str(n1)) 

# Calculate Subtraction
def do_sub():
    n1 = int(num1.get())
    n2 = int(num2.get())
    n1 -= n2; # Subtract and store in n1
    num1.delete(0, tk.END)
    num2.delete(0, tk.END)
    num1.insert(0, str(n1))

# Calculate Multiplication
def do_mul():
    n1 = int(num1.get())  # Get number from entry 1
    n2 = int(num2.get())  # Get number from entry 2
    n1 *= n2;               # Multiply and store in n1
    num1.delete(0, tk.END)  # Delete entry content
    num2.delete(0, tk.END)  # Delete entry content 
    num1.insert(0, str(n1)) # Set the result in entry 1
 
# Calculate Division    
def do_div():
    n1 = int(num1.get())
    n2 = int(num2.get())
    
    if n2 == 0:  # Avoid denominator as 0
        num1.delete(0, tk.END)
        num1.insert(0, "Cant divide by 0")
        
    result = n1/n2; # Divide and store in result 
    num1.delete(0, tk.END)
    num2.delete(0, tk.END)
    num1.insert(0, str(result))
    
# Calculate Power 
def power(x, n):
    s = 1 # Start sum with first value = 1
    for i in range(n):
        s *= x
    return s

def do_pow():
    x = float(num1.get())  
    n = int(num2.get()) 
    y = power(x, n);               
    num1.delete(0, tk.END) 
    num2.delete(0, tk.END)   
    num1.insert(0, str(y)) 

# Calculate Factorial
def factorial(n):
    p = 1
    for i in range(n):
        p *= (i+1) # Calculate next term after each iteration 
    return p

def do_factorial():
    n = int(num1.get())  
    y = factorial(n);               
    num1.delete(0, tk.END)  
    num2.delete(0, tk.END)  
    num1.insert(0, str(y)) 
    
# Calculate Exponential 
def exp(x):
    sum_exp = 1 # Start sum with first value = 1
    term = 1 # First term = 1
    for n in range(1, 11):
        term *= x/n # Calculate term after each iteration 
        sum_exp += term # Sum terms after each iteration
    return sum_exp

def do_exp():
    x = float(num1.get())  
    y = exp(x);               
    num1.delete(0, tk.END) 
    num1.insert(0, str(y)) 

# Calculate Natural Logarithm 
def loga(x):
    if x <= 0: # Because log is not for non-positive numbers
        return "Error"
    elif x == 1: # Be aware of special case: ln(1) = 0
        return 0
    
    # Find highest n that 2**n < x < 2**(n+1)
    n = 0
    while x >= 2: # Explain: Smallest n = 0 -> x > 2**0=1
        x /= 2
        n += 1
    
    # Calculate ln(y) by the Taylor series
    # for ln(1 + y), where y = x - 1
    y = x - 1
    term = y # Assign 1st value for iteration
    sum_ln = y # The first term is y, so we start with y
    for i in range(2, 111): # Start iteration from second term
        term *= -y * (i-1)/i # Update term after each iteration
        sum_ln += term

    # Calculate ln(x) = ln(y) + n * ln(2)
    ln_x = sum_ln + n * 0.69314718056 # Value of ln(2)
    
    # Check if integer
    if ln_x.is_integer():
        return int(ln_x)  
    else:
        return round(ln_x, 6) 
       
def do_loga():
    try:
        x = float(num1.get())  
        y = loga(x)             
        num1.delete(0, tk.END) 
        num1.insert(0, str(y))
    except ValueError:
        num1.delete(0, tk.END)
        num1.insert(0, "Error") # Return "Error" on input box

# Define global value 
radian = None # Avoid a default value of 0 accidentally 

# Convert degree to radian
def convert_to_r():
    global radian
    try: 
        degree = float(num1.get())
        radian = degree * (3.14159 / 180) # Math formula
        num1.delete(0, tk.END)
        num1.insert(0, str(round(radian, 10)))
    except ValueError:
        num1.delete(0, tk.END)
        num1.insert(0, "Error")
 
# calculate sine       
def sin(x):
    s = x
    p = x
    for n in range(1, 11):
        p *= -x/(2*n) * x/(2*n+1) # algorithm of sine series 
        s += p
    return s

def do_sin():
    global radian # Make sure radian can be executed everywhere
    if radian is not None: 
        try:      
            result = sin(radian)
            num1.delete(0, tk.END)
            num1.insert(0, str(result))
        except ValueError:
            num1.delete(0, tk.END)
            num1.insert(0, "Error")
    else:
        num1.delete(0, tk.END)
        num1.insert(0, "Convert plz")

# Calculate cosine     
def cos(x):
    sum_cos = 1  # First term of the series is cos(0) = 1
    term = 1  # Hold term value
    for n in range(1, 11):  # Loop for 10 terms
        term *= -x**2 / (2*n*(2*n - 1))  # Update term after each iteration
        sum_cos += term  # Add the term to the sum
    return sum_cos

def do_cos():
    global radian # Radian can be executed everywhere
    if radian is not None: 
        try:      
            result = cos(radian) 
            num1.delete(0, tk.END)
            num1.insert(0, str(result))
        except ValueError:
            num1.delete(0, tk.END)
            num1.insert(0, "Error")
    else: 
        num1.delete(0, tk.END)
        num1.insert(0, "Convert plz") # Print on input box

# Calculate tangent
def tan(x):
    sin_value = sin(x) # Calculate sine and cosine
    cos_value = cos(x)

    if cos_value == 0:  # Avoid denominator as 0
        return "undefined"

    return sin_value / cos_value  # Return the tangent value

def do_tan():
    global radian
    if radian is not None:
        try:
            result = tan(radian)
            num1.delete(0, tk.END)
            if result == "Undefined":
                num1.insert(0, "Undefined")
            else:
                num1.insert(0, str(round(result, 10)))
        except ValueError:
            num1.delete(0, tk.END)
            num1.insert(0, "Error")
    else:
        num1.delete(0, tk.END)
        num1.insert(0, "Convert plz") # Print on input box
        
# Calculate Arctan
def arctan(x):
    s = x # start with first value = x
    p = x
    for n in range(1, 1001):
        p *= - x*x*(2*n-1)/(2*n+1) # calculate each term after each iteration
        s += p # sum all terms 
    return s 
    
def do_arctan():
    try:
        x = float(num1.get())
        if x > 1:  # If x is greater than 1, use this formula
            result = (3.14159 / 2) - arctan(1 / x)
        else:
            result = arctan(x)  # Directly use arctan function
        num1.delete(0, tk.END)
        num1.insert(0, str(round(result, 6)))  # Round result for better readability
    except ValueError as e:
        num1.delete(0, tk.END)
        num1.insert(0, str(e))  # Show error message in Terminal
        
# Reset Button
def reset():  
        num1.delete(0, tk.END) # delete value in input box 1
        num2.delete(0, tk.END) # delete value in input box 2
        
# Button Setup 
frame = tk.Frame(window, bg="lightblue", width=300, height=200)
frame.pack(padx=10, pady=10)  # Place the frame using the pack() geometry manager

btnAdd = tk.Button(frame, text = " Add ", command = do_add)
btnAdd.grid(row=0, column=0, padx=10, pady = 10)

btnSub = tk.Button(frame, text = " Sub ", command = do_sub)
btnSub.grid(row=0, column=1, padx=10, pady = 10)

btnMul = tk.Button(frame, text = " Mul ", command = do_mul)
btnMul.grid(row=0, column=2, padx=10, pady = 10)

btnDiv = tk.Button(frame, text = " Div ", command = do_div)
btnDiv.grid(row=0, column=3, padx=10, pady = 10)

btnPower = tk.Button(frame, text = " Pow ", command = do_pow)
btnPower.grid(row=1, column=0, padx=10, pady = 10)

btnFactorial = tk.Button(frame, text = " n! ", command = do_factorial)
btnFactorial.grid(row=1, column=1, padx=10, pady = 10)

btnExponential = tk.Button(frame, text = " Exp ", command = do_exp)
btnExponential.grid(row=1, column=2, padx=10, pady = 10)

btnLogarithm = tk.Button(frame, text = " Log ", command = do_loga)
btnLogarithm.grid(row=1, column=3, padx=10, pady = 10)

btnSin = tk.Button(frame, text = " Sin ", command = do_sin)
btnSin.grid(row=2, column=0, padx=10, pady = 10)

btnCos = tk.Button(frame, text = " Cos ", command = do_cos)
btnCos.grid(row=2, column=1, padx=10, pady = 10)

btnTan = tk.Button(frame, text = " Tan ", command = do_tan)
btnTan.grid(row=2, column=2, padx=10, pady = 10)

btnRad = tk.Button(frame, text = " Rad ", command = convert_to_r)
btnRad.grid(row=2, column=3, padx=10, pady = 10)

btnArcTan = tk.Button(frame, text = " ArcTan ", command = do_arctan)
btnArcTan.grid(row=3, column=0, padx=10, pady = 10)

btnReset = tk.Button(frame, text = " Reset ", command = reset)
btnReset.grid(row=3, column=1, padx=10, pady = 10)

# Start the event loop
window.mainloop()
