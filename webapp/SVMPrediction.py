import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
import pickle

class SVMPrediction:

    def detecting(reviews):


        #train_news = pd.read_csv(train_file)
        #tfidf = TfidfVectorizer(stop_words='english',use_idf=True,smooth_idf=True) #TF-IDF
        
        #knn_pipeline = Pipeline([('lrgTF_IDF', tfidf), ('lrg_mn', KNeighborsClassifier())])

        filename = 'D:\\Source Code\\Canteen\\webapp\\svm_model.sav'
    
        #pickle.dump(knn_pipeline.fit(train_news['review'], train_news['sentiment']), open(filename, 'wb'))
        train = pickle.load(open(filename, 'rb'))
        #print(reviews)
        predicted_class = train.predict(reviews)
        #print(type(test_news["review"])
        return predicted_class



if __name__ == "__main__":
    pass
    #NB.detecting('testset.csv')

