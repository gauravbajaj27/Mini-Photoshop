from tkinter import filedialog, Text
from tkinter import *
from PIL import *
import os
import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.title("Signals and Systems project")
# root.iconbitmap('C:/Users/microsoft/OneDrive/Desktop/camera.ico')
# root.geometry("900x500")
root.configure(background="#ef476f")

def imgPreview():
    global myimage
    root.filename = filedialog.askopenfilename(initialdir="C:/",
                                               title="Open Image"
                                               , filetypes=(("jpg files", "*.jpg"), ("png files", "*.png") , ("all files", "*.*")))
    # label = Label(root, text=root.filename)
    # label.pack()
    img1=Image.open(root.filename)
    # img1 = img1.resize((200, 1400),Image.ANTIALIAS)
    img1.thumbnail((500,1080))
    myimage = ImageTk.PhotoImage(img1)
    canvas0.create_image(100, 0, anchor=NW, image=myimage)
    # 350, 4200
    # imglabel = Label(root, image=myimage)
    # imglabel.grid(row=0,column=1, columnspan=4)
# my_img = ImageTk.PhotoImage(Image.open("Deadpool.png"))
# my_label = Label(root, image=my_img, width=300, height =300)
# my_label.grid(row=8, column=0)

# def gradButt():
#     class Example(tk.Frame):
#         def __init__(self, parent):
#             tk.Frame.__init__(self, parent)
#             f1 = GradientFrame(self, borderwidth=1, relief="sunken")
#             f2 = GradientFrame(self, "green", "blue", borderwidth=1, relief="sunken")
#             f1.pack(side="top", fill="both", expand=True)
#             f2.pack(side="bottom", fill="both", expand=True)
#
#     class GradientFrame(tk.Canvas):
#         '''A gradient frame which uses a canvas to draw the background'''
#
#         def __init__(self, parent, color1="red", color2="black", **kwargs):
#             tk.Canvas.__init__(self, parent, **kwargs)
#             self._color1 = color1
#             self._color2 = color2
#             self.bind("<Configure>", self._draw_gradient)
#
#         def _draw_gradient(self, event=None):
#             '''Draw the gradient'''
#             self.delete("gradient")
#             width = self.winfo_width()
#             height = self.winfo_height()
#             limit = width
#             (r1, g1, b1) = self.winfo_rgb(self._color1)
#             (r2, g2, b2) = self.winfo_rgb(self._color2)
#             r_ratio = float(r2 - r1) / limit
#             g_ratio = float(g2 - g1) / limit
#             b_ratio = float(b2 - b1) / limit
#
#             for i in range(limit):
#                 nr = int(r1 + (r_ratio * i))
#                 ng = int(g1 + (g_ratio * i))
#                 nb = int(b1 + (b_ratio * i))
#                 color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
#                 self.create_line(i, 0, i, height, tags=("gradient",), fill=color)
#             self.lower("gradient")
#
#     if __name__ == "__main__":
#         root = tk.Tk()
#         Example(root).pack(fill="both", expand=True)


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

# canvas3 = tk.Canvas(root, height=750, width=170, bg="#ef476f")
# canvas3.grid(row=0,column=0, columnspan=1, rowspan=15, padx=0, pady=0, ipadx=0, ipady=0)


# ROW 0
# canvas1
# 457b9d

#  ////    ROW 0
canvas0 = tk.Canvas(root, height=200, width=700, bg="#457b9d")
canvas0.grid(row=0,column=1, columnspan=2, rowspan=5, padx=0, pady=0, ipadx=0, ipady=43)

# button  openImage
openImageButton = tk.Button(root, text="Open Image", padx=10, pady=0, fg="white", bg="#FF8811", command=imgPreview)
openImageButton.grid(row=0,column=0, rowspan=1, columnspan=1, sticky=NW, padx=35, pady=2, ipadx=0, ipady=0)
# button  GradientButton
GradientButton = tk.Button(root, text="Gradient", padx=10, pady=0, fg="white", bg="#FF8811", command=gradButt)
GradientButton.grid(row=1, column=0, sticky=NW, padx=35, pady=0, ipadx=0, ipady=0)
# button  EdgeDetectionButton
EdgeDetectionButton = tk.Button(root, text="Edge Detection", padx=10, pady=0, fg="white", bg="#FF8811")
EdgeDetectionButton.grid(row=2, column=0, sticky=NW, padx=35, pady=0, ipadx=0, ipady=0)
# button  GrayscaleButton
GrayscaleButton = tk.Button(root, text="Grayscale", padx=10, pady=0, fg="white", bg="#FF8811")
GrayscaleButton.grid(row=3, column=0, sticky=NW, padx=35, pady=0, ipadx=0, ipady=0)
# button  HorizontalFlipButton
HorizontalFlipButton = tk.Button(root, text="Horizontal Flip", padx=10, pady=0, fg="white", bg="#FF8811")
HorizontalFlipButton.grid(row=4, column=0, sticky=NW, padx=35, pady=0, ipadx=0, ipady=0)

#  ////  ROW 1

canvas1 =tk.Canvas(root,height=200, width=700, bg="#264653")
canvas1.grid(row=6,column=1, columnspan=2, rowspan=9, padx=0, pady=0, ipadx=0, ipady=70)
# button  VerticalFlipButton
VerticalFlipButton = tk.Button(root, text="Vertical Flip", padx=10, pady=0, fg="white", bg="#FF8811")
VerticalFlipButton.grid(row=5, column=0, sticky=NW, padx=35, pady=5, ipadx=0, ipady=0)
# slider  solarisation
slide_solarisation= Scale(root, from_=0, to=100, orient=HORIZONTAL)
slide_solarisation.grid(row=6, column=0, sticky=NW, padx=35, pady=0, ipadx=0, ipady=0)

# slider  brightness
slide_brightness= Scale(root, from_=0, to=100, orient=HORIZONTAL)
slide_brightness.grid(row=8, column=0, sticky=NW, padx=35, pady=0, ipadx=0, ipady=0)

# slider  contrast
slide_contrast= Scale(root, from_=0, to=100, orient=HORIZONTAL)
slide_contrast.grid(row=10, column=0, sticky=NW, padx=35, pady=0, ipadx=0, ipady=0)

# slider  blur
slide_blur= Scale(root, from_=0, to=100, orient=HORIZONTAL)
slide_blur.grid(row=12, column=0, sticky=NW, padx=35, pady=0, ipadx=0, ipady=0)

# # //// ROW 3
# canvas3 =tk.Canvas(root,height=50, width=820, bg="#264653")
# canvas3.grid(row=3, column=0,  columnspan=5, rowspan=1)
#
# label_solarisation = Label(root, text="Solarisation")
# label_solarisation.grid(row= 3, column=0 )
#
# label_brightness = Label(root, text="Brightness")
# label_brightness.grid(row= 3, column=1)
#
# label_contrast = Label(root, text="Contrast")
# label_contrast.grid(row= 3, column=2)
#
# label_blur = Label(root, text="Blur")
# label_blur.grid(row= 3, column=3)


label1 = Label(root, text= slide_solarisation.get())
def slide1():
    label1 = Label(root, text= slide_solarisation.get())
    # label1.grid(row=4, column=0)
def slide2():
    label = Label(root, text= slide_brightness.get())
    # label.grid(row=4, column=1)
def slide3():
    label = Label(root, text= slide_contrast.get())
    # label.grid(row=4, column=2)
def slide4():
    label = Label(root, text= slide_blur.get())
    # label.grid(row=4, column=3)



label = Label(root, text= slide_solarisation.get())
slide_button = Button(root, text="Solarisation",command=slide1, padx=10, pady=5, fg="white", bg="#0096c7")
slide_button.grid(row=7, column=0, sticky="", padx=0, pady=0, ipadx=0, ipady=0)

label = Label(root, text= slide_brightness.get())
slide_button = Button(root, text="Brightness",command=slide2, padx=10, pady=5, fg="white", bg="#0096c7")
slide_button.grid(row=9, column=0, sticky="", padx=0, pady=0, ipadx=0, ipady=0)

label = Label(root, text= slide_contrast.get())
slide_button = Button(root, text="Contrast",command=slide3, padx=10, pady=5, fg="white", bg="#0096c7")
slide_button.grid(row=11, column=0, sticky="", padx=0, pady=0, ipadx=0, ipady=0)

label = Label(root, text= slide_blur.get())
slide_button = Button(root, text="Blur",command=slide4, padx=10, pady=5, fg="white", bg="#0096c7")
slide_button.grid(row=13, column=0, sticky="", padx=0, pady=0, ipadx=0, ipady=0)



# canvas6 = tk.Canvas(root, height=200, width=700, bg="#457b9d")
# canvas6.grid(row=6, column=1, columnspan=4)

# button 8 Export
Export = tk.Button(root, text="Export", padx=0, pady=0, fg="white", bg="#FF8811")
Export.grid(row=14, column=0, sticky="", padx=0, pady=4, ipadx=0, ipady=0)

# //// ROW 7
# button 9 Exit
Exit = tk.Button(root, text="EXIT!",padx=0, pady=0, fg="white", bg="#FF8811", command=root.quit)
Exit.grid(row=15, column=0, sticky="", padx=0, pady=0, ipadx=0, ipady=0)

# frame if you want
# (relwidth, relheight, relx, rely if they are 1 then full canvas will  be occupied)
# frame = tk.Frame(root, bg="white")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
















root.mainloop()
