from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

def predict(inputFeatures):

    inputFeatures = [[7.7,2.6,6.9,2.3]]    
    iris = datasets.load_iris()

    knn = KNeighborsClassifier()
    knn.fit(iris.data, iris.target)

    predictInt = knn.predict(inputFeatures)
    if predictInt[0] == 0:
        predictString = 'setosa'
    elif predictInt[0] == 1:
        predictString = 'versicolor'
    elif predictInt[0] == 2:
        predictString = 'virginica'
    else:
        predictString = 'null3'

   #return predictString
    print '################## RESULT ##########################################################'
    print 'Input(slength, swidth, plength , pwidth) :', inputFeatures
    print "Predicted species : " ,  predictString
    print '####################################################################################'    


if __name__ == '__main__':
    predict()
