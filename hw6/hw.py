'''
********8
'''

import numpy as np
from scipy.spatial import distance

def synthetic_data():
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
    
    # total data created
    total_data = np.vstack((x1_labled, x2_labled))
    np.random.shuffle(total_data)
    
    return total_data


def n_validator(data, p, classifier, *args):
    
    # data, p, classifier, *args
    np.random.shuffle(data)

    partition = len(data)/p
    total = 0
    
    for i in range(p):
        
        # obtain training and test data
        start = round(partition * i)
        end =  round(partition * (i + 1))
        training = np.delete(data, range(start, end) , 0)
        test = data[range(start, end)]
        
        class_column_index = training.shape[1] - 1 ##########
        
        x = classifier(training, test)
        matches = [i for i in range(len(x)) if int(x[i]) == int(test[i][class_column_index])] ###massive problem
        
        total += len(matches)
 
    return total/len(data)


def NNclassifier(training, test):
    
    class_column_index = training.shape[1] - 1
    
    test_anon = np.delete(test, class_column_index, 1)
    
    # calculates distances matrix
    training_anon = np.delete(training, class_column_index, 1)
    dist = distance.cdist(test_anon, training_anon , 'euclidean')
    
    # calculates lowest point/label and adds it to classification list
    classifiers = list()
    for i in range(len(dist)):    
        lowest_dist_index = np.argsort(dist[i])[0]
        classifiers.append(training[lowest_dist_index][class_column_index])
    
    return classifiers

    
def main():
    with open('cancer_data.txt') as file:
        cancer_data = file.readlines()
    cancer_data = np.array([i.split() for i in cancer_data])
    cancer_data =np.delete(cancer_data.astype('float16'), 0, 1)
    print(n_validator(cancer_data, 5, NNclassifier))

    
main()