Name: Cooper Bates
UNI: cbb2153


HW5_2 Percolate

Description:
	This module percolation2.py contains the functions outlined in assignment 5-2. For the read_grid function the first line of the file is taken in to store the array size, and the rest of the file is read at once using the read method. For write_grid, write and write_lines methods are used to print the size and array independently.

	Undirected_flow calls the flow_from function on each of the elements in the first row of the array. The flow_from function is a recursive function that uses the states of the flow and site vacancy matrix to follow an undirected flow path from each top-row element, and fill in the flow matrix accordingly.

	The Percolates function simply checks if the sum of the elements in the last row is greater than zero. The make_sites function leverages a method in the Numpy “random” library to produce an array where each element has a probability p of being open. Show_perc leverages the colormap function of matplotlib.py and the combination of the flow and site arrays to produce a visual of the sites/flow.

	Make_plot uses the matplotlib.py plot function to plot two lists against one another. The x list is filled with values of regular interval of between 0 and 1, with a step of .01 chosen for plotting speed, since accuracy is added by adaptive_plot helper function. At each step on the x axis, the percolation probability of a certain number of trials given by the user is calculated and appended to the y list.(The number of trials to calculate percolation probability is ultimately given by the user, however it is recommended that it be above 5000 for accuracy within a .01 range.) After the percolation probability is calculated at each step, a helper function called adaptive_plot is called. This function is a recursive function that checks the difference in y values between the current and last step, and if greater than a certain threshold, currently set to .075, then it will recursively estimate intermediary points to make plot smoother while still preserving plotting speed.


Bugs:
	No bugs currently, that I have observed. Since two functions are recursive, if their arguments are very low numbers it may exceed the computer’s Recursion Depth, producing an error. Mind the additional Comments

Additional Comments:
	If a matrix is inputed where the dimensions are not square, the program will break. Also, if a text file name is inputed as an argument to the read_grid function, and the file does not exist in the given directory, an error will be thrown.

	With the make_plot and adaptive_plot function, the step variable in make_plot and the threshold_variable in adaptive_plot can be modified to create a graph more oriented toward plotting speed, or data point accuracy. The current way it is initialized is oriented more for plotting speed.

In its current state the graph takes a little over two minutes to plot. 