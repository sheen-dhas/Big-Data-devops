from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

def predict(inputFeatures):

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
    print predictString


if __name__ == '__main__':
  # predict([[1.5,0.7,1.3,0.3],[1.5,0.7,1.3,0.3]])
    predict([[7.0,3.2,4.7,1.4],[7.0,3.2,4.7,1.4]])
  # predict([[1.5,0.7,1.3,0.3],[7.0,3.2,4.7,1.4]])
