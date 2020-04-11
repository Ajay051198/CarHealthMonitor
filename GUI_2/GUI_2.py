import tkinter as tk
from tkinter import ttk
import math


# BASE-LINE code for adding pages

class HealthGraphs(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Adding an icon for the GUI
        tk.Tk.iconbitmap(self, default="graph.ico")

        # Adding the GUI title
        tk.Tk.wm_title(self, "Car Health Monitor")

        # Pulling in the current systems screen height and width info
        width_value = (self.winfo_screenwidth() / 2.5)
        height_value = (self.winfo_screenheight() / 2.5)

        # Setting up a minimum size for the GUI
        tk.Tk.wm_minsize(self, math.ceil(width_value), math.ceil(height_value))

        # Adding a window frame
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)  # 0 is the min size, weight is the priority
        container.grid_columnconfigure(0, weight=1)

        # creating an empty dictionary for all the frames that we will create
        self.frames = {}

        # creating a for loop for every new page
        for F in (StartPage, PageOne, PageTwo):
            # creating a start page for the GUI
            frame = F(container, self)

            self.frames[F] = frame

            # assigning the location
            frame.grid(row=0, column=0, sticky="nsew")  # nswe = north,south,east,west. Can be expanded in all
            # directions

        # showing up of a frame StartPage whenever this GUI opens
        self.show_frame(StartPage)

    def show_frame(self, cont):
        # cont is the key for the self.frames dictionary in the __init method
        frame = self.frames[cont]
        frame.tkraise()  # brings up thw window to the top


# Adding a Start page
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="HEALTH \nMONITOR", font=("Times New Roman", 12))
        label.grid(row=0, column=0)

        button1 = ttk.Button(self, text="Page 1", command=lambda: controller.show_frame(PageOne))
        button1.grid(row=1, column=1)
        button2 = ttk.Button(self, text="Page 2", command=lambda: controller.show_frame(PageTwo))
        button2.grid(row=2, column=1)


# Adding Page 1
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Engine Oil Temperature", font=("Times New Roman", 12))
        label.grid(row=0, column=0)

        button1 = ttk.Button(self, text="Home", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=1)
        button2 = ttk.Button(self, text="Page 2", command=lambda: controller.show_frame(PageTwo))
        button2.grid(row=2, column=1)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Tire Health", font=("Times New Roman", 12))
        label.grid(row=0, column=0)

        button1 = ttk.Button(self, text="Home", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=1)

        button2 = ttk.Button(self, text="Page 1", command=lambda: controller.show_frame(PageOne))
        button2.grid(row=2, column=1)


app = HealthGraphs()

app.mainloop()