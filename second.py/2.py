from tkinter import * 
from tkinter import messagebox 
from PIL import Image, ImageTk   # =>pip install window 

root = Tk()
root.title("Tkinter baisics")
root.geometry("400x400")

def show_image():
    img_window = Toplevel(root)# sceondary window 1(img_window)
    img_window.title("Image Window")

    img = Image.open("Demo.jpeg")# here you need to write the name of your image 
    img = img.resize((200, 200))
    img_Tk = ImageTk.PhotoImage(img)# loading it to Tkiner

    #
    image_label = Label(img_window, image=img_Tk)
    img_label.image = img_Tk
    image_label.pack()

    def show_message():
        messagebox.showinfo("Your msg", "hello friend!")

    def open_top_window():
        top = Toplevel(root) # secondaray window 2 (top)
        top.title("Top window")
        top.geometry("250x150")
        Label(top, text="New top window!", font=("Arial", 12)).pack(pady=20)

    btn1 = Button(root, text="Show Image", command=show_image)
    btn1.pack(pady=10)

    btn2 = Button(root, text="Show Image", command = show_message)
    btn2.pack(pady=10)

    btn3 = Button(root, text="Show Image", command=open_top_window)
    btn3.pack(pady=10)

root.mainloop()