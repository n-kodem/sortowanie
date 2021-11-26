from os import read
from heap_sort import *
from insertion_sort import *
from quicksort import *
from bubble_sort import *
from mergesort import *
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import time

def sorttest(name,repeat,array):
    sort_times = []

    for i in range(repeat):
        start = time.time()
        quicksort(array.copy())
        end = time.time()
        sort_times.append(end-start)
    
    return [min(sort_times),sum(sort_times)/len(sort_times),max(sort_times)]
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
        global mintime
        mintime = Label(self, text="Just do it")
        mintime.place(x=70,y=40)

        # text with placement
        global avgtime
        avgtime = Label(self, text="Just do it")
        avgtime.place(x=70,y=60)

        # text with placement
        global maxtime
        maxtime = Label(self, text="Just do it")
        maxtime.place(x=70,y=80)

        global numOfLoop
        numOfLoop = Entry(self, show=None, font=('Arial', 9))
        numOfLoop.place(x=100,y=120,width=50)

        n = StringVar()
        global typeOfSorting 
        typeOfSorting = ttk.Combobox(self, width = 27, textvariable = n,state="readonly")
        typeOfSorting['values'] = ("heap_sort","insertion_sort","quicksort","bubble_sort","mergesort")
        typeOfSorting.current(0)
        typeOfSorting.place(x=150,y=120)
    def clickStartTestBtn(self):
        filename = fd.askopenfilename()
        if filename != "":
            print(filename)
            with open("inp.txt", "r+") as file1:
                data=list(map(int,[i.replace("\n","") for i in file1.readlines()]))
            print(data)
            sorts = sorttest(typeOfSorting.get(),numOfLoop.get(),data)
            mintime.set(sorts[0])
            avgtime.set(sorts[1])
            maxtime.set(sorts[2])
            

        
root = Tk()
app = Window(root)
root.wm_title("Tkinter button")
root.geometry("320x200")
root.mainloop()