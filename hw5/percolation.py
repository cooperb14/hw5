"""
Name: Cooper Bates
UNI: cbb2153

Percolation Module that exhibits functions defined by 1006 Hw5_1
"""
import numpy as np


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
    
    
def make_sites(n,p):
    """Returns an nxn site vacancy matrix

    Generates a numpy array representing an nxn site vacancy 
    matrix with site vaccancy probability p
    """
    
    return np.random.binomial(1, p ,(n,n))
    
    
def vertical_flow(sites):
    """Returns a matrix of vacant/full sites (1=full, 0=vacant)

    sites is a numpy array representing a site vacancy matrix. This 
    function should return the corresponding flow matrix generated 
    through vertical percolation
    """
    
    size = len(sites)    
    a = []
    x = []
    for n in sites:
        a.extend(n)
        x.extend([0]*size)
    
    x[:size] = a[:size]
    for i in range(size, len(x)):
        x[i] = a[i]
        if not x[i - size]:
            x[i] = 0
    x = np.array(x)
    x.shape = (size,size)
    return x
    
    
def percolates(flow_matrix):
    """Returns a boolean if the flow_matrix exhibits percolation
    
    flow_matrix is a numpy array representing a flow matrix
    """
    
    return bool(sum(flow_matrix[flow_matrix.shape[0] - 1]) > 0)

