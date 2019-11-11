# MARK:- Libsfrom NaiveBayes import NaiveBayes
import numpy as np
import json
import re
from NaiveBayes import NaiveBayes

group_train = []

# MARK:- support function

# get label by comparing individual tags' labels


def max(positive, negative, neutral):
    if positive == negative:
        return 2
    if positive > negative:
        if neutral > positive:
            return 2
        return 1
    if negative > positive:
        if neutral > negative:
            return 2
        return 0


# MARK:- Get content from json data file
with open('test.json', encoding='utf8') as json_file:
    reviews = json.load(json_file)
    comments = []
    labels = []
    tags = []
    for rev in reviews:
        comments.append(rev['comment'])
        tags.append(rev['tags'])

    for tag in tags:
        positive = 0
        negative = 0
        neutral = 0

        for attr in tag.values():
            for val in list(attr.values()):
                if val == "positive":
                    positive += 1
                if val == "negative":
                    negative += 1
                if val == "neutral":
                    neutral += 1
        labels.append(max(positive, negative, neutral))


# MARK:- start training data
train_data = comments  # list
train_labels = labels  # np.array

# for i in range(0, 10):
#     print(train_labels[i])

nb = NaiveBayes(np.unique(train_labels))  # instantiate a NB class object
print("---------------- Training In Progress --------------------")

# start tarining by calling the train function
nb.train(train_data, train_labels)
print('----------------- Training Completed ---------------------')


# newsgroups_test = fetch_20newsgroups(
#     subset='test', categories=categories)  # loading test data
# test_data = newsgroups_test.data  # get test set examples
# test_labels = newsgroups_test.target  # get test set labels

# print("Number of Test Examples: ", len(test_data))
# print("Number of Test Labels: ", len(test_labels))

# pclasses = nb.test(test_data)  # get predcitions for test set

# # check how many predcitions actually match original test labels
# test_acc = np.sum(pclasses == test_labels)/float(test_labels.shape[0])

# print("Test Set Examples: ", test_labels.shape[0])
# print("Test Set Accuracy: ", test_acc*100, "%")
