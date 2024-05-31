import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.configure(bg="#2e2e2e")

# Global variable to store the expression
expression = ""

# Function to update the expression in the text entry box
def update_expression(number):
    global expression
    expression += str(number)
    equation.set(expression)

# Function to evaluate the final expression
def evaluate_expression():
    global expression
    try:
        result = str(eval(expression))  # Evaluate the expression
        equation.set(result)
        expression = result
    except:
        equation.set("error")
        expression = ""

# Function to clear the text entry box
def clear_expression():
    global expression
    expression = ""
    equation.set("")

# Create a StringVar to hold the expression
equation = tk.StringVar()

# Create the text entry box for showing the expression
expression_field = tk.Entry(root, textvariable=equation, font=('Arial', 20, 'bold'), bg="#ffffff", fg="#000000", bd=10, insertwidth=2, width=14, borderwidth=4)
expression_field.grid(columnspan=4, ipadx=8, ipady=20)

# Create buttons
buttons = [
    '7', '8', '9', '/', '4', '5', '6', '*',
    '1', '2', '3', '-', '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, fg="#ffffff", bg="#4caf50", font=('Arial', 20, 'bold'),
                        command=evaluate_expression, height=2, width=7)
    else:
        btn = tk.Button(root, text=button, fg="#ffffff", bg="#333333", font=('Arial', 20, 'bold'),
                        command=lambda button=button: update_expression(button), height=2, width=7)
    
    btn.grid(row=row_val, column=col_val, pady=10, padx=10)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create Clear button
clear_button = tk.Button(root, text='C', fg="#ffffff", bg="#f44336", font=('Arial', 20, 'bold'),
                         command=clear_expression, height=2, width=7)
clear_button.grid(row=row_val, column=col_val, pady=10, padx=10)

# Run the main application loop
root.mainloop()
