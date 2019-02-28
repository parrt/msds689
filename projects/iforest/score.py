import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
import sys
import time

from iforest import IsolationTreeEnsemble, find_TPR_threshold

def score(X, y, n_trees, desired_TPR, datafile,sample_size,
          reqd_fit_time,
          reqd_score_time,
          reqd_FPR,
          reqd_n_nodes):
    it = IsolationTreeEnsemble(sample_size=sample_size, n_trees=n_trees)

    fit_start = time.time()
    it.fit(X, improved=improved)
    fit_stop = time.time()
    fit_time = fit_stop - fit_start
    print(f"INFO {datafile} fit time {fit_time:3.2f}s")

    n_nodes = sum([t.n_nodes for t in it.trees])
    print(f"INFO {datafile} {n_nodes} total nodes in {n_trees} trees")

    score_start = time.time()
    scores = it.anomaly_score(X)
    score_stop = time.time()
    score_time = score_stop - score_start
    print(f"INFO {datafile} score time {score_time:3.2f}s")

    threshold, FPR = find_TPR_threshold(y, scores, desired_TPR)

    y_pred = it.predict_from_anomaly_scores(scores, threshold=threshold)
    confusion = confusion_matrix(y, y_pred)
    TN, FP, FN, TP = confusion.flat
    TPR = TP / (TP + FN)
    FPR = FP / (FP + TN)

    errors = 0
    if fit_time > reqd_fit_time * 2:
        print(f"FAIL {datafile} fit time {fit_time:.1f} > {reqd_fit_time}")
        errors += 1

    if score_time > reqd_score_time * 2:
        print(f"FAIL {datafile} score time {score_time:.1f} > {reqd_score_time}")
        errors += 1

    if TPR < desired_TPR*.9: # TPR must be within 10% (or above)
        print(f"FAIL {datafile} TPR {TPR:.2f} < {desired_TPR} +- 10%")
        errors += 1

    if FPR > reqd_FPR*1.3: # TPR must be within 30%
        print(f"FAIL {datafile} FPR {FPR:.4f} > {reqd_FPR} +- 30%")
        errors += 1

    if n_nodes > reqd_n_nodes*1.15:
        print(f"FAIL {datafile} n_nodes {n_nodes} > {reqd_n_nodes} +- 15%")
        errors += 1

    if errors==0:
        print(f"SUCCESS {datafile} {n_trees} trees at desired TPR {desired_TPR*100.0:.1f}% getting FPR {FPR:.4f}%")
    else:
        print(f"ERRORS {datafile} {errors} errors {n_trees} trees at desired TPR  {desired_TPR*100.0:.1f}% getting FPR {FPR:.4f}%")


def score_cc():
    df = pd.read_csv("creditcard.csv")
    N = 15_000
    df = df.sample(N)  # grab random subset (too slow otherwise)
    if noise: add_noise(df)
    X, y = df.drop('Class', axis=1), df['Class']

    score(X, y, n_trees=300, desired_TPR=.8,
          datafile='creditcard.csv',sample_size=256,
          reqd_fit_time=.45 if noise and improved else 0.4,
          reqd_score_time=20,
          reqd_FPR=.15 if noise and improved else .08,
          reqd_n_nodes=24000 if noise and improved else 27176)


def score_http():
    df = pd.read_csv("http.csv")
    N = 16_000
    df = df.sample(N)  # grab random subset (too slow otherwise)
    if noise: add_noise(df)
    X, y = df.drop('attack', axis=1), df['attack']

    score(X, y, n_trees=300, desired_TPR=.99,
          datafile='http.csv',sample_size=256,
          reqd_fit_time=.37 if noise and improved else 0.2,
          reqd_score_time=21 if noise and improved else 13,
          reqd_FPR=.22 if noise and improved else 0.006,
          reqd_n_nodes=26300 if noise and improved else 22700)


def score_cancer():
    df = pd.read_csv("cancer.csv")
    N = len(df)
    df = df.sample(N)  # grab random subset (too slow otherwise)
    if noise: add_noise(df)
    X, y = df.drop('diagnosis', axis=1), df['diagnosis']

    score(X, y, n_trees=1000, desired_TPR=.75,sample_size=5,
          datafile='cancer.csv',
          reqd_fit_time=0.2,
          reqd_score_time=.75,
          reqd_FPR=.33,
          reqd_n_nodes=8500)


def add_noise(df):
    n_noise = 5
    for i in range(n_noise):
        df[f'noise_{i}'] = np.random.normal(0,100,len(df))


if __name__ == '__main__':
    noise = False
    improved = False
    if '-noise' in sys.argv:
        noise = True
    if '-improved' in sys.argv:
        improved = True

    print(f"Running noise={noise} improved={improved}")
    score_cc()
    print()
    score_http()
    print()
    score_cancer()
