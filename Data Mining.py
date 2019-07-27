import pandas as pd
import quandl
import math , datetime
import numpy as np
from sklearn import preprocessing,model_selection, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import pickle
style.use('ggplot')

#df is dataframe
#Obtaining data
df = quandl.get('WIKI/GOOGL')
#Obtaining default features
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
#Works out the High Low Percent and makes new feature collumn
df['HL_PCT'] = (df['Adj. High']-df['Adj. Close']) / df['Adj. Close'] *100
#Works out the Percentage Change and makes new feature collumn
df['PCT_change'] = (df['Adj. Close']-df['Adj. Open']) / df['Adj. Open'] *100
#Refining dataframe with only the important/useful features
df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

forecast_col = 'Adj. Close'
#Filling in null values with nonsense value
df.fillna(-99999, inplace=True)

#Forecast (Prediction)
#Math.ceil prevents decimal
forecast_out = int(math.ceil(0.01*len(df)))
#No of days perdicted
print(forecast_out)
df['label'] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X = X[:-forecast_out]
X_lately = X[-forecast_out:]
df.dropna(inplace=True)
y = np.array(df['label'])
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
#njobs = number of threads
clf = LinearRegression(n_jobs=10)
#Training the classifier
clf.fit(X_train, y_train)

#Pickiling (saving) Trained classfile so we don't have to train again
with open('linearregression.pickle','wb') as f:
    pickle.dump(clf,f)
pickle_in = open('linearregression.pickle','rb')
clf = pickle.load(pickle_in)


accuracy = clf.score(X_test,y_test)

forecast_set=clf.predict(X_lately)
print(forecast_set, accuracy , forecast_out)

df['Forecast'] = np.nan
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date]= [np.nan for _ in range(len(df.columns)-1)] +[i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()