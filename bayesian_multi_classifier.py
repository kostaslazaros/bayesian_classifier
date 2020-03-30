import os
import numpy
from pandas import DataFrame as df
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


def read_files(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)
            with open(path, 'r', encoding='utf-8') as fil:
                message = fil.read()
            yield path, message


def df_from_dir(path, classification):
    rows = []
    index = []
    for filename, message in read_files(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)
    return df(rows, index=index)


def create_df(data_dir):
    categories = {}
    for root, dirnames, filenames in os.walk(data_dir):
        for adir in dirnames:
            categories[adir] = os.path.join(data_dir, adir)
    data = df({'message': [], 'class': []})
    for categorie, cat_dir in categories.items():
        data = data.append(df_from_dir(cat_dir, categorie))
    return data, categories


def train(train_data):
    vectorizer = CountVectorizer()
    counts = vectorizer.fit_transform(train_data['message'].values)
    classifier = MultinomialNB()
    targets = train_data['class'].values
    classifier.fit(counts, targets)
    return classifier, vectorizer


def predict(data, classifier, vectorizer):
    data_counts = vectorizer.transform(data)
    predictions = classifier.predict(data_counts)
    return predictions


class Predict:
    def __init__(self, data_directory):
        traindata, categories = create_df(data_directory)
        self.classifier, self.vectorizer = train(traindata)
        print('Trained classifier with categories:', list(categories.keys()))

    def predict_one(self, str2predict):
        data_counts = self.vectorizer.transform([str2predict])
        predictions = self.classifier.predict(data_counts)
        return predictions[0]


if __name__ == '__main__':
    datadir = './categories/'
    prd = Predict(datadir)
    print(prd.predict_one('Ελλάδα 1940 πόλεμος'))
