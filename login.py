import customtkinter # pkg importation
from tkinter import * # pkg call
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# window-box setup
window = customtkinter.CTk()
window.geometry("700x400")
window.title("Login")
window.iconbitmap("favicon.ico")
window.resizable(False, False)

# img box-selector
img = PhotoImage(file="log.png")
Label_img = customtkinter.CTkLabel(master=window, image=img)
Label_img.place(x=5, y=5)

# frame-box in window-box setup
frame = customtkinter.CTkFrame(master=window, width=350, height=395)
frame.pack(side=RIGHT)

# frame widgets
label = customtkinter.CTkLabel(master=frame, text="Sistema de Login")
label.place(x=25, y=5)

input1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")

window.mainloop()                                                