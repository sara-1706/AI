import tkinter as tk
from tkinter import scrolledtext

# Bot response logic
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    if "order" in user_input and "status" in user_input:
        return "To check your order status, please visit 'My Orders' on our website."
    elif "return" in user_input or "refund" in user_input:
        return "You can return books within 7 days. Refunds are processed in 5 business days."
    elif "available" in user_input or "have" in user_input:
        return "Please provide the book name so I can check its availability."
    elif "harry potter" in user_input:
        return "'Harry Potter' series is in stock!"
    elif "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "bye" in user_input or "exit" in user_input:
        return "Thanks for visiting BookNest! Have a great day!"
    else:
        return "Sorry, I didn't get that. Can you rephrase your query?"

# Function to handle send button click
def send_message():
    user_text = entry.get()
    if user_text.strip() == "":
        return
    chatbox.config(state=tk.NORMAL)
    chatbox.insert(tk.END, "You: " + user_text + "\n")
    bot_response = get_bot_response(user_text)
    chatbox.insert(tk.END, "Bot: " + bot_response + "\n\n")
    chatbox.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("BookNest Chatbot")
root.geometry("400x500")

chatbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chatbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(padx=10, pady=(0, 10), fill=tk.X)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=(0, 10))

# Start GUI loop
root.mainloop()
