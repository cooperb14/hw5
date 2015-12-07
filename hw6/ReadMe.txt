Name: Cooper Bates
UNI: cbb2153


HW6_1 Nearest Neighbor

Description:
	This module consists of three functions. The two prescribed ones are NNclassifer and n_validator. NNclassifier takes in two data sets as numpy arrays, one training set and one test set, and then uses the cdist method to create an array of the euclidean distances between each point in each array. It then calculates the index for the smallest distance and applies it to the training set to obtain the correlating tag of the “nearest neighbor”. It then appends this tag to an array containing the “best guess” of classifying tags the computer has for all sample points in the test data set given the nearest neighbor approach.

	n_validator takes in several arguments, and essentially works to give a reading on the accuracy of the classifier object inputed as an argument. It does this by first looking at a total data set as well as a partitioning index p inputed as an argument. Using a for loop, it calculates the most even way of breaking the total data set into p parts and then tests the classifier on the data partitions for all the possible combinations with the partitions created.

	synthetic_data simply creates a data set of 600 samples and two classes according to the means and covariances supplied by the assignment.

Bugs:
	No bugs currently, that I have observed.

Additional Comments:
	I have submitted along with this file the Wisconsin Breast Cancer Data as a text file in the format which my program reads it. It is just a modified format of the original downloaded data. The modifications I performed to the data before the program was run are as follows:
	-Replaced all instances of ‘M’ with ‘0’ and all instances of ’B’ with ‘1’
	-Replaced all ‘,’ with ‘ ‘