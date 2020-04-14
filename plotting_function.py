import numpy as np
import matplotlib.pyplot as plt


def graph(formula, x_range, x_label, y_label, graph_title):
    """
    This function can be used to plot the graphs based on equation of the curve.

Arguments:
    formula {[str]} -- [equation to be plotted]
    x_range {[list]} -- [range of values x axis (start, end, interval)]
    x_label {[type]} -- [title of x axis]
    y_label {[type]} -- [title of y axis]
    graph_title {[type]} -- [title of graph]
    """
    x = np.array(x_range)
    # eval function evaluates the “String” like a python expression and returns the result as an integer
    y = eval(formula)
    plt.plot(x, y)  # used to plot the graphs
    plt.title(graph_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


# To plot engine-oil reliability curve
graph('np.exp(-(x/5190)**1.55)', range(0, 15000, 1000),
      'Hours', 'Reliability', 'Running hours vs Reliability')

# To plot engine-oil failure curve
graph('1-np.exp(-(x/5190)**1.55)', range(0, 15000, 1000),
      'Hours', 'Failure', 'Running hours vs Failure')