import tkinter as tk
from tkinter import messagebox
import math

# Function definitions
history = []

def click(event):
    global input_text
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            expression = input_text.get().strip()  # Get and trim the input
            if not expression:
                raise ValueError("Empty Input")
            result = eval(expression)
            history.append(f"{expression} = {result}")
            input_text.set(result)
        except Exception as e:
            input_text.set("Error")
            messagebox.showerror("Error", "Invalid Input. Please try again.")
    elif text == "C":
        input_text.set("")
    elif text == "CA":
        input_text.set("")
        history.clear()
    elif text == "CH":
        if history:
            messagebox.showinfo("History", "\n".join(history))
        else:
            messagebox.showinfo("History", "No calculations yet.")
    elif text == "%":
        try:
            value = float(input_text.get()) / 100
            input_text.set(value)
        except Exception as e:
            input_text.set("Error")
            messagebox.showerror("Error", "Invalid Input. Please try again.")
    elif text == "√":
        try:
            value = math.sqrt(float(input_text.get()))
            input_text.set(value)
        except Exception as e:
            input_text.set("Error")
            messagebox.showerror("Error", "Invalid Input. Please try again.")
    else:
        input_text.set(input_text.get() + text)

# Main GUI setup
root = tk.Tk()
root.title("Enhanced Calculator")
root.geometry("400x600")
root.resizable(False, False)

# Input field
input_text = tk.StringVar()
input_field = tk.Entry(root, textvar=input_text, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
input_field.pack(fill=tk.BOTH, ipadx=8, ipady=15)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.BOTH, expand=True)

# Button layout
button_texts = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+'],
    ['CA', 'CH', '%', '√']  # New row for additional buttons
]

for row in button_texts:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(fill=tk.BOTH, expand=True)
    for char in row:
        btn = tk.Button(row_frame, text=char, font=("Arial", 18), bd=5, relief=tk.RIDGE)
        btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        btn.bind("<Button-1>", click)

# Run the application
root.mainloop()

