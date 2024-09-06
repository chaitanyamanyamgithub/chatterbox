import tkinter as tk

# Function to handle sending messages
def send_message():
    message = entry_box.get()
    if message.strip() != "":
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "You: " + message + "\n")
        chat_box.config(state=tk.DISABLED)
        chat_box.yview(tk.END)
        entry_box.delete(0, tk.END)

# Creating the main window
window = tk.Tk()
window.title("Chat Box")

# Chat box to display messages
chat_box = tk.Text(window, width=50, height=20, state=tk.DISABLED, bg="light yellow")
chat_box.pack(padx=10, pady=10)

# Entry box to type messages
entry_box = tk.Entry(window, width=40)
entry_box.pack(padx=10, pady=10)

# Send button to send messages
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=5)

# Bind the Enter key to send message
window.bind('<Return>', lambda event: send_message())

# Run the GUI loop
window.mainloop()
