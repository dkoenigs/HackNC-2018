import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix  


def decision(size, cat, type, cr, genre):

        data = pd.read_csv('googleplaystore.csv')

        newSize = []

        for x in data['Size']:
            if(x[-1:] == 'M'):
                newSize.append(float(x[:-1]))
            elif(x[-1:] == 'k'):
                newSize.append(float(x[:-1]))
            elif(x[-1:] == 'G'):
                newSize.append(float(x[:-1]))
            else:
                newSize.append(9999999)

        data['newSize'] = newSize
        data.drop(data.columns[2], axis=1, inplace=True)
        data = data[data['newSize'] != 9999999]

        catDummy = pd.get_dummies(data['Category'])
        typeDummy = pd.get_dummies(data['Type'])
        crDummy = pd.get_dummies(data['Content Rating'])
        genreDummy = pd.get_dummies(data['Genres'])

        def semicolon(str):
            if ";" not in str:
                return True
            else:
                return False


        genreList = genreDummy.columns
        newGenreList = []
        for elt in genreList:
            if(semicolon(elt)):
                newGenreList.append(elt)

        genreDummy = genreDummy[newGenreList]

        data = pd.concat([data, catDummy, typeDummy, crDummy, genreDummy], axis = 1)
        cols = [1,2,3,4]

        data.drop(data.columns[cols], axis = 1, inplace=True)

        X = data.values[:, 1:]
        Y = data.values[:, 0]

        X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)

        scaler = StandardScaler()  
        scaler.fit(X_train)

        X_train = scaler.transform(X_train)  
        X_test = scaler.transform(X_test)  

        classifier = KNeighborsClassifier(n_neighbors=3)  
        classifier.fit(X_train, y_train) 
        y_pred = classifier.predict(X_test)

        def catMaker(str):
            catList = []
            for i in range(0, len(catDummy.columns)):
                if str == catDummy.columns[i] :
                    catList.append(1)
                else:
                    catList.append(0)
            return catList

        def typeMaker(str):
            typeList = []
            for i in range(0, len(typeDummy.columns)):
                if str == typeDummy.columns[i]:
                    typeList.append(1)
                else:
                    typeList.append(0)
            return typeList

        def crMaker(str):
            crList = []
            for i in range(0, len(crDummy.columns)):
                if str == crDummy.columns[i]:
                    crList.append(1)
                else:
                    crList.append(0)
            return crList

        def genreMaker(str):
            genreList = []
            for i in range(0, len(genreDummy.columns)):
                if str == genreDummy.columns[i]:
                    genreList.append(1)
                else:
                    genreList.append(0)
            return genreList

        finalList = [size]
        catList = catMaker(cat)
        typeList = typeMaker(type)
        crList = crMaker(cr)
        genreList = genreMaker(genre)
        finalList = finalList + catList + typeList + crList + genreList

        result = classifier.predict([finalList])
        return result[0]

    
def main(longString):
    inputs = longString.split(',')
    inputs[0] = float(inputs[0])

    final = decision(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4])
    return final

   
final = input("What are your parameters: ")
print(main(final))


# plzRun = myPythonClass()
# print(plzRun.main("2.9,COMMUNICATION,FREE,Everyone,Communication"))
