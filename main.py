from tkinter import *
from tkinter import filedialog
import math
from PIL import Image, ImageTk, ImageOps, ImageFilter, ImageEnhance
from tkinter import messagebox
# from wand.image import Image
from PIL.ImageFilter import (
   BLUR, CONTOUR
)
#import os

root = Tk()

#Setting background
bg = PhotoImage(file="F:/Pics/star2.png")
my_label = Label(root, image=bg)
my_label.place(x=0 , y=0, relwidth=1, relheight=1)
my_text = Label(root, text="Image-e-nation", font=("Verdana", 30, "bold"), fg="white", bg="#020202")
my_text.grid(row=1, column=1, pady=50, padx=100)

def open_img_file():
    global filename, top, panel, panel2, image, output_image
    filename = filedialog.askopenfilename(initialdir="F:/Pics", title="Select file", filetypes=(("jpg files", ".jpg"), ("all files", "*.*")))


    # setup new window
    top = Toplevel(root)
    top.title("Effect window")
    top.minsize(350, 300)
    # get image
    image = ImageTk.PhotoImage(Image.open(filename))

    # load image
    panel = Label(top,  image=image,  borderwidth=3, relief="solid")
    panel.image = image
    panel.grid(row=1, column=2, padx=10)

    button_exit2 = Button(top, text="Exit", padx=20, pady=10,
                          command=top.destroy).grid(row=6, column=3, sticky= "e")


    topframe = Frame(top)
    topframe.grid(row=1, column=1)
    bandw_button = Button(topframe, text="Black&White", width=7, height=2, padx=20, pady=5,
                          command=bandw).grid(row=1, column=1, pady=7)
    negative_button = Button(topframe, text="Invert", width=7, height=2, padx=20, pady=5,
                          command=negative).grid(row=2, column=1, pady=7)
    photocopy_button = Button(topframe, text="Photocopy", width=7, height=2, padx=20, pady=5,
                          command=showsliderphotocopy).grid(row=3, column=1, pady=7)
    painting_button = Button(topframe, text="Painting", width=7, height=2, padx=20, pady=5,
                          command=painting).grid(row=4, column=1, pady=7)
    sketch_button = Button(topframe, text="Sketch", width=7, height=2, padx=20, pady=5,
                          command=sketch).grid(row=5, column=1, pady=7)
    sepia_button = Button(topframe, text="Sepia", width=7, height=2, padx=20, pady=5,
                          command=showslidersepia).grid(row=6, column=1, pady=7)
    posterize_button = Button(topframe, text="Posterize", width=7, height=2, padx=20, pady=5,
                          command=posterize).grid(row=7, column=1, pady=7)
    save_button = Button(topframe, text="Save", width=7, height=2, padx=20, pady=5,
                          command=savefile).grid(row=10, column=1, pady=7)
    nightvision_button = Button(topframe, text="Nightvision", width=7, height=2, padx=20, pady=5,
                         command=nightvision).grid(row=8, column=1, pady=7)
    vignette_button = Button(topframe, text="Vignette", width=7, height=2, padx=20, pady=5,
                         command=showslidervignette).grid(row=9, column=1, pady=7)
    # test_button = Button(topframe, text="Test", width=7, height=2, padx=20, pady=5,
    #                      command=savefile).grid(row=10, column=1, pady=7)



root.title("Image-e-nation")
root.minsize(375, 340)

button = Button(text="Select Image", width=8, height=2, padx=10, pady=2,
                command=open_img_file)
button.grid(row=2, column=1)



def popup():
    response = messagebox.showinfo("What do I do?", "I am an image editing sofware.I can add different kinds of uniue effects to your images and give them an interesting new look.")


def bandw():
    global output_image
    image_file = Image.open(filename) # open colour image
    output_image = image_file.convert('L')
    display_image = ImageTk.PhotoImage(output_image)
    panel2 = Label(top, image=display_image, borderwidth=3, relief="solid")
    panel2.image = display_image
    panel2.grid(row=1, column=3, padx=8)


def painting():
    global output_image
    img1 = Image.open(filename)
    img2 = Image.open("F:/Pics/van.jpg")
    img2 = img2.resize(img1.size)
    output_image  = Image.blend(img1, img2 , 0.4)
    display_image = ImageTk.PhotoImage(output_image)
    panel2 = Label(top, image=display_image, borderwidth=3, relief="solid")
    panel2.image = display_image
    panel2.grid(row=1, column=3, padx=8)



def sketch():
    global output_image
    sket = Image.open(filename)
    sket = sket.convert('L')
    #sket = sket.filter(EDGE_ENHANCE)
    output_image = sket.filter(CONTOUR)

    display_image = ImageTk.PhotoImage(output_image)
    panel2 = Label(top, image=display_image, borderwidth=3, relief="solid")
    panel2.image = display_image
    panel2.grid(row=1, column=3, padx=8)


def negative():
    global output_image
    image_to_transform = Image.open(filename)
    output_image = image_to_transform.convert("RGB")

    for x in range(output_image.width):
        for y in range(output_image.height):

            input_pixel = output_image.getpixel((x, y))


            output_R = 255 - input_pixel[0]
            output_G = 255 - input_pixel[1]
            output_B = 255 - input_pixel[2]

            output_image.putpixel((x, y), (int(output_R), int(output_G), int(output_B)))

    display_image = ImageTk.PhotoImage(output_image)
    panel2 = Label(top, image=display_image, borderwidth=3, relief="solid")
    panel2.image = display_image
    panel2.grid(row=1, column=3, padx=8)

'''
def test():
    global output_image
    image_to_transform = Image.open(filename)
    output_image = image_to_transform.convert("RGB")

    for x in range(output_image.width):
        for y in range(output_image.height):

            input_pixel = output_image.getpixel((x, y))

            # output_R = input_pixel[1]/2
            # output_B = output_R*2
            # output_G = output_B*2
            output_R = 255 - input_pixel[0]

            output_G = 255 - input_pixel[1]

            output_B = 255 - input_pixel[2]
            output_image.putpixel((x, y), (int(output_R), int(output_G), int(output_B)))

    display_image = ImageTk.PhotoImage(output_image)
    panel2 = Label(top, image=display_image, borderwidth=3, relief="solid")
    panel2.image = display_image
    panel2.grid(row=1, column=3, padx=8)
'''

def showsliderphotocopy():
    global horizontal
    horizontal = Scale(top, from_=0, to=255, orient=HORIZONTAL)
    horizontal.grid(row=9, column=1)
    my_lab = Label(top, text=horizontal.get())
    my_lab.grid(row=15, column=1)
    buttn = Button(top, text="Update", command=photocopy)
    buttn.grid(row=16, column=1)

def photocopy():
    global output_image

    my_la = Label(top, text=horizontal.get())
    my_la.grid(row=13,column=1)
    threshold = horizontal.get()

    image_to_transform = Image.open(filename)
    output_image = image_to_transform.convert("L")

    for x in range(output_image.width):
        for y in range(output_image.height):

            if output_image.getpixel((x, y)) < threshold:
                input_pixel = output_image.getpixel((x, y))
                replacement_value =(input_pixel  * (threshold - input_pixel )) / (threshold * threshold)
                output_image.putpixel((x, y), int(replacement_value))
            else:

                output_image.putpixel((x, y), 255)
    display_image = ImageTk.PhotoImage(output_image)
    panel2 = Label(top, image=display_image, borderwidth=3, relief="solid")
    panel2.image = display_image
    panel2.grid(row=1, column=3, padx=8)


def nightvision():
    global output_image
    image_to_transform = Image.open(filename)
    output_image = image_to_transform.convert("RGB")

    for x in range(output_image.width):
        for y in range(output_image.height):

            input_pixel = output_image.getpixel((x, y))

            output_R = input_pixel[1]/2
            output_B = output_R*2
            output_G = output_B*2
            output_image.putpixel((x, y), (int(output_R), int(output_G), int(output_B)))

    display_image = ImageTk.PhotoImage(output_image)
    panel2 = Label(top, image=display_image, borderwidth=3, relief="solid")
    panel2.image = display_image
    panel2.grid(row=1, column=3, padx=8)


def showslidervignette():
    global horizontal
    horizontal = Scale(top, from_=0, to=25, orient=HORIZONTAL)
    horizontal.grid(row=9, column=1)
    my_lab = Label(top, text=horizontal.get())
    my_lab.grid(row=15, column=1)
    buttn = Button(top, text="Update", command=vignette)
    buttn.grid(row=16, column=1)

def vignette():
    global output_image
    my_la = Label(top, text=horizontal.get())
    my_la.grid(row=13,column=1)
    threshold = horizontal.get()/100

    image_to_transform = Image.open(filename)
    output_image = image_to_transform.convert("RGB")
    cx = int(output_image.width / 2)
    cy = int(output_image.height / 2)
    maxD = math.sqrt(cx**2 + cy**2)

    for x in range(output_image.width):
        for y in range(output_image.height):
            d = math.sqrt((x-cx)**2 + (y-cy)**2)
            effect = (1 - d/maxD)-threshold
            input_pixel = output_image.getpixel((x, y))

            output_R = input_pixel[0] * effect
            output_G = input_pixel[1] * effect
            output_B = input_pixel[2] * effect
            output_image.putpixel((x, y), (int(output_R), int(output_G), int(output_B)))

    display_image = ImageTk.PhotoImage(output_image)
    panel2 = Label(top, image=display_image, borderwidth=3, relief="solid")
    panel2.image = display_image
    panel2.grid(row=1, column=3, padx=8)

def showsliderposterize():
    global horizontal
    horizontal = Scale(top, from_=4, to=8, orient=HORIZONTAL)
    horizontal.grid(row=9, column=1)
    my_lab = Label(top, text=horizontal.get())
    my_lab.grid(row=15, column=1)
    buttn = Button(top, text="Update", command=posterize)
    buttn.grid(row=16, column=1)

def posterize():
    global output_image

    image_to_transform = Image.open(filename)
    output_image = image_to_transform.convert("RGB")

    for x in range(output_image.width):
        for y in range(output_image.height):

            input_pixel = output_image.getpixel((x, y))

            output_R = getcolor(input_pixel[0])
            output_B = getcolor(input_pixel[2])
            output_G = getcolor(input_pixel[1])
            output_image.putpixel((x, y), (output_R, output_G, output_B))

    display_image = ImageTk.PhotoImage(output_image)
    panel2 = Label(top, image=display_image, borderwidth=3, relief="solid")
    panel2.image = display_image
    panel2.grid(row=1, column=3, padx=8)

def getcolor(color):
    global threshold

    # my_la = Label(top, text=horizontal.get())
    # my_la.grid(row=13,column=1)
    # threshold = horizontal.get()

    # if threshold == 8 :
    if (color < 32):
        return 16
    elif (color > 31 and color < 64):
        return 47
    elif (color > 63 and color < 95):
        return 79
    elif (color > 94 and color < 126):
        return 110
    elif (color > 125 and color < 157):
        return 141
    elif (color > 156 and color < 188):
        return 172
    elif (color > 187 and color < 219):
        return 203
    elif (color > 218 and color < 256):
        return 239

'''
    my_la = Label(top, text=horizontal.get())
    my_la.grid(row=13,column=1)
    threshold = horizontal.get()

    if threshold == 4 :
        if (color < 64):
            return 32
        elif (color > 63 and color < 128):
            return 92
        elif (color > 127 and color < 186):
            return 158
        elif (color > 185 and color < 256):
            return 220

    elif threshold == 7 :
        if (color < 32):
            return 16
        elif (color > 31 and color < 64):
            return 47
        elif (color > 63 and color < 95):
            return 79
        elif (color > 94 and color < 126):
            return 110
        elif (color > 125 and color < 157):
            return 141
        elif (color > 156 and color < 188):
            return 172
        elif (color > 187 and color < 219):
            return 203
        elif (color > 218 and color < 256):
            return 239
'''

def showslidersepia():
    global horizontal
    horizontal = Scale(top, from_=0, to=100, orient=HORIZONTAL)
    horizontal.grid(row=9, column=1)
    my_lab = Label(top, text=horizontal.get())
    my_lab.grid(row=15, column=1)
    buttn = Button(top, text="Update", command=sepia)
    buttn.grid(row=16, column=1)

def sepia():
    global output_image

    my_la = Label(top, text=horizontal.get())
    my_la.grid(row=13,column=1)
    threshold = horizontal.get()

    image_to_transform = Image.open(filename)
    output_image = image_to_transform.convert("RGB")

    for x in range(output_image.width):
        for y in range(output_image.height):

            input_pixel = output_image.getpixel((x, y))

            output_R = (input_pixel[0] * 0.393 + input_pixel[1] * 0.769 + input_pixel[2] * 0.189) - threshold
            output_G = (input_pixel[0] * 0.349 + input_pixel[1] * 0.686 + input_pixel[2] * 0.168) - threshold
            output_B = (input_pixel[0] * 0.272 + input_pixel[1] * 0.534 + input_pixel[2] * 0.131) - threshold
            output_image.putpixel((x, y), (int(output_R), int(output_G), int(output_B)))

    display_image = ImageTk.PhotoImage(output_image)
    panel2 = Label(top, image=display_image, borderwidth=3, relief="solid")
    panel2.image = display_image
    panel2.grid(row=1, column=3, padx=8)


def savefile():

    #imj = Image.open(filename)
    #display_image = ImageTk.PhotoImage(imj)
    #display_image = ImageTk.PhotoImage(Image.open(filename))
    save_imagefile = filedialog.asksaveasfile(initialdir="F:/Pics",
                                        defaultextension='.jpg',
                                        filetypes=[
                                            ("Image file", ".jpg"),
                                            ("All files", ".*"),
                                        ])

    output_image.save(save_imagefile.name)


about_button = Button(root, text="About", width=8, height=2 , padx=10, pady=2, command=popup)
about_button.grid(row=3, column=1, pady=10)

button_exit = Button(root, text="Exit", width=8, height=2, padx=9, pady=2, command=root.quit)
button_exit.grid(row=4, column=1)


root.mainloop()