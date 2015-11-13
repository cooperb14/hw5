"""
Name: Cooper Bates
UNI: cbb2153

This is the main funciton provided to test our percolation module
"""
import percolation as perc

def main():
    site_matrix=perc.make_sites(3,0.45)
    perc.write_grid('sites.txt',site_matrix)
    sites_read=perc.read_grid('sites.txt')
#    print(sites_read)
    sites_flow=perc.vertical_flow(sites_read)
#    print(sites_flow)
    if perc.percolates(sites_flow):
        print('percolates')
    else:
        print('does not percolate')
        
main()