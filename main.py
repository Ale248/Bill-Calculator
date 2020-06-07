from tkinter import *
from PIL import ImageTk,Image

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.entryList = list()
        self.columnNum = 2
        self.currentRow = 0

        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        # quitButton = Button(self, text="Exit", command=self.client_exit)
        # quitButton.place(x=0, y=0)

        # menu = Menu(self.master)
        # self.master.config(menu=menu)
        #
        # file = Menu(menu)
        # file.add_command(label="Exit", command=self.client_exit)
        # menu.add_cascade(label="File", menu=file)
        #
        # edit = Menu(menu)
        # edit.add_command(label="Show Img", command=self.showImg)
        # edit.add_command(label="Show Text", command=self.showText)
        # menu.add_cascade(label="Edit", menu=edit)

        # TOP FRAME
        self.topFrame = Frame(self, bg="Blue")
        self.topFrame.pack(side=TOP, fill=BOTH, expand=1)

        # self.blueButton = Button(self.topFrame, text="Blue", fg="Blue")
        # self.blueButton.pack(side=TOP, anchor=NW)
        #
        # self.blackButton = Button(self.topFrame, text="Black", fg="Black")
        # self.blackButton.pack(side=TOP, anchor=NW)
        # self.entry1 = Entry(self.topFrame)
        # self.entry1.pack(side=TOP, anchor=NW)


        # BOTTOM FRAME
        self.bottomFrame = Frame(self, bg="Red")
        self.bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

        self.addButton = Button(self.bottomFrame, text="Add", fg="Red", command=self.addEntry)
        self.addButton.pack(side=LEFT)

    def addEntry(self):
        entryRow = list()
        for i in range(self.columnNum):
            oneEntry = Entry(self.topFrame)
            oneEntry.grid(row = self.currentRow, column = i)
        # topEntry = Entry(self.topFrame)
        # topEntry.insert(END, str(len(self.entryList)))
        # topEntry.pack(side=TOP, anchor=NW)
        # self.entryList.append(topEntry)

        self.currentRow += 1
        print(self.topFrame.grid_size())

    def showImg(self):
        load = Image.open("pic.jpg").resize((100, 100))
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def showText(self):
        text = Label(self, text="Helloooo")
        text.pack()

    def client_exit(self):
        exit()


window = Tk()

windowWidth = 800
windowHeight = 600

# display window in center of screen
# -------------
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

positionRight = int(screenWidth/2 - windowWidth/2)
positionDown = int(screenHeight/2 - windowHeight/2)

window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, positionRight, positionDown))
# -------------

app = Window(window)
window.mainloop()
