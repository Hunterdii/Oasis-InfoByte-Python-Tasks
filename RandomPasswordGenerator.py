import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import string
import random
import pyperclip

def generate_password():
    length = length_var.get()
    if length <= 0:
        messagebox.showerror("Error", "Please enter a valid password length.")
        return

    character_set = ''
    if uppercase_var.get():
        character_set += string.ascii_uppercase
    if lowercase_var.get():
        character_set += string.ascii_lowercase
    if digits_var.get():
        character_set += string.digits
    if symbols_var.get():
        character_set += string.punctuation

    if not character_set:
        messagebox.showerror("Error", "Please select at least one character set.")
        return

    password = ''.join(random.choice(character_set) for _ in range(length))
    password_entry.delete(0, 'end')
    password_entry.insert('end', password)

def copy_password():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Password Copied", "Password copied to clipboard successfully!")
    else:
        messagebox.showwarning("No Password", "No password to copy!")

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(expand=True, padx=20, pady=20)

length_label = tk.Label(frame, text="Password Length:", bg="#f0f0f0", font=("Helvetica", 12))
length_label.grid(row=0, column=0, sticky="w", pady=5)

length_var = tk.IntVar()
length_entry = tk.Entry(frame, textvariable=length_var, font=("Helvetica", 12))
length_entry.grid(row=0, column=1, sticky="w", pady=5)

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(frame, text="Uppercase", variable=uppercase_var, bg="#f0f0f0", font=("Helvetica", 10))
uppercase_checkbox.grid(row=1, column=0, sticky="w", pady=2)

lowercase_var = tk.BooleanVar()
lowercase_checkbox = tk.Checkbutton(frame, text="Lowercase", variable=lowercase_var, bg="#f0f0f0", font=("Helvetica", 10))
lowercase_checkbox.grid(row=2, column=0, sticky="w", pady=2)

digits_var = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(frame, text="Digits", variable=digits_var, bg="#f0f0f0", font=("Helvetica", 10))
digits_checkbox.grid(row=3, column=0, sticky="w", pady=2)

symbols_var = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(frame, text="Symbols", variable=symbols_var, bg="#f0f0f0", font=("Helvetica", 10))
symbols_checkbox.grid(row=4, column=0, sticky="w", pady=2)

generate_button = tk.Button(frame, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
generate_button.grid(row=5, column=0, columnspan=2, pady=10)

password_entry = tk.Entry(frame, show="*", font=("Helvetica", 14), justify="center")
password_entry.grid(row=6, column=0, columnspan=2, pady=10)

copy_button = tk.Button(frame, text="Copy Password", command=copy_password, bg="#008CBA", fg="white", font=("Helvetica", 12, "bold"))
copy_button.grid(row=7, column=0, columnspan=2)

def on_enter(event):
    event.widget.config(bg="#5EBABA")

def on_leave(event):
    event.widget.config(bg="#008CBA" if event.widget == copy_button else "#4CAF50")

copy_button.bind("<Enter>", on_enter)
copy_button.bind("<Leave>", on_leave)

generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)

def pulsate_animation(widget):
    def animate():
        widget.config(bg="#5EBABA")
        widget.after(500, lambda: widget.config(bg="#4CAF50"))
        widget.after(1000, animate)
    animate()

pulsate_animation(generate_button)

root.mainloop()
