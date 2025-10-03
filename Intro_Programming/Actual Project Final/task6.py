import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime

# Function to save and show info
def save_info():
    name = name_entry.get()
    age = age_entry.get()
    hobby = hobby_entry.get()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    info = f"👤 Name: {name}\n🎂 Age: {age}\n🎯 Hobby: {hobby}\n🕒 Time: {timestamp}"
    messagebox.showinfo("User Information", info)

# Main window
root = tk.Tk()
root.title("Database by Eduard Cortez")
root.geometry("700x400")

# Load and resize background image (replace with your picture filename)
bg_image = Image.open("Eduard.png")
bg_image = bg_image.resize((300, 400))  # fixed width para left side lang
bg_photo = ImageTk.PhotoImage(bg_image)

# Picture on the left
bg_label = tk.Label(root, image=bg_photo)
bg_label.pack(side="left", fill="y")

# Input fields on the right
frame = tk.Frame(root, bg="white", bd=5)
frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

tk.Label(frame, text="Enter Name:", bg="white").grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Enter Age:", bg="white").grid(row=1, column=0, sticky="w", pady=5)
age_entry = tk.Entry(frame, width=30)
age_entry.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Favorite Hobby:", bg="white").grid(row=2, column=0, sticky="w", pady=5)
hobby_entry = tk.Entry(frame, width=30)
hobby_entry.grid(row=2, column=1, pady=5)

submit_btn = tk.Button(frame, text="Save", command=save_info, bg="green", fg="white")
submit_btn.grid(row=3, columnspan=2, pady=15)

root.mainloop()
