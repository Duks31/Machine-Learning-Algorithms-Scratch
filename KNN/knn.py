
# import sklearn
# from sklearn.model_selection import train_test_split 
# from sklearn.utils import shuffle 
# from sklearn.neighbors import KNeighborsClassifier, kneighbors_graph
# import pandas as pd
# from sklearn import linear_model, preprocessing

# data = pd.read_csv('car.data')

# print(data.head()) #print the top 5 rows
# print(data.tail()) #print the bottom 5 rows 

# le = preprocessing.LabelEncoder() #turning non integer value into integer value


# buying = le.fit_transform(list(data['buying']))
# main = le.fit_transform(list(data['maint']))
# door = le.fit_transform(list(data['door']))
# person = le.fit_transform(list(data['persons']))
# lug_boot = le.fit_transform(list(data['lug_boot']))
# safety = le.fit_transform(list(data['safety']))
# class_ = le.fit_transform(list(data['class']))

# x = list(zip(buying, main, door, person, lug_boot, safety))
# y = list(class_)

# x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y, test_size= 0.1)

# model = KNeighborsClassifier(n_neighbors=9)

# model.fit(x_train, y_train)

# acc = model.score(x_test, y_test)

# print(acc)



# # This will display the predicted class, our data and the actual class
# # We create a names list so that we can convert our integer predictions into 
# # their string representation 
# predicted = model.predict(x_test)
# names = ["unacc", "acc", "good", "vgood"]

# for x in range(len(predicted)):
#     print("Predicted: ", names[predicted[x]], "Data: ", x_test[x], "Actual: ", names[y_test[x]])

# #looking at the neighbors  
# predicted = model.predict(x_test)
# names = ["unacc", "acc", "good", "vgood"]

# for x in range(len(predicted)):
#     print("Predicted: ", names[predicted[x]], "Data: ", x_test[x], "Actual: ", names[y_test[x]])
#     # Now we will we see the neighbors of each point in our testing data
#     n = model.kneighbors([x_test[x]], 9, True)
#     print("N: ", n)



    

