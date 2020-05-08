# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd

datasetdna = pd.read_json('dna.json', lines = True)
X_dna = datasetdna.iloc[: ,[0,1,2]]
count = 0

for i in range(0,3023):
    x= X_dna["category"][i]
    if x == "to be inserted" :
        X_dna = X_dna.drop([i])
    
datasetfirstpost = pd.read_json('firstpost.json', lines = True)
X_firstpost = datasetfirstpost.iloc[: ,[0,1,2]]
count = 0
x= X_firstpost["category"][1]

for i in range(0,3852):
    x= X_firstpost["category"][i]
    if x == "to be inserted" :
        X_firstpost = X_firstpost.drop([i])




datasetzee = pd.read_json('zee.json', lines = True)
X_zee = datasetzee.iloc[: ,[0,1,2]]
count = 0
x= X_zee["category"][1]

for i in range(0,3282):
    x= X_zee["category"][i]
    if x == "to be inserted" :
        X_zee = X_zee.drop([i])
        


datasetndtv = pd.read_json('ndtv.json', lines = True)
X_ndtv = datasetndtv.iloc[: ,[0,1,2]]
count = 0
x= X_ndtv["category"][1]

for i in range(0,4949):
    x= X_ndtv["category"][i]
    if x == "to be inserted" :
        X_ndtv = X_ndtv.drop([i])
        
datasetoneindia = pd.read_json('oneindia.json', lines = True)
X_oneindia = datasetoneindia.iloc[: ,[0,1,2]]
count = 0

for i in range(0,4365):
    x= X_oneindia["category"][i]
    if x == "to be inserted" :
        X_oneindia = X_oneindia.drop([i])
        

datasetnews18 = pd.read_json('news18.json', lines = True)
X_news18 = datasetnews18.iloc[: ,[0,1,2]]
count = 0

for i in range(0,4396):
    x= X_news18["category"][i]
    if x == "to be inserted" :
        X_news18 = X_news18.drop([i])
        

datasetrepublic = pd.read_json('republic.json', lines = True)
X_republic = datasetrepublic.iloc[: ,[0,1,2]]
count = 0

for i in range(0,2976):
    x= X_republic["category"][i]
    if x == "to be inserted" :
        X_republic = X_republic.drop([i])

datasetthehindu = pd.read_json('thehindu.json', lines = True)
X_thehindu = datasetthehindu.iloc[: ,[0,1,2]]
count = 0

for i in range(0,2030):
    x= X_thehindu["category"][i]
    if x == "to be inserted" :
        X_thehindu = X_thehindu.drop([i])


nlpdata = pd.concat([X_dna, X_firstpost, X_ndtv,X_zee,X_republic,X_news18,X_thehindu,X_oneindia], ignore_index=True)


X = nlpdata.iloc[: , [0,2]]
y = nlpdata.iloc[: , [1]]

import re
import nltk


nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
set(stopwords.words('english'))
for i in range(0,23406):
    news = re.sub('[^a-zA-Z]', ' ', X["_id"][i])
    news= news.lower()
    news = news.split()
    ps = PorterStemmer()
    news = [word for word in news if not word in {'http','www','dnaindia','com','zeenews', 'oneindia', 'ndtv','firstpost','news18','republicworld','thehindu'} ]
    news = [ps.stem(word) for word in news if not word in set(stopwords.words('english'))]
    
    news = ' '.join(news)
    corpus.append(news)

for i in range(0, 23406):
    news = re.sub('[^a-zA-Z]', ' ', X["headline"][i])
    news = news.lower()
    news = news.split()
    ps = PorterStemmer()
    news = [word for word in news if not word in {'www','dnaindia','com','zeenews', 'oneindia', 'ndtv','firstpost','news18','republicworld','thehindu'} ]
    news = [ps.stem(word) for word in news if not word in set(stopwords.words('english'))]
    
    news = ' '.join(news)
    corpus[i] = corpus[i] + news

#from numpy import array
X = np.array(corpus)    
y=np.array(nlpdata['category'][:23406])
#y = nlpdata['category'][:23406]   
#X = X.reshape(X.shape[1:])
#X = X.transpose()
    
import pickle


with open('X.pickle','wb') as f:
    pickle.dump(X,f)


with open('y.pickle','wb') as f:
    pickle.dump(y,f)
    
    
with open('X.pickle','rb') as f:
    X= pickle.load(f)


with open('y.pickle','rb') as f:
    y = pickle.load(f)

#X = ['india photo galleri pentagon shoot media report f say us suspend secur assist pak janpentagon shoot media report f']

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

vectorizer = CountVectorizer(min_df = 1, max_df = 1.0, max_features = 2000 ,stop_words =stopwords.words('english'),ngram_range=(1, 2))
X = vectorizer.fit_transform(X).toarray()

#X = vectorizer.transform(X).toarray()

tfidf = TfidfTransformer()
X = tfidf.fit_transform(X).toarray()

#X = tfidf.transform(X).toarray()

from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
# dividing X, y into train and test data 
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size= 0.6, random_state = 2) 

# training a KNN classifier 
from sklearn.neighbors import KNeighborsClassifier 
knn = KNeighborsClassifier(n_neighbors = 7).fit(X_train, y_train) 
  

# accuracy on X_test 
accuracy = knn.score(X_test, y_test) 
print(accuracy) 
  
# creating a confusion matrix 
knn_predictions = knn.predict(X_test)  
cm = confusion_matrix(y_test, knn_predictions) 


# training a linear SVM classifier 
from sklearn.svm import SVC 
svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X_train, y_train) 
svm_predictions = svm_model_linear.predict(X) 

print(svm_predictions)
# model accuracy for X_test   
accuracy_svm = svm_model_linear.score(X_test, y_test) 
print(accuracy_svm)
# creating a confusion matrix 
#cm = confusion_matrix(y_test, svm_predictions) 


with open('vectorizer.pickle','wb') as f:
    pickle.dump(vectorizer,f)


with open('tfidf.pickle','wb') as f:
    pickle.dump(tfidf,f)
    
    
with open('svm_model_linear.pickle','wb') as f:
    pickle.dump(svm_model_linear,f)


with open('knn.pickle','wb') as f:
    pickle.dump(knn,f)
