from tkinter import *
from PIL import Image, ImageTk
import os
import qrcode
from tkinter import filedialog

root = Tk()
root.geometry('1250x650')
root.title('Qr Generator')
root.configure(bg='#333')

placeholder_text = StringVar()
placeholder_text.set("Your data here")

e = Entry(root, highlightthickness=5, font=('Arial', 14, 'bold'), textvariable=placeholder_text, width=50)
e.pack(padx=30, pady=30)

file_path = ''

def generate_qr_code(data):
    global file_path
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=10,
    )

    qr.add_data(data)
    qr.make(fit=True)

    default_path = os.path.expanduser("~/Downloads/")
    file_path = filedialog.asksaveasfilename(initialdir=default_path, defaultextension=".png")

    qr_image = qr.make_image(fill_color="#49FF00", back_color="#191825")
    qr_image.save(file_path)

    display_image()

def display_image():
    if file_path:
        image = Image.open(file_path)
        imagetk = ImageTk.PhotoImage(image.resize((350, 350)))
        label.config(image=imagetk)
        label.image = imagetk

label = Label(root, text='                                                        ', bg='#333')
label.pack()

button = Button(root, padx=30, pady=10, text='Generate QR', font=('Sans serif', 14, 'bold'), fg='Blue', bg='green', command=lambda: generate_qr_code(e.get()))
button.pack(pady=50)

root.mainloop()
