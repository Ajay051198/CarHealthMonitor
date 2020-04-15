import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt

import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import plotting_function
import tkinter as tk
from tkinter import ttk
import math

style.use("ggplot")

# Creating an object for the figure to be plot
f = plt.figure()

select_param = "TIRE"
programName = "tire"
chartLoad = True
paneCount = 1


# Creating a method for menu parameters
def changeParam(toWhat, pn):
    global select_param
    global programName

    select_param = toWhat
    programName = pn


# Creating an animate function for the matplotlib graphs


def animate(i):
    if chartLoad:
        if paneCount == 1:
            try:

                if select_param == "OIL":
                    a = plt.subplot2grid((6, 4), (0, 0), rowspan=5, colspan=4)
                    time = 18000
                    engineOilReliability = plotting_function.dataManipulation(fileName="Sample.txt")
                    # sample txt would be replaced with a file
                    engineOilReliability.computeX(time)
                    engineOilReliability.computeY("np.exp(-(i/5190)**1.55)")
                    # engineOilReliability.graph('Hours', 'Reliability',
                    #                         'Running hours vs Reliability')

                    print(engineOilReliability.x_values)
                    a.clear()
                    a.set_xlabel("time")
                    a.set_ylabel("Reliability Index")
                    a.plot(engineOilReliability.x_values, engineOilReliability.y_values, label="legend")
                    a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,
                             ncol=2, borderaxespad=0)
                    title = "OIL HEALTH "
                    a.set_title(title)

                elif select_param == "TIRE":
                    a = plt.subplot2grid((6, 4), (0, 0), rowspan=5, colspan=4)
                    time = 30000
                    engineOilReliability = plotting_function.dataManipulation(fileName="Sample.txt")
                    # sample txt would be replaced with a file
                    engineOilReliability.computeX(time)
                    engineOilReliability.computeY("np.exp(-(i/5190)**1.55)")
                    # engineOilReliability.graph('Hours', 'Reliability',
                    #                         'Running hours vs Reliability')

                    print(engineOilReliability.x_values)
                    a.clear()
                    a.set_xlabel("time")
                    a.set_ylabel("Reliability Index")
                    a.plot(engineOilReliability.x_values, engineOilReliability.y_values, label="legend")
                    a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,
                             ncol=2, borderaxespad=0)
                    title = "TIRE HEALTH "
                    a.set_title(title)

            except Exception as e:
                print(e)


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

        # Adding a menu bar
        menubar = tk.Menu(container)

        paramChoice = tk.Menu(menubar, tearoff=1)
        paramChoice.add_command(label="TIRE DATA",
                                command=lambda: changeParam("TIRE", "tire"))
        paramChoice.add_command(label="OIL DATA",
                                command=lambda: changeParam("OIL", "oil"))
        menubar.add_cascade(label="Select Data", menu=paramChoice)

        tk.Tk.config(self, menu=menubar)

        # creating an empty dictionary for all the frames that we will create
        self.frames = {}

        # creating a for loop for every new page
        for F in (StartPage, PageOne):
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
        label.pack(padx=10, pady=10)

        button1 = ttk.Button(self, text="View Graphs",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack(padx=10, pady=10)


# Adding Page 1
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Reliability Graphs", font=("Times New Roman", 12))
        label.pack(padx=10, pady=10)

        button1 = ttk.Button(self, text="Home", command=lambda: controller.show_frame(StartPage))
        button1.pack(padx=10, pady=10)

        canvas1 = FigureCanvasTkAgg(f, self)
        canvas1.draw()
        canvas1.get_tk_widget().pack(padx=10, pady=10)


app = HealthGraphs()
graph = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()
