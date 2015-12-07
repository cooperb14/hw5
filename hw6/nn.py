'''
Name: Cooper Bates
UNI: cbb2153

Fufills the specifications of Nearest Neighbor assignment part 1
'''

import numpy as np
from scipy.spatial import distance

def synthetic_data():
    '''
    Generates a synthetic data set of 600 samples classified into
    two categories
    '''    
    
    #means
    m1 = [2.5, 3.5]
    m2 = [.5, 1]
    
    #covariance
    cov1 = [[1,1],[1,4.5]]
    cov2 = [[2,0],[0,1]]
    
    
    #class 1 created
    x1 = np.random.multivariate_normal(m1,cov1,300)
    labels = np.zeros(300)
    labels.shape = (300,1)
    x1_labled = np.hstack((x1, labels))
    
    #class 2 created
    x2 = np.random.multivariate_normal(m2,cov2,300)
    labels = np.ones(300)
    labels.shape = (300,1)
    x2_labled = np.hstack((x2, labels))
    
    # total data set created and shuffled
    total_data = np.vstack((x1_labled, x2_labled))
    np.random.shuffle(total_data)
    
    return total_data


def n_validator(data, p, classifier, *args):
    '''
    Takes in a total data set, and partitions it in several different ways,
    testing the classifier on the data during each partition
    '''
    
    # shuffles data set
    np.random.shuffle(data)
    
    # sets partition value
    partition = data.shape[0]/p
    total = 0
    
    for i in range(p):
        
        # set start and end row indicies for partition
        start = round(partition * i)
        end =  round(partition * (i + 1))
        
        # obtain training and test data
        training = np.delete(data, range(start, end) , 0)
        test = data[range(start, end)]
        
        class_index = training.shape[1] - 1
         
        # obtain classifications for test partition
        x = classifier(training, test)
        
        # check classifications against actual classifications
        matches = [i for i in range(len(x)) if x[i] == test[i][class_index]]

        total += len(matches)
 
    return total/data.shape[0]


def NNclassifier(training, test):
    '''
    Classiefier funciton that takes in training data and its lables, and
    using nearest neighbor, calculates the most probable lable for the
    samples in the test data set.
    '''
    
    class_index = training.shape[1] - 1
    
    # strips test set of classifications
    test_anon = np.delete(test, class_index, 1)
    
    # calculates distances matrix
    training_anon = np.delete(training, class_index, 1)
    dist = distance.cdist(test_anon, training_anon , 'euclidean')
        
    # calculates lowest point/label and adds it to classification list
    classifiers = list()
    for i in range(dist.shape[0]):    
        lowest_dist_index = np.argsort(dist[i])[0]
        classifiers.append(training[lowest_dist_index][class_index])

    return np.array(classifiers)