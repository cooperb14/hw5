import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
import string

def main():

    
    #class 1 created
    x1 = np.array([[0, 0], [0, 3]])
    labels = np.zeros(2)
    labels.shape = (2,1)
    x1_labled = np.hstack((x1, labels))
    
    #class 2 created
    x2 = np.array([[0, 4.5], [0, 6.75]])
    labels = np.ones(2)
    labels.shape = (2,1)
    x2_labled = np.hstack((x2, labels))
    
    # total data obtained
    total_data = np.vstack((x1_labled, x2_labled))
    np.random.shuffle(total_data)

    
    # training and test
    training = np.delete(total_data, range(2, 4), 0)
    test = np.delete(total_data, range(0, 2), 0)
    test_anon = np.delete(test, 2, 1)
    
    # takes in training and test, gives classifier Number
    print(training)
    print(" ")
    print(test_anon[0])
    print(" ")
    dist = distance.cdist(test_anon, np.delete(training, 2, 1), 'euclidean')
    low = np.argsort(dist[0])[0]
    print(training[low][2])
#    print(test[0][2])
    
def expense():
    with open('expense.txt') as file:
        expenses = file.read()
    expenses = expenses.replace('\n', ' ')
    expenses = expenses.replace('+', '-')
    s = ''
    for i in expenses:
        if i.isdigit() or i == ' ' or i == '.' or i == '-':
            s = s + i
    y = [float(x) for x in s.split()]
    print(y)
    print(sum(y))
    
    
expense()
