import matplotlib

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import plotting_function


matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk
import math

style.use("ggplot")


# Creating an animate function for the matplotlib graphs
# def graph1_animate(i):
    # pullData1 = open("sampleData1.txt", "r").read()
    # dataList1 = pullData1.split('\n')
    # xList1 = []
    # yList1 = []

    # for line in dataList1:
    #     if len(line) > 1:
    #         x, y = line.split(',')
    #         xList1.append(int(x))
    #         yList1.append(int(y))

    # In order to avoid overuse of memory
    # a.clear()
    # a.plot(xList1, yList1)


    # time=18000
    # engineOilReliability = plotting_function.dataManipulation(fileName="Sample.txt")
    # # sample txt would be replaced with a file
    # engineOilReliability.computeX(time)
    # engineOilReliability.computeY("np.exp(-(i/5190)**1.55)")
    # # engineOilReliability.graph('Hours', 'Reliability',
    # #                         'Running hours vs Reliability')

    # print (engineOilReliability.x_values)

    # a.clear()
    # a.plot( engineOilReliability.x_values,  engineOilReliability.y_values)

graph = "curve"


f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)


def graph1_animate(i):
    # pullData2 = open("sampleData2.txt", "r").read()
    # dataList2 = pullData2.split('\n')
    # xList2 = []
    # yList2 = []
    # for line in dataList2:
    #     if len(line) > 1:
    #         x, y = line.split(',')
    #         xList2.append(int(x))
    #         yList2.append(int(y))

    #     # In order to avoid overuse of memory
    # a2.clear()
    # a2.plot(xList2, yList2)
    if graph == "curve1":
        print("hello")
        xList2 = [1,2,3]
        yList2 = [1,5,10]
        time=18000
        engineOilReliability = plotting_function.dataManipulation(fileName="Sample.txt")
        # sample txt would be replaced with a file
        engineOilReliability.computeX(time)
        engineOilReliability.computeY("np.exp(-(i/5190)**1.55)")
        # engineOilReliability.graph('Hours', 'Reliability',
        #                         'Running hours vs Reliability')

        print (engineOilReliability.x_values)
        a.clear()
        a.plot(engineOilReliability.x_values, engineOilReliability.y_values)

    elif graph == "curve2":
        print("world")
        time=30000
        engineOilReliability = plotting_function.dataManipulation(fileName="Sample.txt")
        # sample txt would be replaced with a file
        engineOilReliability.computeX(time)
        engineOilReliability.computeY("np.exp(-(i/5190)**1.55)")
        # engineOilReliability.graph('Hours', 'Reliability',
        #                         'Running hours vs Reliability')

        print (engineOilReliability.x_values)
        a.clear()
        a.plot(engineOilReliability.x_values, engineOilReliability.y_values)


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
        for F in (StartPage, PageTwo):
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

def selectGraph(graphName):
    global graph
    graph = graphName
    print("im in select graph")

# Adding a Start page
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="HEALTH \nMONITOR", font=("Times New Roman", 12))
        label.grid(row=0, column=0)

        # button1 = ttk.Button(self, text="Page 1", command=lambda: [controller.show_frame(PageOne),selectGraph("curve1")])
        # button1.grid(row=1, column=1)
        button2 = ttk.Button(self, text="Page 2", command=lambda: [controller.show_frame(PageTwo),selectGraph("curve2")])
        button2.grid(row=2, column=1)


# Adding Page 1
# class PageOne(tk.Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Engine Oil Temperature", font=("Times New Roman", 12))
#         label.grid(row=0, column=1)

#         button1 = ttk.Button(self, text="Home", command=lambda: controller.show_frame(StartPage))
#         button1.grid(row=1, column=1)
#         button2 = ttk.Button(self, text="Page 2", command=lambda: [controller.show_frame(PageTwo),selectGraph("curve2")])
#         button2.grid(row=2, column=1)

#         # canvas1 = FigureCanvasTkAgg(f1, self)
#         # canvas1.draw()
#         # canvas1.get_tk_widget().grid(row=3, column=1)
        
     



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Tire Health", font=("Times New Roman", 12))
        label.grid(row=0, column=1)

        button1 = ttk.Button(self, text="Home", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=1)

        button2 = ttk.Button(self, text="Graph 1", command=lambda:selectGraph("curve1"))
        button2.grid(row=2, column=1)

        button3 = ttk.Button(self, text="Graph 2", command=lambda: selectGraph("curve2"))
        button3.grid(row=3, column=1)

        canvas1 = FigureCanvasTkAgg(f, self)
        canvas1.draw()
        canvas1.get_tk_widget().grid(row=4, column=1)

  


app = HealthGraphs()
graph1 = animation.FuncAnimation(f, graph1_animate, interval=1000)

app.mainloop()
