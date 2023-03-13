from __future__ import print_function

from comet_ml import Experiment

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.pipeline import Pipeline

from sklearn.datasets import fetch_20newsgroups

from sklearn.linear_model import SGDClassifier

from sklearn.metrics import accuracy_score

from sklearn.model_selection import KFold

import numpy as np


def convert_to_np(dataset):
    return np.asarray(dataset.data), dataset.target


experiment = Experiment(api_key="YOUR KEY HERE", project_name="cross-validation")

experiment.set_name("20 newsgroups cross validated")

# Get dataset and put into train,test lists

categories = ["alt.atheism", "soc.religion.christian", "comp.graphics", "sci.med"]

x_validation, y_validation = convert_to_np(
    fetch_20newsgroups(
        subset="test", categories=categories, shuffle=True, random_state=42
    )
)

x_train, y_train = convert_to_np(
    fetch_20newsgroups(
        subset="train", categories=categories, shuffle=True, random_state=42
    )
)

kf = KFold(n_splits=10)

curr_fold = 0

acc_list = []

for train_idx, test_idx in kf.split(x_train):

    text_clf = Pipeline(
        [
            ("vect", CountVectorizer()),  # Counts occurrences of each word
            (
                "tfidf",
                TfidfTransformer(),
            ),  # Normalize the counts based on document length
            (
                "clf",
                SGDClassifier(
                    loss="hinge",
                    penalty="l2",  # Call classifier with vector
                    alpha=1e-3,
                    random_state=42,
                    max_iter=5,
                    tol=None,
                ),
            ),
        ]
    )

text_clf.fit(x_train[train_idx].tolist(), y_train[train_idx])

# Predict unseen test data based on fitted classifer

predicted = text_clf.predict(x_train[test_idx])

# Compute accuracy

acc = accuracy_score(y_train[test_idx].tolist(), predicted)

acc_list.append(acc)

experiment.log_metric("accuracy_fold_%s" % curr_fold, acc)

curr_fold += 1

experiment.log_metric("average accuracy", np.average(acc_list))

