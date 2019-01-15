# Isolation Forest Implementation


The goal of this project is to implement the original [Isolation Forest](IsolationForestPaper.pdf) algorithm by Fei Tony Liu, Kai Ming Ting, and Zhi-Hua Zhou.  (A later version of this work is also available: [Isolation-based Anomaly Detection](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.673.5779&rep=rep1&type=pdf).) There are two general approaches to anomaly detection: 

1. model what normal looks like and then look for nonnormal observations
2. focus on the anomalies, which are few and different; this is interesting new approach by the authors of isolation forests.

The isolation forest algorithm is original and beautiful in its simplicity; and also seems to work very well, with a few known weaknesses. The academic paper is extremely readable


I have provided some useful code to plot the results of and test your implementation.

## Data sets

For this project, we'll use three data sets:

* [Credit card fraud](https://www.kaggle.com/mlg-ulb/creditcardfraud); download, unzip to get `creditcard.csv`

* Get cancer data into `cancer.csv` by executing [savecancer.csv](https://github.com/parrt/msds689/blob/master/projects/iforest/savecancer.py) that I provide.

* [http.csv.zip](https://github.com/parrt/msds689/blob/master/projects/iforest/http.csv.zip); download, unzip to get `http.csv`.

These files are not that large, but for a pure Python solution to the isolation forest, they are too big.  For example, my solution takes a few minutes to plow through the credit card data. (My hybrid python/C solution takes about two seconds.)

<center>
<table border=0>
<tr><td>http.csv, 200 trees, 99% desired TPR</td></tr>
<tr>
<td border=0>
<a href="images/http-200-99.svg"><img src="images/http-200-99.svg" width="400"></a>
</tr>
</table>
</center>

<table border=0>
<tr><td>creditcard.csv, 200 trees, 80% desired TPR</td><td>creditcard.csv, 200 trees, 90% desired TPR</td></tr>
<tr>
<td border=0>
<a href="images/creditcard-200-80.svg"><img src="images/creditcard-200-80.svg" width="400"></a>
<td border=0>
<a href="images/creditcard-200-90.svg"><img src="images/creditcard-200-90.svg" width="400"></a>
</tr>
</table>

<table border=0>
<tr><td> cancer, 300 trees, 70% desired TPR</td><td> cancer, 300 trees, 80% desired TPR</td></tr>
<tr>
<td border=0>
<a href="images/cancer-300-70.svg"><img src="images/cancer-300-70.svg" width="400"></a>
<td border=0>
<a href="images/cancer-300-80.svg"><img src="images/cancer-300-80.svg" width="400"></a>
</tr>
</table>

## Algorithm

select features rather than random feature 5%

Here are the algorithms from the Liu *et al* paper:

<img src="images/iForest.png" width="350">

<img src="images/iTree.png" width="350">

<img src="images/PathLength.png" width="350">

<img src="images/avgPathLength.png" width="320">

<img src="images/score.png" width="150">

compute n_nodes

Sample code

https://github.com/mgckind/iso_forest/blob/master/iso_forest.py

Results

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

With 5 noise columns:

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


With 5 noise columns and 3 candidates:

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