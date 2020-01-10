# Implementing kmeans clustering

The goal of this project is to get more practice implementing algorithms, as well as translating pseudocode algorithms to Python. This project is also very loosely defined as it is much more realistic. Previously, I very carefully laid out exactly the process to follow. Now you will have to think about the whole problem and plan your approach. Further, the exact assessment rubric is not specified. Your goal is to produce a notebook (and submit a PDF version) that is a kind of report or tutorial you might publish, detailing your exploration of kmeans clustering. (This could be useful as an artifact to send to potential employers.)

These algorithms were surprisingly challenging to get working because there are a number of pitfalls that can take a while to debug. With probability 92.5%, you will be asked to describe kmeans clustering during interviews.

You will work under `kmeans-`*userid* repo.

## kmeans

First, you must implement the standard kmeans algorithm:

<img src="kmeans.png" width="550">

and put into file `kmeans.py` in root directory of your repo.  You can import that file into your notebook using the following from one of the cells:

```
%run kmeans
```

Your function must follow this interface:

```python
def kmeans(X:np.ndarray, k:int, centroids=None, tolerance=1e-2):
    ...
    return centroids, clusters
```

where `centroids` is an *k* x *p* matrix containing the *k* centroids (vectors are *p* long). The `clusters` return value is a list of length *k* containing lists of observation indexes associated with every cluster. I use the tolerance as a general guideline for comparing previous and next generation centroids. If the norm of the two flattened centroid lists is less than the tolerance, I stop.  By default, `centroids=None` indicates that your algorithm should randomly select *k* unique centroids. Here's a sample run on one dimensional data:

<img src="sample-run.png" width="400">

Your software must also handle more than one dimensional data. For example, on the cancer data set there are *p*=30 features.

If `centroids='kmeans++'` then your algorithm should use the kmeans++ mechanism for selecting initial centroid. 

## kmeans++

You must find the kmeans++ initial centroid identification algorithm somewhere on the web and implement that in your kmeans.py file.

The basic idea is to randomly pick the first of *k* centroids. Then, pick next *k*-1 points by selecting points that maximize the minimum distance to all existing cluster centroids. So for each point, compute the minimum distance to each cluster.  Among those min distances to clusters for each point, find the max distance. The associated point is the new centroid.

Here's a sample run on the cancer data set for me:

<img src="cancer.png" width="400">

You will notice that I have generated a confusion matrix but how do we know which centroid is associated with which true label (we don't have the *y* target to work with during clustering)?  What I do is to find the most common prediction in each cluster and then assume that is the prediction, flipping each element in that cluster to the appropriate label. Then, we can compare those results to the known *y*.

## Application to image compression

In the introduction to machine learning course, we looked at the application of clustering to image compression. Rather than use millions of colors, we can usually get away with 256 or even 64 colors. The key is choosing the right colors that are representative for that image. The way to do that is to cluster in *p*=3 space for (red,green,blue) vectors. But, it's a good idea to start with grayscale.

### Greyscale

Here's an original picture from North Africa taken by my father during World War II and one with just k=4 levels of gray:

<img src="north-africa-1940s-grey.png" width="50%"><img src="just-4-greys.png" width="50%">

My code looks something like this:

```python
k=4
centroids, clusters = kmeans(X_, k=k, centroids='kmeans++', tolerance=.01)
centroids = centroids.astype(np.uint8)
reassign_grey(X, centroids)
img_ = Image.fromarray(X.reshape(h,w), 'L') # L means grayscale
img_.show()
```

Note that you have to write a function to convert all of the values to one of the values in `centroids`.

### Color

As an example of color compression, here is your favorite instructor in Vancouver as a disembodied head visiting Chinatown and a compressed version that uses only 32 colors:

<img src="parrt-vancouver.jpg" width="50%"><img src="demon.png" width="50%">

(I like those demon eyes!)

Here is what my code looks like, once again using the magic `reassign_colors()` function I wrote:

```python
k=32
centroids, clusters = kmeans(X_, k=k, centroids='kmeans++', tolerance=.01)
centroids = centroids.astype(np.uint8)
reassign_colors(X, centroids)
img_ = Image.fromarray(X.reshape((h,w,3)))
img_.show()
```

## Advanced: Spectral clustering

In the introduction of machine learning, we discussed how to use random forests in an unsupervised way to get a similarity or distance metric from observation *i* to observation *j*. This information is not directly useful in k means because the means are not typically observations (they are the means of a cluster of them). That means we can't measure the distance of a point to a cluster. Instead, we can use spectral clustering which accepts a similarity matrix, does some linear algebra magic, and then clusters a transformed space using its kmeans. I used sklearn's built-in mechanism:

```python
S = similarity_matrix(X)
cluster = SpectralClustering(n_clusters=2, affinity='precomputed')
cluster.fit_predict(S) # pass similarity matrix not X
```

And then got a confusion matrix that improves upon the standard kmeans score for cancer data set.

```
       pred F  pred T
Truth                
F         198      14
T          39     318
clustering accur 0.9068541300527241
```

You are welcome to implement your own spectral clustering and then  you can use your own kmeans implementation.

### Breiman's RF for unsupervised learning trick

See [Breiman's website](https://www.stat.berkeley.edu/~breiman/RandomForests/cc_home.htm#prox) for the idea behind getting a proximity matrix from random forests. To save you the trouble of learning how sklearn implements random forests, here is a function that will get you all of the samples at the leaves reached by some input matrix X:

```python
def leaf_samples(rf, X:np.ndarray):
    """
    Return a list of arrays where each array is the set of X sample indexes
    residing in a single leaf of some tree in rf forest. For example, if there
    are 4 leaves (in one or multiple trees), we might return:

        array([array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
               array([10, 11, 12, 13, 14, 15]), array([16, 17, 18, 19, 20]),
               array([21, 22, 23, 24, 25, 26, 27, 28, 29]))
    """
    n_trees = len(rf.estimators_)
    leaf_samples = []
    leaf_ids = rf.apply(X)  # which leaf does each X_i go to for sole tree?
    for t in range(n_trees):
        # Group by id and return sample indexes
        uniq_ids = np.unique(leaf_ids[:,t])
        sample_idxs_in_leaves = [np.where(leaf_ids[:, t] == id)[0] for id in uniq_ids]
        leaf_samples.extend(sample_idxs_in_leaves)
    return leaf_samples
```

## Deliverables

1. You must provide `kmeans.py` in root directory of your repo. 
2. You must submit a notebook called `kmeans.ipynb` with the associated PDF generated from it to ease our grading, `kmeans.pdf`.

## Assessment

I believe I will have help with a grader, but reading your reports will take significantly longer than when I provide you some unit tests. Sorry in advance. Also, given the wide range of reports that you will submit, I will limit myself to one of three grades check minus, check, check plus, corresponding roughly to C, B, A.
