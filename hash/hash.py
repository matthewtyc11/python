import hashlib
import secrets
import tkinter as tk
from tkinter import messagebox, simpledialog

# Initialize the main dictionary to store user data
data = {}

# Function to save data to a file
def save_data_to_file():
    with open("user_data.txt", "w") as file:
        for username, info in data.items():
            file.write(f"{username}: {info}\n")

# Function to create a new account
def create_account():
    username = simpledialog.askstring("Account Name", "Enter account name:")
    if username in data:
        messagebox.showerror("Error", "Account already exists!")
        return
    
    password = simpledialog.askstring("Password", "Enter password:", show='*')
    random_token = secrets.token_hex(32)
    data[username] = {
        "Name": username,
        "Password": hashlib.sha1((password + random_token).encode('utf-8')).hexdigest(),
        "Random": random_token
    }
    save_data_to_file()  # Save the updated data to the file
    messagebox.showinfo("Success", "Account created successfully!")

# Function to log in to an existing account
def login():
    username = simpledialog.askstring("Account Name", "Enter account name:")
    if username not in data:
        messagebox.showerror("Error", "This user does not exist!")
        return
    
    password = simpledialog.askstring("Password", "Enter password:", show='*')
    user_data = data[username]
    hashed_password = hashlib.sha1((password + user_data["Random"]).encode('utf-8')).hexdigest()
    
    if hashed_password == user_data["Password"]:
        messagebox.showinfo("Success", "Logged in successfully!")
    else:
        messagebox.showerror("Error", "Wrong password!")

# Function to display all user data
def display_data():
    if not data:
        messagebox.showinfo("No Data", "No accounts exist.")
    else:
        all_data = "\n".join(f"{user}: {info}" for user, info in data.items())
        messagebox.showinfo("All Data", all_data)

# Setting up the main window
root = tk.Tk()
root.title("Account Manager")

# Creating buttons for each action
create_button = tk.Button(root, text="Create Account", command=create_account)
create_button.pack(pady=10)

login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=10)

display_button = tk.Button(root, text="Display All Data", command=display_data)
display_button.pack(pady=10)

# Run the application
root.mainloop()