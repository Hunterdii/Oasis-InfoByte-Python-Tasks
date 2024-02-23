import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
from ttkthemes import ThemedStyle
import emoji

HOST = '127.0.0.1'
PORT = 1489

BASE_COLOR = '#2F3136'
WHITE = "#E5E5EA"
PRIMARY_COLOR = '#4CAF50'
SECONDARY_COLOR = '#ECEFF1'
THIRD_COLOR = '#C51162'
FONT = ("Helvetica", 12)
BUTTON_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 10)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def add(message, tag=None):
    message_box.config(state=tk.NORMAL)
    message_box.insert(tk.END, message + "\n", tag)
    message_box.config(state=tk.DISABLED)
    message_box.see(tk.END)  

def connect():
    try:
        client.connect((HOST, PORT))
        print('successfully connected to server')
        add("[CHATBOT] Successfully connected to the server")

        username = username_textbox.get()
        if username != '':
            client.sendall(username.encode())
        else:
            messagebox.showerror("Error", "Username should not be empty")
            return

        threading.Thread(target=listen_for_messages_from_server, args=(client,)).start()
        username_textbox.config(state=tk.DISABLED)
        username_button.config(state=tk.DISABLED)

    except Exception as e:
        messagebox.showerror("Error", f"Unable to connect to server {HOST} {PORT}: {e}")

def send_message():
    message = message_textbox.get()
    if message != '':
        client.sendall(emoji.demojize(message).encode())
        add(f"You ~ {message}", 'user_message')
        message_textbox.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Message should not be empty")

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        message = f"Uploaded file: {file_path}"
        add(f"You ~ {message}", 'user_message')

root = tk.Tk()
root.geometry("800x600")
root.title('Browser-Based Chat Application')
root.resizable(False, False)

style = ThemedStyle(root)
style.set_theme("arc")

root.configure(bg=BASE_COLOR)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

username_frame = tk.Frame(root, bg=BASE_COLOR)
username_frame.grid(row=0, column=0, sticky="ew")

username_label = tk.Label(username_frame, text="Enter Username: ", font=FONT, bg=BASE_COLOR, fg=PRIMARY_COLOR)
username_label.pack(side=tk.LEFT, padx=10, pady=10)

username_textbox = tk.Entry(username_frame, font=FONT, bg=WHITE, fg="#223377", width=23)
username_textbox.pack(side=tk.LEFT, padx=10, pady=10)

username_button = tk.Button(username_frame, font=BUTTON_FONT, bg=PRIMARY_COLOR, fg=WHITE, command=connect, text="Join",
                            borderwidth=2, highlightbackground='#223377', highlightcolor='#223377', highlightthickness=2)
username_button.pack(side=tk.LEFT, padx=10, pady=10)

middle_frame = tk.Frame(root, bg=SECONDARY_COLOR)
middle_frame.grid(row=1, column=0, sticky="nsew")

message_box = scrolledtext.ScrolledText(middle_frame, font=SMALL_FONT, bg=WHITE, fg="#555555", width=67, height=26.5)
message_box.config(state=tk.DISABLED)
message_box.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

message_box.tag_config('user_message', foreground='blue', font=('Helvetica', 10, 'bold'))

bottom_frame = tk.Frame(root, bg=SECONDARY_COLOR)
bottom_frame.grid(row=2, column=0, sticky="ew")

message_label = tk.Label(bottom_frame, text="Message: ", font=FONT, bg=BASE_COLOR, fg=PRIMARY_COLOR)
message_label.pack(side=tk.LEFT, padx=10, pady=10)

message_textbox = tk.Entry(bottom_frame, font=FONT, bg=WHITE, fg="#556b2f", width=38)
message_textbox.pack(side=tk.LEFT, padx=10, pady=10)

message_button = tk.Button(bottom_frame, font=BUTTON_FONT, bg=PRIMARY_COLOR, fg=WHITE, command=send_message, text="Send",
                            borderwidth=2, highlightbackground='#223377', highlightcolor='#223377', highlightthickness=2)
message_button.pack(side=tk.LEFT, padx=10, pady=10)

file_button = tk.Button(bottom_frame, font=BUTTON_FONT, bg=PRIMARY_COLOR, fg=WHITE, command=upload_file, text="Upload",
                        borderwidth=2, highlightbackground='#223377', highlightcolor='#223377', highlightthickness=2)
file_button.pack(side=tk.LEFT, padx=10, pady=10)

def listen_for_messages_from_server(client):
    while True:
        message = client.recv(2048).decode('utf-8')
        if message:
            username, content = message.split('~')
            add(f"[{username}] ~ {content}", 'user_message')
        else:
            messagebox.showerror("Error", "Message from user should not be empty")

def main():
    root.mainloop()

if __name__ == '__main__':
    main()
