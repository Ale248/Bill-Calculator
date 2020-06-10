from tkinter import *
from PIL import ImageTk,Image

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.padx = 3
        self.pady = 3

        self.buttonWidth = 27
        self.buttonHeight = 10

        self.entryList = list()
        self.currentColumn = 3
        self.currentRow = 3

        self.master.title("TMobile Bill Calculator")
        self.master.resizable(False, False)
        self.pack(fill=BOTH, expand=1)

        # TOP FRAME
        self.topFrame = Frame(self)
        self.topFrame.pack(side=TOP, fill=BOTH, expand=1)

        self.priceLabel = Label(self.topFrame, text="Price:")
        self.priceLabel.grid(row=0, column=2, padx=self.padx, pady=self.pady)

        self.priceEntry = Entry(self.topFrame)
        self.priceEntry.grid(row=0, column=3, padx=self.padx, pady=self.pady)

        self.nameLabel = Label(self.topFrame, text="Name")
        self.nameLabel.grid(row=1, column=0, padx=self.padx, pady=self.pady)

        self.baseLabel = Label(self.topFrame, text="Base")
        self.baseLabel.grid(row=1, column=1, padx=self.padx, pady=self.pady)

        self.totalLabel = Label(self.topFrame, text="Total")
        self.totalLabel.grid(row=1, column=2, padx=self.padx, pady=self.pady)

        self.firstNameEntry = Entry(self.topFrame)
        self.firstNameEntry.grid(row=2, column=0, padx=self.padx, pady=self.pady)

        self.firstBaseEntry = Entry(self.topFrame, state=DISABLED)
        self.firstBaseEntry.grid(row=2, column=1, padx=self.padx, pady=self.pady)

        self.firstTotalEntry = Entry(self.topFrame, state=DISABLED)
        self.firstTotalEntry.grid(row=2, column=2, padx=self.padx, pady=self.pady)

        # BOTTOM FRAME
        self.bottomFrame = Frame(self)
        # self.bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=1)
        self.bottomFrame.pack(side=BOTTOM, fill=BOTH)

        # self.addPersonButton = Button(self.bottomFrame, text="Add line", fg="Red", command=self.addEntry, width=27, height=10)
        self.addPersonButton = self.makeBottomButton(self.bottomFrame, "Add line", self.addEntry)
        self.addPersonButton.pack(side=LEFT, padx=1)

        # self.addColumnButton = Button(self.bottomFrame, text="Add column", fg="Black", command=self.addColumn, width=27, height=10)
        self.addColumnButton = self.makeBottomButton(self.bottomFrame, "Add column", self.addColumn)
        self.addColumnButton.pack(side=LEFT, padx=1)

        # self.printButton = Button(self.bottomFrame, text="Print", fg="Blue", command=self.printEntries, width=27, height=10)
        self.printButton = self.makeBottomButton(self.bottomFrame, "Print", self.printEntries)
        self.printButton.pack(side=LEFT, padx=1)

        # self.calculateButton = Button(self.bottomFrame, text="Calculate", fg="Black", command=self.calculateEntries, width=27, height=10)
        self.calculateButton = self.makeBottomButton(self.bottomFrame, "Calculate", self.calculateEntries)
        self.calculateButton.pack(side=LEFT, padx=1)

    def makeBottomButton(self, frame, text, method):
        return Button(frame, text=text, command=method, width=self.buttonWidth, height=self.buttonHeight)

    def addColumn(self):
        # newColumnTitle = Entry(self.topFrame)
        # newColumnTitle.grid(row=0, column=self.currentColumn-1, padx=self.padx, pady=self.pady)
        # for i in range(self.currentRow):

        # Max column is 6
        if self.currentColumn < 6:
            # Move the last column to the next one
            for i in range(1, self.currentRow):
                temp = self.topFrame.grid_slaves(row=i, column=self.currentColumn-1)[0]
                temp.grid(row=i, column=self.currentColumn, padx=self.padx, pady=self.pady)

            # Insert column in place of the previous one
            newColumnTitle = Entry(self.topFrame, justify='center')
            newColumnTitle.grid(row=1, column=self.currentColumn-1, padx=self.padx, pady=self.pady)
            for i in range(2, self.currentRow):
                temp = Entry(self.topFrame)
                temp.grid(row=i, column=self.currentColumn-1, padx=self.padx, pady=self.pady)

            self.currentColumn += 1


    def calculateEntries(self):
        pass

    def addEntry(self):
        # entryRow = list()
        # for i in range(self.columnNum):
        #     oneEntry = Entry(self.topFrame)
        #     oneEntry.grid(row = self.currentRow, column = i, padx=self.padx, pady=self.pady)
        if self.currentRow < 12:

            nameEntry = Entry(self.topFrame)
            nameEntry.grid(row=self.currentRow, column=0, padx=self.padx, pady=self.pady)

            baseEntry = Entry(self.topFrame, state=DISABLED)
            baseEntry.grid(row=self.currentRow, column=1, padx=self.padx, pady=self.pady)

            totalEntry = Entry(self.topFrame, state=DISABLED)
            totalEntry.grid(row=self.currentRow, column=2, padx=self.padx, pady=self.pady)

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
