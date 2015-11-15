Name: Cooper Bates
UNI: cbb2153


HW5_1 Percolate

Description:
This module percolation.py contains the functions outlined in assignment 5-1. For the read-in function I took in the first line of the file to store the array size, and read in the rest of the file at once using the read method. For write-out I used the write and write_lines methods to print the size and array independently. For make_sites I leveraged a method in the Numpy “random” library to produce an array where each element has a probablity p of being open. For vertical_flow I initially stored the size of the input array, then compressed the array into a 1-d list while simultaneously seeding a separate list of zeros of the same length. The remainder of the function iterates through both lists and alters the elements of the zeros array depending on the condition of its analogous elements in the initial array. By the end the zeros array has become the flow_matrix, and is shaped using the initial dimension value we stored. The Percolates function simply checks if the sum of the elements in the last row is greater than zero. 

Bugs:
No bugs currently, that I have observed. Mind the additional Comments

Additional Comments:
If a matrix is inputed where the dimensions are not square, the program will break. Also, if a text file name is inputed as an argument to the read_grid function, and the file does not exist in the given directory, an error will be thrown. 