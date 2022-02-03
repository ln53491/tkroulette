from PIL import Image, ImageTk
import tkinter as tk
import itertools
import os
import shutil
import threading
import time
from random import *
from glob import *
from subprocess import *

def lajkuj():
    print('xd bre')

def igrase(e=None):
    intro = Popen(['other.exe'])
    root.destroy()

def disable_event():
    pass

def update_image_file(dst):
    TEST_IMAGES = glob('Intro/*.png')
    TEST_IMAGES = TEST_IMAGES[:-2]
    for src in itertools.cycle(TEST_IMAGES):
        shutil.copy(src, dst)
        time.sleep(.5)

def refresh_image(canvas, img, image_path, image_id):
    try:
        pil_img = Image.open(image_path)
        img = ImageTk.PhotoImage(pil_img)
        canvas.itemconfigure(image_id, image=img)
    except IOError:
        root.quit()
        img = ImageTk.PhotoImage(Image.open('Intro\\19.png'))
    canvas.after(500, refresh_image, canvas, img, image_path, image_id)  

root = tk.Tk()
root.iconbitmap("Intro/icon.ico")
image_path = 'Intro\\bg.png'
root.title('TkinteRoulette™')
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", disable_event)
th = threading.Thread(target=update_image_file, args=(image_path,))
th.daemon = True
th.start()
while not os.path.exists(image_path):
    time.sleep(.1)

canvas = tk.Canvas(root, height=480, width=1280)
img = None
image_id = canvas.create_image(641, 241, image=img)
canvas.pack()
canvas.config(cursor="circle")
refresh_image(canvas, img, image_path, image_id)
root.after(randint(1000,5000),igrase)
root.mainloop()
