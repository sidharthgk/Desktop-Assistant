from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import threading
import main  # Import your main.py file

class GUI:
    def __init__(self, master):
        self.master = master
        master.geometry("800x600")
        master.lift()
        master.attributes("-topmost", True)
        self.show_intro_animation()
        self.create_buttons()

    def show_intro_animation(self):
        lbl = Label(self.master)
        lbl.place(x=0, y=0)
        self.load_gif(lbl, "bot.gif")

    def load_gif(self, label, filename):
        img = Image.open(filename)
        for frame in ImageSequence.Iterator(img):
            frame = frame.resize((800, 600))
            frame = ImageTk.PhotoImage(frame)
            label.config(image=frame)
            label.image = frame  # Keep a reference to prevent garbage collection
            self.master.update()
            time.sleep(0.05)

    def create_buttons(self):
        speak_button = Button(self.master, text="Speak", command=self.start_listening)
        speak_button.place(x=350, y=550)

    def start_listening(self):
        # Call the start_listening function from main.py in a separate thread
        threading.Thread(target=main.start_listening).start()

def main():
    root = Tk()
    gui = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
