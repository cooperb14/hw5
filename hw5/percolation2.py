"""
Name: Cooper Bates
UNI: cbb2153

Percolation Module that exhibits functions defined by 1006 Hw5_2
"""
import numpy as np
import matplotlib.pyplot as plt



    
def flow_from(sites,full,i,j):
    """Adjusts the full array for flow from a single site

    This method does not return anything. It changes the array full
    Notice it is not side effect free
    """
    n  = sites.shape[0]
    if 0 <= i < n and 0 <= j < n:
        if sites[i,j] == 1 and full[i,j] != 1:
            full[i,j] = 1
            #check right
            flow_from(sites, full, i + 1, j)
            #check left
            flow_from(sites, full, i - 1, j)
            #check up
            flow_from(sites, full, i, j + 1)
            #check below
            flow_from(sites, full, i, j - 1)
            
def make_sites(n,p):
    """Returns an nxn site vacancy matrix

    Generates a numpy array representing an nxn site vacancy 
    matrix with site vaccancy probability p
    """
    
    return np.random.binomial(1, p ,(n,n))

def percolates(flow_matrix):
    """Returns a boolean if the flow_matrix exhibits percolation
    
    flow_matrix is a numpy array representing a flow matrix
    """
    
    return bool(sum(flow_matrix[flow_matrix.shape[0] - 1]) > 0)
    
    
def undirected_flow(sites):
    """Returns a matrix of vacant/full sites (1=full, 0=vacant)

    sites is a numpy array representing a site vacancy matrix. This 
    function should return the corresponding flow matrix generated 
    through directed percolation
    """
    #create full/flow matrix
    n = sites.shape[0]
    
    full = np.array([0] * n**2)
    full.shape = (n,n)
    
    for j in range(n):
        flow_from(sites, full, 0, j)
    
    return full


def show_perc(sites):
    """Displays a matrix using three colors for vacant, blocked, full
    
    Used to visualize undirected flow on the matrix sites.
    """
    x = undirected_flow(sites)
    y = sites
    z = x + y
    plt.matshow(z)
    plt.show()
    
def make_plot(n,trials):
    """"generates and displays a graph of percolation p vs. vacancy p

    estimates percolation probability on an nxn grid for directed 
    percolation by running a Monte Carlo simulation using the variable
    trials number of trials for each point. """
    
    x = []
    y = []
    p = .01
    
    while p <= 1:
        y.append(p)
        total = 0
        for counter in range(trials):
            a = make_sites(n,p)
            b = undirected_flow(a)
            c = percolates(b)
            total += int(c)
        d = total/trials
        x.append(d)
        p += .01
    plt.plot(x,y)
        
def main():
#    x = np.random.binomial(1, .35 ,(5,5))
#   y = np.array([[0,0, 1, 0, 0],[1, 0, 1, 0, 1],[0, 0, 1, 0, 0],[1, 1, 1, 0, 0],[1, 0, 0, 0, 1]])
#   plt.matshow(y)
#   plt.show()
#   show_perc(y)

# x = np.linspace(0,300,20)
    make_plot(50,200)
    
    
main()