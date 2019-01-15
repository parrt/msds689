# Isolation Forest Implementation


The goal of this project is to implement the original [Isolation Forest](IsolationForestPaper.pdf) algorithm by Fei Tony Liu, Kai Ming Ting, and Zhi-Hua Zhou.  (A later version of this work is also available: [Isolation-based Anomaly Detection](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.673.5779&rep=rep1&type=pdf).) There are two general approaches to anomaly detection: 

1. model what normal looks like and then look for nonnormal observations
2. focus on the anomalies, which are few and different. This is the interesting and relatively-new approach taken by the authors of isolation forests.

The isolation forest algorithm is original and beautiful in its simplicity; and also seems to work very well, with a few known weaknesses. The academic paper is extremely readable

I have provided some useful code to test and plot the results of your implementation.

**WARNING**: There are sample implementations out there. I will be using [MOSS](https://theory.stanford.edu/~aiken/moss) to compare your programs together and against the known implementations. For example, here are two sample implementations:  [mgckind/iso_forest at github](https://github.com/mgckind/iso_forest/blob/master/iso_forest.py) and [Unsupervised Fraud Detection: Isolation Forest at Kaggle](https://www.kaggle.com/rgaddati/unsupervised-fraud-detection-isolation-forest). You may read these but absolutely no copying. You must learn to implement recursive tree algorithms yourself.

## Data sets

For this project, we'll use three data sets:

* [Kaggle credit card fraud competition data set](https://www.kaggle.com/mlg-ulb/creditcardfraud); download, unzip to get `creditcard.csv`

* Get cancer data into `cancer.csv` by executing [savecancer.csv](https://github.com/parrt/msds689/blob/master/projects/iforest/savecancer.py) that I provide.

* [http.csv.zip](https://github.com/parrt/msds689/blob/master/projects/iforest/http.csv.zip); download, unzip to get `http.csv`.

These files are not that large, but a pure Python solution for isolation forest takes too long on the whole file: 2.5 minutes on `creditcard.csv` and 5 minutes on `http.csv`.  (My hybrid python/C solution takes about two seconds. ha!)

## Visualization of normal versus anomaly separation

Using [plot_anomalies.py](https://github.com/parrt/msds689/blob/master/projects/iforest/plot_anomalies.py), which I provide for you, you can see the results of the isolation forest trying to detect anomalies. These data sets all have known targets indicating normal versus anomaly, but this information is only used during testing and not during training. In other words, we use this information to discover how well we can separate the distribution of normal versus anomalous observations.  The section provides a number of results, but yours might look different because of the inherent randomness involved in selecting subsets of the data and constructing random trees. (click on the images to enlarge.)

<center>
<table border="0">
<tr><td>http.csv, 200 trees, 99% desired TPR</td></tr>
<tr>
<td border=0>
<a href="images/http-200-99.svg"><img src="images/http-200-99.svg" width="350"></a>
</tr>
</table>
</center>

<table border="0">
<tr><td>creditcard.csv, 200 trees, 80% desired TPR</td><td>creditcard.csv, 200 trees, 90% desired TPR</td></tr>
<tr>
<td border=0>
<a href="images/creditcard-200-80.svg"><img src="images/creditcard-200-80.svg" width="350"></a>
<td border=0>
<a href="images/creditcard-200-90.svg"><img src="images/creditcard-200-90.svg" width="350"></a>
</tr>
</table>

<table border="0">
<tr><td> cancer, 300 trees, 70% desired TPR</td><td> cancer, 300 trees, 80% desired TPR</td></tr>
<tr>
<td border=0>
<a href="images/cancer-300-70.svg"><img src="images/cancer-300-70.svg" width="350"></a>
<td border=0>
<a href="images/cancer-300-80.svg"><img src="images/cancer-300-80.svg" width="350"></a>
</tr>
</table>

## Algorithm

For your convenience, here are the algorithms extracted from the Liu *et al* paper:

<table border="0">
<tr>
<td valign="top"><img src="images/iForest.png" width="350"></td><td><img src="images/iTree.png" width="350"></td>
</tr>
<tr>
<td valign="top">
<img src="images/PathLength.png" width="350">
</td>
</td>
Please use this version of average path length `c()`, not the one in the original paper:
<img src="images/avgPathLength.png" width="320">

Then finally here's the scoring formula:

<img src="images/score.png" width="150">
</td>
</tr>
</table>


where "*H(i)* is the harmonic number and it can be estimated by *ln(i)* + 0.5772156649 (Euler’s constant)."

You also have to compute the number of nodes as you construct trees. The scoring test rig uses tree field `n_nodes`:

```python
n_nodes = sum([t.n_nodes for t in it.trees])
print(f"INFO {datafile} {n_nodes} total nodes in {n_trees} trees")
```

## The required API

Your implementation must be in a file called `iforest.py` and define the following classes and methods

```python
class IsolationTreeEnsemble:
    def __init__(self, sample_size, n_trees=10):
        ...
        
    def fit(self, X:np.ndarray, improved=False):
        """
        Given a 2D matrix of observations, create an ensemble of IsolationTree
        objects and store them in a list: self.trees.  Convert DataFrames to
        ndarray objects.
        """
        if isinstance(X, pd.DataFrame):
            X = X.values
        ...
        return self

    def path_length(self, X:np.ndarray) -> np.ndarray:
        """
        Given a 2D matrix of observations, X, compute the average path length
        for each observation in X.  Compute the path length for x_i using every
        tree in self.trees then compute the average for each x_i.  Return an
        ndarray of shape (len(X),1).
        """
        if isinstance(X, pd.DataFrame):
            X = X.values
        ...

    def anomaly_score(self, X:np.ndarray) -> np.ndarray:
        """
        Given a 2D matrix of observations, X, compute the anomaly score
        for each x_i observation, returning an ndarray of them.
        """
        ...

    def predict_from_anomaly_scores(self, scores:np.ndarray, threshold:float) -> np.ndarray:
        """
        Given an array of scores and a score threshold, return an array of
        the predictions: 1 for any score >= the threshold and 0 otherwise.
        """
        ...

    def predict(self, X:np.ndarray, threshold:float) -> np.ndarray:
        "A shorthand for calling anomaly_score() and predict_from_anomaly_scores()."
        ...
```

```python
class IsolationTree:
    def __init__(self, height_limit):
        ...

    def fit(self, X:np.ndarray, improved=False):
        """
        Given a 2D matrix of observations, create an isolation tree. Set field
        self.root to the root of that tree and return it.

        If you are working on an improved algorithm, check parameter "improved"
        and switch to your new functionality else fall back on your original code.
        """
        ...
        return self.root
```

You will either a single tree node definition, or one for decision nodes and one for leaves. That implementation details up to you.

You also need to implement a function used by the scoring test rig:
 
```python
def find_TPR_threshold(y, scores, desired_TPR):
    """
    Start at score threshold 1.0 and work down until we hit desired TPR.
    Step by 0.01 score increments. For each threshold, compute the TPR
    and FPR to see if we've reached to the desired TPR. If so, return the
    score threshold and FPR.
    """
    ...
    return threshold, FPR
```


## Scoring results

Using [score.py](https://github.com/parrt/msds689/blob/master/projects/iforest/score.py), here is a sample run:

```
Running noise=False improved=False
INFO creditcard.csv fit time 0.21s
INFO creditcard.csv 17250 total nodes in 200 trees
INFO creditcard.csv score time 12.78s
SUCCESS creditcard.csv 200 trees at desired TPR 80.0% getting FPR 0.0823%

INFO http.csv fit time 0.25s
INFO http.csv 20326 total nodes in 300 trees
INFO http.csv score time 21.23s
SUCCESS http.csv 300 trees at desired TPR 99.0% getting FPR 0.0063%

INFO cancer.csv fit time 1.41s
INFO cancer.csv 129930 total nodes in 1000 trees
INFO cancer.csv score time 2.38s
SUCCESS cancer.csv 1000 trees at desired TPR 75.0% getting FPR 0.3165%
```

Due to the subsampling of the original data said and the inherent random nature of isolation for us, your results will differ.  I'm hoping that the variance is not so high that valid programs fail the scoring, but let me know.

The indicated required score values were set using my machine and my implementation. Then I gave a range above that that are still allowed as valid.

## Improving on the original algorithm

If you'd like to add noise to see how your algorithm performs, turn on commandline parameter `-noise`. With 5 noise columns, here's what one of my sample runs looks like:

```
Running noise=True improved=False
INFO creditcard.csv fit time 0.24s
INFO creditcard.csv 19758 total nodes in 200 trees
INFO creditcard.csv score time 12.73s
FAIL creditcard.csv FPR 0.1143 > 0.05 +- 30%
ERRORS creditcard.csv 1 errors 200 trees at desired TPR  80.0% getting FPR 0.1143%

INFO http.csv fit time 0.36s
INFO http.csv 30244 total nodes in 300 trees
INFO http.csv score time 20.09s
FAIL http.csv FPR 0.0734 > 0.006 +- 30%
FAIL http.csv n_nodes 30244 > 15200 +- 20%
ERRORS http.csv 2 errors 300 trees at desired TPR  99.0% getting FPR 0.0734%

INFO cancer.csv fit time 1.46s
INFO cancer.csv 128342 total nodes in 1000 trees
INFO cancer.csv score time 2.37s
SUCCESS cancer.csv 1000 trees at desired TPR 75.0% getting FPR 0.3137%
```

Notice that it is starting to fail because of poor performance.

The scoring mechanism knows how to switch mechanisms through the use of the command line option `-improved`.  My improved algorithm with 5 noise columns, looks like this:

```
Running noise=True improved=True
INFO creditcard.csv fit time 0.27s
INFO creditcard.csv 15836 total nodes in 200 trees
INFO creditcard.csv score time 13.00s
SUCCESS creditcard.csv 200 trees at desired TPR 80.0% getting FPR 0.0272%

INFO http.csv fit time 0.35s
INFO http.csv 26284 total nodes in 300 trees
INFO http.csv score time 20.66s
SUCCESS http.csv 300 trees at desired TPR 99.0% getting FPR 0.0134%

INFO cancer.csv fit time 1.27s
INFO cancer.csv 108890 total nodes in 1000 trees
INFO cancer.csv score time 2.39s
SUCCESS cancer.csv 1000 trees at desired TPR 75.0% getting FPR 0.3866%
```

The scoring mechanism is sensitive to the improved algorithm and is a bit more relaxed because it knows the improved algorithm is trying to work on noisy columns.