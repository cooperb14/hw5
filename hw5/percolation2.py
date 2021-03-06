"""
Name: Cooper Bates
UNI: cbb2153

Percolation Module that exhibits functions defined by 1006 Hw5_2
"""
import numpy as np
import matplotlib.pyplot as plt


def read_grid(infile_name):
    """Create a site vacancy matrix from a text file.

    infile_name is the name (a string)  of the
    text file to be read. The method should return 
    the corresponding site vacancy matrix represented
    as a numpy array
    """
    
    in_file = open(infile_name, 'r')
    
    size_n = int(in_file.readline())
    ls = in_file.read().replace('\n',' ').split()
    in_file.close()
    
    array = np.array([int(x) for x in ls])
    array.shape = (size_n,size_n)
    return array


def write_grid(outfile_name,sites):
    """Write a site vacancy matrix to a file.

    outfile_name is a string that is the name of the
    text file to write to. sites is a numpy array
    representing the site vacany matrix to write
    """
    
    out_file = open(outfile_name, 'w')        
    ls = []
    for n in range(len(sites)):
        x = ' '.join([str(i) for i in sites[n]]) + '\n'
        ls.append(x)
    out_file.write(str(sites.shape[0]) + '\n')
    out_file.writelines(ls)
    out_file.close()


def undirected_flow(sites):
    """Returns a matrix of vacant/full sites (1=full, 0=vacant)

    sites is a numpy array representing a site vacancy matrix. This 
    function should return the corresponding flow matrix generated 
    through directed percolation
    """
    
    n = sites.shape[0]
    
    #create empty flow matrix
    full = np.array([0] * n**2)
    full.shape = (n,n)
    
    for j in range(n):
        flow_from(sites, full, 0, j)
    return full


def flow_from(sites,full,i,j):
    """Adjusts the full array for flow from a single site

    This method does not return anything. It changes the array full
    Notice it is not side effect free
    """
    n  = sites.shape[0]
    if 0 <= i < n and 0 <= j < n:
        if sites[i,j] == 1 and full[i,j] != 1:
            full[i,j] = 1
            
            #check right cell
            flow_from(sites, full, i + 1, j)
            
            #check left cell
            flow_from(sites, full, i - 1, j)
            
            #check up cell
            flow_from(sites, full, i, j + 1)
            
            #check below cell
            flow_from(sites, full, i, j - 1)


def percolates(flow_matrix):
    """Returns a boolean if the flow_matrix exhibits percolation

    flow_matrix is a numpy array representing a flow matrix
    """
    
    return bool(sum(flow_matrix[flow_matrix.shape[0] - 1]) > 0)
  

def make_sites(n,p):
    """Returns an nxn site vacancy matrix

    Generates a numpy array representing an nxn site vacancy 
    matrix with site vaccancy probability p
    """
    
    return np.random.binomial(1, p ,(n,n))


def show_perc(sites):
    """Displays a matrix using three colors for vacant, blocked, full
    
    Used to visualize undirected flow on the matrix sites.
    """
    
    x = undirected_flow(sites)
    y = sites
    
    #adds flow and site vacancy matricies to show overlap
    z = x + y
    plt.matshow(z)
    plt.show()


def make_plot(n,trials):
    """"generates and displays a graph of percolation p vs. vacancy p

    estimates percolation probability on an nxn grid for directed 
    percolation by running a Monte Carlo simulation using the variable
    trials number of trials for each point. """
    
    #initializes local variables
    x = []
    y = []
    last_y = 0
    last_x = 0
    p = 0
    
    #sets step size for site vacancy p (x-axis)
    step = .01
    
    while p <= 1:
        
        #calculates percolation p (y-axis)
        d = percolation_prob(n, p, trials)
        j = []
        i = []
        
        #calls adaptive plotting to optimize point plotting
        adaptive_plot(d, p, j, i, last_y, last_x, n, trials)
        j.sort()
        i.sort()
        y.extend(j)
        x.extend(i)
        y.append(d)
        x.append(p)
        last_y = d
        last_x = p
        p += step
        
    #creates plot from the x and y lists, labels plot
    plt.plot(x,y)
    plt.title('Graph of Percolation p vs. Site Vacancy p')
    plt.ylabel('Percolation prob')
    plt.xlabel('Site Vacancy prob')
    plt.show()


def percolation_prob(n, p, trials):
   '''
   Helper function for make_plot that calculates percolation p
   given a specific ndim, site vacancy p, and trials #
   ''' 
   
   total = 0
   for counter in range(trials):
       a = make_sites(n,p)
       b = undirected_flow(a)
       c = percolates(b)
       total += int(c)
   return total/trials


def adaptive_plot(y, x, j, i, last_y, last_x, n, trials):
   '''
   Helper function for make_plot that calculates percolation p
   given a specific ndim, site vacancy p, and trials #
   ''' 
   
   #sets threshold for allowable difference in y-axis points
   threshold = .075
   
   if abs(y - last_y) > threshold:
       x_middle = abs(x - last_x)/2
       y_middle = percolation_prob(n, x_middle, trials)
       j.append(y_middle)
       i.append(x_middle)
       
       #checks threshold difference right of the median
       adaptive_plot(y_middle, x_middle, j, i, last_y, last_x, n, trials)
       
       #checks threshold difference left of the median
       adaptive_plot(y, x, j, i, y_middle, x_middle, n, trials)