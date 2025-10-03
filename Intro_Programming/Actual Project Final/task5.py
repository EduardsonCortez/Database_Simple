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
root.geometry("600x400")

# Load background image (replace 'myphoto.jpg' with your picture)
bg_image = Image.open("Eduard.png")
bg_image = bg_image.resize((600, 400))  # resize para sakto sa window
bg_photo = ImageTk.PhotoImage(bg_image)

# Background label
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Input fields
frame = tk.Frame(root, bg="white", bd=5)
frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(frame, text="Enter Name:", bg="white").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Enter Age:", bg="white").grid(row=1, column=0, sticky="w")
age_entry = tk.Entry(frame, width=30)
age_entry.grid(row=1, column=1)

tk.Label(frame, text="Favorite Hobby:", bg="white").grid(row=2, column=0, sticky="w")
hobby_entry = tk.Entry(frame, width=30)
hobby_entry.grid(row=2, column=1)

submit_btn = tk.Button(frame, text="Save", command=save_info, bg="green", fg="white")
submit_btn.grid(row=3, columnspan=2, pady=10)

root.mainloop()
