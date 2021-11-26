from tkinter import *
from tkinter import filedialog as fd
import time

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link it to clickExitButton() and place it
        exitButton = Button(self, text="Start test", command=self.clickStartTestBtn)
        exitButton.place(x=0, y=0)

        # text with placement
        text = Label(self, text="Just do it")
        text.place(x=70,y=90)

        numOfLoop = Entry(self, show=None, font=('Arial', 9))
        numOfLoop.place(x=100,y=120,width=50)

    def clickStartTestBtn(self):
        filename = fd.askopenfilename()
        if filename != "":
            print(filename)
            with open("inp.txt", "r+") as file1:
                data=list(map(int,[i.replace("\n","") for i in file1.readlines()]))
            print(data)
            start = time.time()
            a = 0
            for i in range(1000):
                a += (i**100)
            end = time.time()
            
            # difference of start and end variables
            # gives the time of execution of the
            # program in between
            print("The time of execution of above program is :", end-start)
        
root = Tk()
app = Window(root)
root.wm_title("Tkinter button")
root.geometry("320x200")
root.mainloop()