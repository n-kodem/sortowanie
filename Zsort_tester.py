from os import read
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import time

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link it to clickExitButton() and place it
        exitButton = Button(self, text="Start test", command=self.clickStartTestBtn)
        exitButton.place(x=70, y=10)

        # text with placement
        mintime = Label(self, text="Just do it")
        mintime.place(x=70,y=40)

        # text with placement
        avgtime = Label(self, text="Just do it")
        avgtime.place(x=70,y=60)

        # text with placement
        maxtime = Label(self, text="Just do it")
        maxtime.place(x=70,y=80)

        numOfLoop = Entry(self, show=None, font=('Arial', 9))
        numOfLoop.place(x=100,y=120,width=50)

        n = StringVar()
        typeOfSorting = ttk.Combobox(self, width = 27, textvariable = n,state="readonly")
        typeOfSorting['values'] = ("1","2","3","4")
        typeOfSorting.current(0)
        typeOfSorting.place(x=150,y=120)
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

            print("Time:", end-start)
        
root = Tk()
app = Window(root)
root.wm_title("Tkinter button")
root.geometry("320x200")
root.mainloop()