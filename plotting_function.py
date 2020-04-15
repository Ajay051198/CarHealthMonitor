import numpy as np
import matplotlib.pyplot as plt



debug=False

class dataManipulation():
    """
        This class is used to read a text file, use the data to calculate
        corresponding value of reliability and plot the graph

    """

    def __init__(self,fileName):
        self.x_values = []
        self.y_values = []
        self.fileName = fileName

    def computeX(self,time):
        """
            This method is used to read the data from the text file and
            store it in a form of list

        Arguments:
            filename {[string]} -- [.txt file from which the time data is read]

        Returns:
            [list] -- [Data from the file stored in a list]
        """
        

        # with open(self.fileName, 'r') as filehandle:
        #     for line in filehandle:
        #         line.rstrip("\n")
        #         # remove linebreak which is the last character of the string np.exp(-(i/5190)**1.55)
        #         currentData = line[:-1]

        #         # add item to the list
        #         self.x_values.append(float(currentData))
                

        timeinc=0

        for i in range(40+1):
            stepSize=time/40
            
            self.x_values.append(timeinc)
            timeinc=timeinc+stepSize
        print(self.x_values)

                    

        

    def computeY(self, formula):
        """
            This method is used to calculate the value corresponding to x.
            It will compute the equation based on the x value and the formula provided  

        Arguments:
            formula {[string]} -- [Equation used to compute y]

        Returns:
            [list] -- [The calculated y value is stored in a form of list]
        """

        for i in self.x_values:
            y = eval(formula)
            self.y_values.append(y)

    def graph(self, x_label, y_label, graph_title):
        """
        This function can be used to plot the graphs based on equation of the curve.

    Arguments:
        x_label {[type]} -- [title of x axis]
        y_label {[type]} -- [title of y axis]
        graph_title {[type]} -- [title of graph]
        """
        x = np.array(self.x_values)
        # eval function evaluates the “String” like a python expression and returns the result as an integer
        y = self.y_values
        plt.plot(x, y)  # used to plot the graphs
        plt.title(graph_title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()


if debug==True:
    engineOilReliability = dataManipulation(fileName="Sample.txt")
    engineOilReliability.computeX(18000)
    engineOilReliability.computeY("np.exp(-(i/5190)**1.55)")
    engineOilReliability.graph('Hours', 'Reliability',
                            'Running hours vs Reliability')


#     # # To plot engine-oil failure curve
# engineOilFailure = Plotting()
# engineOilFailure.graph('1-np.exp(-(x/5190)**1.55)', range(0, 15000, 1000),
#           'Hours', 'Failure', 'Running hours vs Failure')
