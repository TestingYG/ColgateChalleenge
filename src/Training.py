import ColgateFeatuerSet as cf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
from sklearn import metrics
import numpy as np
import xgboost as xgb
import pickle

X = cf.df.loc[:, cf.df.columns != 'price']
y = cf.df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

lm = LinearRegression()

lm.fit(X_train, y_train)

predictions = lm.predict(X_test)
#
# plt.xlabel('Price_test')
# plt.ylabel('Price_predictions')
# plt.scatter(y_test, predictions)
# plt.show()


# print('MAE:', metrics.mean_absolute_error(y_test, predictions))
# print('MSE:', metrics.mean_squared_error(y_test, predictions))
# print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
# print('R2:', metrics.r2_score(y_test, predictions))

k_range = range(1, 12)
scores = {}
score_list = {}
lowest_MAE = 5
knn_best = None
model = None
for k in k_range:
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print (metrics.mean_absolute_error(y_test, y_pred), " " , k)
    print (np.sqrt(metrics.mean_squared_error(y_test, y_pred)), " " , k)
    print (metrics.r2_score(y_test, y_pred), " " , k)
    if((metrics.mean_absolute_error(y_test, y_pred) < lowest_MAE)):
        lowest_MAE = metrics.mean_absolute_error(y_test, y_pred)
        knn_best = knn
model = pickle.dump(knn_best, open('model2.pkl', 'wb'))
print(lowest_MAE)
