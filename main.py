from tkinter import *
from tkinter import messagebox
# from tkinter.messagebox import showinfo
from PIL import ImageTk,Image

import pyperclip
import datetime

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.entriesText = ""

        self.now = datetime.datetime.now()
        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

        self.years = list()
        for year in range(self.now.year - 10, self.now.year + 11):
            self.years.append(year)

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

        self.dateLabel = Label(self.topFrame, text="Month and Year:")
        self.dateLabel.grid(row=0, column=0, padx=self.padx, pady=self.pady, sticky=E)

        self.monthsVariable = StringVar(self.topFrame)
        self.monthsVariable.set(self.months[self.now.month - 1])
        self.monthOption = OptionMenu(self.topFrame, self.monthsVariable, *self.months)
        self.monthOption.grid(row=0, column=1, padx=0, pady=self.pady, sticky=E)

        self.yearsVariable = StringVar(self.topFrame)
        self.yearsVariable.set(self.years[10])
        self.yearOption = OptionMenu(self.topFrame, self.yearsVariable, *self.years)
        self.yearOption.grid(row=0, column=2, padx=0, pady=self.pady, sticky=W)

        self.priceLabel = Label(self.topFrame, text="Base Price:")
        self.priceLabel.grid(row=0, column=3, padx=self.padx, pady=self.pady)

        self.priceEntry = Entry(self.topFrame)
        self.priceEntry.grid(row=0, column=4, padx=self.padx, pady=self.pady)
        self.priceEntry.insert(0, "0.00")

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

        # self.addPersonButton = self.makeBottomButton(self.bottomFrame, "Add line", self.addEntry)
        # self.addPersonButton.pack(side=LEFT, padx=1)

        # Frame for add line and remove line
        # ----------
        self.lineFrame = Frame(self.bottomFrame)
        self.lineFrame.pack(side=LEFT, fill=BOTH)

        # self.addPersonButton = self.makeBottomButton(self.lineFrame, "Add line", self.addEntry)
        self.addPersonButton = Button(self.lineFrame, text="Add line", command=self.addEntry, width=self.buttonWidth, height=int(self.buttonHeight/2), bg="Green")
        self.addPersonButton.pack(side=TOP)

        self.removePersonButton = Button(self.lineFrame, text="Remove line", command=self.removeEntry, width=self.buttonWidth, height=int(self.buttonHeight/2), bg="Red")
        self.removePersonButton.pack(side=TOP)
        # ----------

        # Frame for add column and remove column
        # ----------
        self.columnFrame = Frame(self.bottomFrame)
        self.columnFrame.pack(side=LEFT, fill=BOTH)

        # self.addPersonButton = self.makeBottomButton(self.lineFrame, "Add line", self.addEntry)
        self.addColumnButton = Button(self.columnFrame, text="Add column", command=self.addColumn, width=self.buttonWidth, height=int(self.buttonHeight/2), bg="Green")
        self.addColumnButton.pack(side=TOP)

        self.removeColumnButton = Button(self.columnFrame, text="Remove column", command=self.removeColumn, width=self.buttonWidth, height=int(self.buttonHeight/2), bg="Red")
        self.removeColumnButton.pack(side=TOP)



        # ----------
        # self.addColumnButton = self.makeBottomButton(self.bottomFrame, "Add column", self.addColumn)
        # self.addColumnButton.pack(side=LEFT, padx=1)

        # self.printButton = self.makeBottomButton(self.bottomFrame, "Print", self.printEntries)
        # self.printButton.pack(side=LEFT, padx=1)

        self.clipboardButton = self.makeBottomButton(self.bottomFrame, "Copy to clipboard", self.copyEntries)
        self.clipboardButton.pack(side=LEFT, padx=1)

        self.calculateButton = self.makeBottomButton(self.bottomFrame, "Calculate", self.calculateEntries)
        self.calculateButton.pack(side=LEFT, padx=1)


    def copyEntries(self):
        # may 2020: (284.06)
        # 6 people = 209.89 = 34.99 each
        # medi = 34.99
        # ander = 34.99 + 16.96 + 57.21 = 109.16
        # ale = 34.99
        # albert = 34.99
        # martin = 34.99
        # george = 34.99

        # pyperclip.copy("")

        self.calculateEntries()
        result = ""
        grandTotalString = str(self.endTotalEntry.get())
        numPeople = str(self.rowLength - 2)
        basePrice = str(self.priceEntry.get())
        individualPrice = str(self.topFrame.grid_slaves(row=2, column=1)[0].get())

        currentMonth = self.monthsVariable.get()
        currentYear = self.yearsVariable.get()


        result += "{} {}: ({})\n".format(currentMonth, currentYear, grandTotalString)
        result += "{} people = {} = {} each\n".format(numPeople, basePrice, individualPrice)

        for i in range(2, self.rowLength):
            for j in range(self.columnLength):
                temp = self.topFrame.grid_slaves(row=i, column=j)[0]
                num = temp.get()
                # Name
                if j == 0:
                    result += "{} = ".format(num)
                elif j == 1:
                    result += "{} ".format(num)
                elif j < self.columnLength - 1:
                    if float(num) > 0:
                        result += "+ {} ".format(num)
                else:
                    result += "= {}\n".format(num)


        print(result)



    def removeColumn(self):
        if self.columnLength > 3:
            for i in range(1, self.rowLength):
                temp = self.topFrame.grid_slaves(row=i, column=self.columnLength-2)[0]
                temp.destroy()

                tempA = self.topFrame.grid_slaves(row=i, column=self.columnLength-1)[0]
                tempA.grid(row=i, column=self.columnLength-2, padx=self.padx, pady=self.pady)

            self.endTotalEntry.grid(row=12, column=self.columnLength-2, padx=self.padx, pady=self.pady)
            self.columnLength -= 1


    def removeEntry(self):
        if self.rowLength > 3:
            for j in range(self.columnLength):
                temp = self.topFrame.grid_slaves(row=self.rowLength-1, column=j)[0]
                temp.destroy()

            self.rowLength -= 1


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

            # Formats the base price
            self.setEntry(self.priceEntry, self.formatPrice(basePrice))


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
