from tkinter import *
from PIL import ImageTk,Image

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.padx = 5
        self.pady = 5

        self.entryList = list()
        self.columnNum = 2
        self.currentRow = 3

        self.master.title("TMobile Bill Calculator")
        self.pack(fill=BOTH, expand=1)

        # TOP FRAME
        self.topFrame = Frame(self)
        self.topFrame.pack(side=TOP, fill=BOTH, expand=1)

        self.priceLabel = Label(self.topFrame, text="Price:")
        self.priceLabel.grid(row=0, column=5, padx=self.padx, pady=self.pady)

        self.priceEntry = Entry(self.topFrame)
        self.priceEntry.grid(row=0, column=6, padx=self.padx, pady=self.pady)

        self.nameLabel = Label(self.topFrame, text="Name")
        self.nameLabel.grid(row=1, column=0, padx=self.padx, pady=self.pady)

        self.baseLabel = Label(self.topFrame, text="Base")
        self.baseLabel.grid(row=1, column=1, padx=self.padx, pady=self.pady)

        self.firstNameEntry = Entry(self.topFrame)
        self.firstNameEntry.grid(row=2, column=0, padx=self.padx, pady=self.pady)

        self.firstBaseEntry = Entry(self.topFrame, state=DISABLED)
        self.firstBaseEntry.grid(row=2, column=1, padx=self.padx, pady=self.pady)

        # BOTTOM FRAME
        self.bottomFrame = Frame(self)
        # self.bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=1)
        self.bottomFrame.pack(side=BOTTOM, fill=BOTH)

        self.addButton = Button(self.bottomFrame, text="Add", fg="Red", command=self.addEntry, width=40, height=10)
        self.addButton.pack(side=LEFT)

        self.printButton = Button(self.bottomFrame, text="Print", fg="Blue", command=self.printEntries, width=40, height=10)
        self.printButton.pack(side=RIGHT)

    def addEntry(self):
        # entryRow = list()
        # for i in range(self.columnNum):
        #     oneEntry = Entry(self.topFrame)
        #     oneEntry.grid(row = self.currentRow, column = i, padx=self.padx, pady=self.pady)
        if self.currentRow < 12:

            nameEntry = Entry(self.topFrame)
            nameEntry.grid(row = self.currentRow, column = 0, padx=self.padx, pady=self.pady)

            baseEntry = Entry(self.topFrame, state=DISABLED)
            baseEntry.grid(row = self.currentRow, column = 1, padx=self.padx, pady=self.pady)

            self.currentRow += 1
        # print(self.topFrame.grid_size())

    def printEntries(self):
        if self.currentRow > 0:
            for i in range(self.currentRow):
                for j in range(self.columnNum):
                    temp = self.topFrame.grid_slaves(row=i, column=j)[0]
                    print(temp.get())

    def client_exit(self):
        exit()


if __name__ == '__main__':
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
