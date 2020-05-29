from tkinter import *
from PIL import ImageTk,Image

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        # quitButton = Button(self, text="Exit", command=self.client_exit)
        # quitButton.place(x=0, y=0)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)
        edit.add_command(label="Show Img", command=self.showImg)
        edit.add_command(label="Show Text", command=self.showText)
        menu.add_cascade(label="Edit", menu=edit)

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


root = Tk()
# root.geometry("800x600+0+0")
# Gets the requested values of the height and widht.
# windowWidth = root.winfo_reqwidth()
# windowHeight = root.winfo_reqheight()
# print("Width",windowWidth,"Height",windowHeight)
#
# # Gets both half the screen width/height and window width/height
# positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
# positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
#
# # Positions the window in the center of the page.
# root.geometry("800x600+{}+{}".format(positionRight, positionDown))

rootWidth = 800
rootHeight = 600

windowWidth = root.winfo_screenwidth()
windowHeight = root.winfo_screenheight()

positionRight = int(windowWidth/2 - rootWidth/2)
positionDown = int(windowHeight/2 - rootHeight/2)

root.geometry("{}x{}+{}+{}".format(rootWidth, rootHeight, positionRight, positionDown))

app = Window(root)
root.mainloop()
