from tkinter import *
from tkinter import messagebox
# from tkinter.messagebox import showinfo
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

        # Start from 1
        self.columnLength = 3
        self.rowLength = 3

        self.master.title("TMobile Bill Calculator")
        self.master.resizable(False, False)
        self.pack(fill=BOTH, expand=1)

        # TOP FRAME
        self.topFrame = Frame(self)
        self.topFrame.pack(side=TOP, fill=BOTH, expand=1)

        self.priceLabel = Label(self.topFrame, text="Base Price:")
        self.priceLabel.grid(row=0, column=2, padx=self.padx, pady=self.pady)
        # print(type(self.priceLabel))
        # if isinstance(self.priceLabel, Label):
        #     print("A Label")


        self.priceEntry = Entry(self.topFrame)
        self.priceEntry.grid(row=0, column=3, padx=self.padx, pady=self.pady)
        self.priceEntry.insert(0, "0.00")
        # print(type(self.priceEntry))
        # if isinstance(self.priceEntry, Entry):
        #     print("An Entry")

        self.nameLabel = Label(self.topFrame, text="Name")
        self.nameLabel.grid(row=1, column=0, padx=self.padx, pady=self.pady)

        self.baseLabel = Label(self.topFrame, text="Base")
        self.baseLabel.grid(row=1, column=1, padx=self.padx, pady=self.pady)

        self.totalLabel = Label(self.topFrame, text="Total")
        self.totalLabel.grid(row=1, column=2, padx=self.padx, pady=self.pady)

        self.firstNameEntry = Entry(self.topFrame)
        self.firstNameEntry.grid(row=2, column=0, padx=self.padx, pady=self.pady)
        self.firstNameEntry.insert(0, "Line_1")

        self.firstBaseEntry = Entry(self.topFrame)
        self.firstBaseEntry.grid(row=2, column=1, padx=self.padx, pady=self.pady)
        self.firstBaseEntry.insert(0, "0.00")

        self.firstTotalEntry = Entry(self.topFrame)
        self.firstTotalEntry.grid(row=2, column=2, padx=self.padx, pady=self.pady)
        self.firstTotalEntry.insert(0, "0.00")

        self.endTotalEntry = Entry(self.topFrame)
        self.endTotalEntry.grid(row=12, column=2, padx=self.padx, pady=self.pady)
        self.endTotalEntry.insert(0, "0.00")


        # BOTTOM FRAME
        self.bottomFrame = Frame(self)
        # self.bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=1)
        self.bottomFrame.pack(side=BOTTOM, fill=BOTH)

        self.addPersonButton = self.makeBottomButton(self.bottomFrame, "Add line", self.addEntry)
        self.addPersonButton.pack(side=LEFT, padx=1)

        self.addColumnButton = self.makeBottomButton(self.bottomFrame, "Add column", self.addColumn)
        self.addColumnButton.pack(side=LEFT, padx=1)

        self.printButton = self.makeBottomButton(self.bottomFrame, "Print", self.printEntries)
        self.printButton.pack(side=LEFT, padx=1)

        self.calculateButton = self.makeBottomButton(self.bottomFrame, "Calculate", self.calculateEntries)
        self.calculateButton.pack(side=LEFT, padx=1)

    def makeBottomButton(self, frame, text, method):
        return Button(frame, text=text, command=method, width=self.buttonWidth, height=self.buttonHeight)

    def addColumn(self):
        # Max column is 6
        if self.columnLength < 6:
            # Move the last column to the next one
            for i in range(1, self.rowLength):
                temp = self.topFrame.grid_slaves(row=i, column=self.columnLength-1)[0]
                temp.grid(row=i, column=self.columnLength, padx=self.padx, pady=self.pady)

            temp = self.topFrame.grid_slaves(row=12, column=self.columnLength-1)[0]
            temp.grid(row=12, column=self.columnLength, padx=self.padx, pady=self.pady)

            # Insert column in place of the previous one
            newColumnTitle = Entry(self.topFrame, justify='center')
            newColumnTitle.grid(row=1, column=self.columnLength-1, padx=self.padx, pady=self.pady)

            newColumnTitle.insert(0, "Additional_" + str(self.columnLength-2))

            for i in range(2, self.rowLength):
                temp = Entry(self.topFrame)
                temp.grid(row=i, column=self.columnLength-1, padx=self.padx, pady=self.pady)
                temp.insert(0, "0.00")

            self.columnLength += 1


    def calculateEntries(self):
        try:
            basePrice = float(self.priceEntry.get())
            numLine = self.rowLength - 2

            # Calculate and display individual price
            individualPrice = basePrice / numLine
            for i in range(2, self.rowLength):
                temp = self.topFrame.grid_slaves(row=i, column=1)[0]
                self.setEntry(temp, self.formatPrice(individualPrice))
                temp.config(state=DISABLED)

            # Calculate and display the total for each line
            totalPriceList = list()
            for i in range(2, self.rowLength):
                totalPrice = individualPrice
                for j in range(2, self.columnLength):
                    temp = self.topFrame.grid_slaves(row=i, column=j)[0]
                    if j == self.columnLength - 1:
                        self.setEntry(temp, self.formatPrice(totalPrice))
                        totalPriceList.append(totalPrice)
                    else:
                        totalPrice += float(temp.get())
                totalPrice = individualPrice

            # Calculate and display the grand total (total of everything)
            grandTotal = sum(totalPriceList)
            self.setEntry(self.endTotalEntry, self.formatPrice(grandTotal))
            self.endTotalEntry.config(state=DISABLED)


        except ValueError:
            messagebox.showwarning("Warning", "Please enter numbers only other than the names!")

        # print(basePrice)

    def setEntry(self, entry, text):
        if str(entry['state']) == "disabled":
            entry.config(state=NORMAL)
        entry.delete(0, 'end')
        entry.insert(0, text)

    def formatPrice(self, num):
        return "{:.2f}".format(num)

    def addEntry(self):
        # Max line is 10
        if self.rowLength < 12:
            for j in range(self.columnLength):
                tempEntry = Entry(self.topFrame)
                tempEntry.grid(row=self.rowLength, column=j, padx=self.padx, pady=self.pady)
                if j == 0:
                    tempEntry.insert(0, "Line_" + str(self.rowLength - 1))
                else:
                    tempEntry.insert(0, "0.00")

            self.rowLength += 1
            self.calculateEntries()

    def printEntries(self):
        pass
        # if self.rowLength > 0:
        #     for i in range(self.rowLength):
        #         for j in range(self.columnLength):
        #             temp = self.topFrame.grid_slaves(row=i, column=j)[0]
        #             print(temp.get())

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
