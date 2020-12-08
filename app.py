from tkinter import filedialog, Text
from tkinter import *
from PIL import *
import os
import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title("Signals and Systems project")
root.iconbitmap('C:/Users/microsoft/OneDrive/Desktop/camera.ico')
# root.geometry("850x500")
root.configure(background="white")

def imgPreview():
    global myimage
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/microsoft/PycharmProjects/SSgui.py/photos",
                                               title="Image open"
                                               , filetypes=(("jpg files", "*.jpg"), ("png files", "*.png") , ("all files", "*.*")))
    # label = Label(root, text=root.filename)
    # label.pack()
    img1=Image.open(root.filename)
    # img1 = img1.resize((200, 1400),Image.ANTIALIAS)
    img1.thumbnail((350,4200))
    myimage = ImageTk.PhotoImage(img1)
    canvas1.create_image(0, 0, anchor=NW, image=myimage)

    # imglabel = Label(root, image=myimage)
    # imglabel.grid(row=0,column=1, columnspan=4)
# my_img = ImageTk.PhotoImage(Image.open("Deadpool.png"))
# my_label = Label(root, image=my_img, width=300, height =300)
# my_label.grid(row=8, column=0)


# def addImage():
#     # that app path which we displayed on frame is repeating so will fix that
#     # here widget is anything in the frame
#     # winfo_children() returns a list of all widgets which are children of this widget.
#     # for widget in frame.winfo_children():
#     #     widget.destroy()
#
#     # below code is to open a filedialogue on clicking the button
#     # in which this function is added (by command = function name)
#     filename = filedialog.askopenfilename( title="Select File",
#                                            filetypes=(("JPEG", "*.jpg"), ("all files", "*.*")) )
#     img1 = ImageTk.PhotoImage(Image.open(filename))
#     canvas1.create_image(root, 50,10, image=img1, anchor=NW)

    #  here apps(here images) path is obtained and shown


# here rightnow I am copying the code from which I am learning but I will make this function to
# open image in the aap get preview of the image in the app
# def runApps():
#     for app in apps:
#         os.startfile(app)




# ROW 0
# canvas1
# 457b9d
#  ////    ROW 0
canvas1 = tk.Canvas(root, height=200, width=700, bg="#457b9d")
canvas1.grid(row=0,column=1, columnspan=4)

# button  openImage
openImageButton = tk.Button(root, text="Open Image", padx=10, pady=5, fg="white", bg="#FF8811", command=imgPreview)
openImageButton.grid(row=0,column=0)

#  //// ROW 1

# button  GradientButton
GradientButton = tk.Button(root, text="Gradient", padx=10, pady=5, fg="white", bg="#FF8811")
GradientButton.grid(row=1, column=0)
# button  EdgeDetectionButton
EdgeDetectionButton = tk.Button(root, text="Edge Detection", padx=10, pady=5, fg="white", bg="#FF8811")
EdgeDetectionButton.grid(row=1, column=1)
# button  GrayscaleButton
GrayscaleButton = tk.Button(root, text="Grayscale", padx=10, pady=5, fg="white", bg="#FF8811")
GrayscaleButton.grid(row=1, column=2)
# button  HorizontalFlipButton
HorizontalFlipButton = tk.Button(root, text="Horizontal Flip", padx=10, pady=5, fg="white", bg="#FF8811")
HorizontalFlipButton.grid(row=1, column=3)
# button  VerticalFlipButton
VerticalFlipButton = tk.Button(root, text="Vertical Flip", padx=10, pady=5, fg="white", bg="#FF8811")
VerticalFlipButton.grid(row=1, column=4)

# //// ROW 2

# slider 1 solarisation
slide_solarisation= Scale(root, from_=0, to=100, orient=HORIZONTAL)
slide_solarisation.grid(row=2, column=0)

# slider 1 brightness
slide_brightness= Scale(root, from_=0, to=100, orient=HORIZONTAL)
slide_brightness.grid(row=2, column=1)

# slider 1 contrast
slide_contrast= Scale(root, from_=0, to=100, orient=HORIZONTAL)
slide_contrast.grid(row=2, column=2)

# slider 1 blur
slide_blur= Scale(root, from_=0, to=100, orient=HORIZONTAL)
slide_blur.grid(row=2, column=3)

# //// ROW 3
label_solarisation = Label(root, text="Solarisation")
label_solarisation.grid(row= 3, column=0 )

label_brightness = Label(root, text="Brightness")
label_brightness.grid(row= 3, column=1)

label_contrast = Label(root, text="Contrast")
label_contrast.grid(row= 3, column=2)

label_blur = Label(root, text="Blur")
label_blur.grid(row= 3, column=3)

# //// ROW 4
label1 = Label(root, text= slide_solarisation.get())
def slide1():
    label1 = Label(root, text= slide_solarisation.get())
    label1.grid(row=4, column=0)
def slide2():
    label = Label(root, text= slide_brightness.get())
    label.grid(row=4, column=1)
def slide3():
    label = Label(root, text= slide_contrast.get())
    label.grid(row=4, column=2)
def slide4():
    label = Label(root, text= slide_blur.get())
    label.grid(row=4, column=3)
# //// ROW 5
label = Label(root, text= slide_solarisation.get())
slide_button = Button(root, text="Click to fix value",command=slide1, padx=10, pady=5, fg="white", bg="#0096c7")
slide_button.grid(row=5, column=0)

label = Label(root, text= slide_brightness.get())
slide_button = Button(root, text="Click to fix value",command=slide2, padx=10, pady=5, fg="white", bg="#0096c7")
slide_button.grid(row=5, column=1)

label = Label(root, text= slide_contrast.get())
slide_button = Button(root, text="Click to fix value",command=slide3, padx=10, pady=5, fg="white", bg="#0096c7")
slide_button.grid(row=5, column=2)

label = Label(root, text= slide_blur.get())
slide_button = Button(root, text="Click to fix value",command=slide4, padx=10, pady=5, fg="white", bg="#0096c7")
slide_button.grid(row=5, column=3)

# //// ROW 6

# canvas2
canvas2 = tk.Canvas(root, height=200, width=700, bg="#457b9d")
canvas2.grid(row=6, column=1, columnspan=4)

# button 8 Export
Export = tk.Button(root, text="Export", padx=10, pady=5, fg="white", bg="#FF8811")
Export.grid(row=6, column=0)

# //// ROW 7
# button 9 Exit
Exit = tk.Button(root, text="EXIT!",padx=10, pady=5, fg="white", bg="#FF8811", command=root.quit)
Exit.grid(row=7, column=0, columnspan=5)

# frame if you want
# (relwidth, relheight, relx, rely if they are 1 then full canvas will  be occupied)
# frame = tk.Frame(root, bg="white")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
















root.mainloop()
