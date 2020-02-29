import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_train = pd.read_csv("./data_merged.csv",delimiter=',')
data_train['rain'] = data_train.apply(lambda x: int(x['rain']>0.1), axis = 1)
data_train = data_train[data_train['name'] != "Taxi"]

# Random Shuffle
data_train = data_train.sample(frac=1).reset_index(drop=True)

# training data
X_des = data_train['destination'].tolist()
X_source = data_train['source'].tolist()
X_name = data_train['name'].tolist()
X_time = data_train['time'].tolist()
X_weekday = data_train['weekday'].tolist()
X_rain = data_train['rain'].tolist()

# Location and name_type encoding
cab_type_map = {"Lyft":0, "Uber":1}
loc_type = {"North Station":0, "South Station":1, "North End":2, "Northeastern University":3, "Boston University":4,
           "Back Bay":5, "Beacon Hill":6, "Fenway":7,"Financial District":8, "Haymarket Square":9,"West End":10,
            "Theatre District":11}
name_type = {"Shared":0, "Lux":1, "Lux Black XL":2, "Lyft XL":3, "Lux Black":4, "Lyft":5, "UberPool":6,"UberX":7,
             "UberXL":8,"Black":9,"Black SUV":10, "WAV":11}


X_des = [loc_type[i] for i in X_des]
X_source = [loc_type[i] for i in X_source]
X_name = [name_type[i] for i in X_name]
X_time = [int(i.split(':')[0])*24+int(i.split(':')[1]) for i in X_time]
X = np.column_stack((X_des,X_source,X_name,X_time,X_weekday,X_rain))
X = X.tolist()
Y = data_train['price'].tolist()

# Training Data Random spliting
from sklearn.model_selection import train_test_split
X_train, X_valid, Y_train, Y_valid = train_test_split(X,Y,test_size=0.2,random_state = 43)

# Testing data
data_test = pd.read_csv("./data_test.csv",delimiter=',')

X_des_test = data_test['destination'].tolist()
X_source_test = data_test['source'].tolist()
X_name_test = data_test['name'].tolist()
X_time_test = data_test['time'].tolist()
X_weekday_test = data_test['weekday'].tolist()
X_rain_test = data_test['rain'].tolist()
X_des_test = [loc_type[i] for i in X_des_test]
X_source_test = [loc_type[i] for i in X_source_test]
X_name_test = [name_type[i] for i in X_name_test]
X_time_test = [int(i.split(':')[0])*24+int(i.split(':')[1]) for i in X_time_test]
X_test = np.column_stack((X_des_test,X_source_test,X_name_test,X_time_test,X_weekday_test,X_rain_test))
Y_test = data_test['price'].tolist()

# count accuracy
def accuracy(errors_data, data):
    '''
    :param errors_data:
    :param data:
    :return:
    '''
    mape = 100 * (errors_data / data)
    return 100 - np.mean(mape)

# print out the result
def Result_show(errors_train, errors_valid, errors_test, accuracy_train,accuracy_valid, accuracy_test):
    '''
    :param errors_train:
    :param errors_valid:
    :param errors_test:
    :param accuracy_train:
    :param accuracy_valid:
    :param accuracy_test:
    :return:
    '''

    print('Training Mean Absolute Error:', round(np.mean(errors_train), 2), 'degrees.')
    print('Validation Mean Absolute Error:', round(np.mean(errors_valid), 2), 'degrees.')
    print('Test Mean Absolute Error:', round(np.mean(errors_test), 2), 'degrees.')
    print('Train Accuracy:', round(accuracy_train, 2), '%.')
    print('Valid Accuracy:', round(accuracy_valid, 2), '%.')
    print('Test Accuracy:', round(accuracy_test, 2), '%.')

# Plot estimated and actural price in testset
def chart_show(Y_test_predict,Y_test):

    sns.lineplot(range(200),Y_test_predict,label="Predicted Price")
    sns.lineplot(range(200),Y_test,label="Actual Price")
    plt.legend(loc="upper left")
    plt.ylabel('Price')
    plt.xlabel("index")
    plt.title('Test Set price prediction')
    plt.show()


# ---------------------------------------------------------------------------------
# Random Forest

from sklearn.ensemble import RandomForestRegressor,RandomForestClassifier

rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
X_train_sample = X_train[:50000]
Y_train_sample = Y_train[:50000]
X_valid_sample = X_valid[:10000]
Y_valid_sample = Y_valid[:10000]

rf.fit(X_train_sample, Y_train_sample);
Y_predict_train = rf.predict(X_train_sample)
errors_train = abs(Y_predict_train - Y_train_sample)
Y_predict_valid = rf.predict(X_valid_sample)
errors_valid = abs(Y_valid_sample - Y_predict_valid)
Y_test_predict = rf.predict(X_test)
errors_test = abs(Y_test - Y_test_predict)

accuracy_train = accuracy(errors_train, Y_train_sample)
accuracy_valid = accuracy(errors_valid, Y_valid_sample)
accuracy_test = accuracy(errors_test, Y_test)

Result_show(errors_train, errors_valid, errors_test, accuracy_train,accuracy_valid, accuracy_test)

# Plot the test set prediction result
chart_show(Y_test_predict[:200], Y_test[:200])

# ---------------------------------------------------------------------------------
# SVM

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
Y = [int(i) for i in Y]
X_train, X_valid, Y_train, Y_valid = train_test_split(X,Y,test_size=0.2,random_state = 43)
clf = SVC(gamma='auto')
X_train_sample = X_train[:50000]
Y_train_sample = Y_train[:50000]
X_valid_sample = X_valid[:10000]
Y_valid_sample = Y_valid[:10000]

clf.fit(X_train_sample, Y_train_sample)
SVC(gamma='auto')

Y_predict_train = clf.predict(X_train_sample)
errors_train = abs(Y_predict_train - Y_train_sample)
Y_predict_valid = clf.predict(X_valid_sample)
errors_valid = abs(Y_valid_sample - Y_predict_valid)
Y_test_predict = clf.predict(X_test)
errors_test = abs(Y_test - Y_test_predict)

accuracy_train = accuracy(errors_train, Y_train_sample)
accuracy_valid = accuracy(errors_valid, Y_valid_sample)
accuracy_test = accuracy(errors_test, Y_test)

Result_show(errors_train, errors_valid, errors_test, accuracy_train,accuracy_valid, accuracy_test)
chart_show(Y_test_predict[:200], Y_test[:200])

# ---------------------------------------------------------------------------------
# Decision tree

from sklearn import tree
clf =tree.DecisionTreeClassifier()
clf = clf.fit(X_train, Y_train)

Y_predict_train = clf.predict(X_train)
errors_train = abs(Y_predict_train - Y_train)
Y_predict_valid = clf.predict(X_valid)
errors_valid = abs(Y_valid - Y_predict_valid)
Y_test_predict = clf.predict(X_test)
errors_test = abs(Y_test - Y_test_predict)

accuracy_train = accuracy(errors_train, Y_train)
accuracy_valid = accuracy(errors_valid, Y_valid)
accuracy_test = accuracy(errors_test, Y_test)

Result_show(errors_train, errors_valid, errors_test, accuracy_train,accuracy_valid, accuracy_test)
chart_show(Y_test_predict[:200], Y_test[:200])
