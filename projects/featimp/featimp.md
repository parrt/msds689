# Feature importance and selection

The goal of this project is to get a much stronger understanding of the various feature importance algorithms and how to select features in a model. As with your second project, this project is very loosely defined and you must generate a report summarizing your techniques and explorations in a notebook you would be proud to send a potential employer.

You will work under `featimp-`*userid* repo and create a support file called `featimp.py` that you can import that file into your notebook using the following from one of the cells:

```
%run featimp
```

That way you can keep big chunks of functions out of your notebook and the notebook can be primarily about explanations and visualizations. (You can link to the code from the notebook of course.)

## Importance strategies working directly from the data

The simplest technique to identify important regression features is to rank them by their Spearman's rank correlation coefficient; the feature with the largest coefficient is taken to be the most important. This method is measuring *irrelevance importance* and works well for independent features, but suffers in the presence of codependent features.   Groups of features with similar relationships to the response variable receive the same or similar ranks, even though just one should be considered important.

Another possibility is to use principle component analysis (PCA), which operates on just the X explanatory matrix. PCA transforms data into a new space characterized by eigenvectors and identifies features that explain the most variance in the new space. If the first principal component covers a large percentage of the variance, the "loads" associated with that component can indicate importance of features in the original X space.

In an effort to deal with codependencies, data analysis techniques rank features not just by *relevance* (correlation with the response variable) but also by low *redundancy*, the amount of information shared between codependent features, which is the idea behind minimal-redundancy-maximal-relevance (mRMR):

<img src="mRMR.png" width="300">
 
## Model-based importance strategies

 permutation importance
 drop column importance

## Comparing strategies

 Because we as humans cannot simply look at the data and decide which features are most important, we often just rely on testing how well the recommended features work for a variety of models. For example, given a feature ranking, we can train OLS, RF, and XGBoost models on the top *k=1..p* features to see how good those features are.  For example, on the bulldozer data set for a new technique I'm working on, I generate a graph that looks like this:
 
<img src="bulldozer-topk-spearman.png" width="200">

That compares Spearman's rank coefficient, PCA, and linear regression.

You should also add compare to [shap](https://github.com/slundberg/shap) to your comparisons to see how well the techniques you implement do in relation to shap.

You can make a different graph for top-*k* as tested with OLS, RF, and XGBoost. It's often the case that features determined for one model do not export well to other models.
 
## Automatic feature selection algorithm

Once you have an ordering of features from most to least important, we need a mechanism to drop off unimportant features and keep the top *k*, for some *k* we don't know beforehand. Implement an automated mechanism that selects the top *k* features automatically that gives the best validation error. In other words, get a baseline validation metric appropriate for a classifier or a regressor then get the feature importances. Dropped the lowest importance feature and retrain the model and re-computing the validation metric. If the validation metric is worse, then we have dropped one too many features. Because of codependencies between features, you must recompute the feature importances after dropping each feature.

In your report, you should make it clear how the algorithm works and the results. That means you will have to come up with a way to visualize or describe the results.

## Deliverables

1. File `featimp.py` in the root directory of your repository.
2. Notebook called `featimp.ipynb` and associated PDF generated from it called `featimp.pdf`.

## Assessment

I believe I will have help with a grader, but reading your reports will take significantly longer than when I provide you some unit tests. Sorry in advance. Also, given the wide range of reports that you will submit, I will limit myself to one of three grades check minus, check, check plus, corresponding roughly to C, B, A.

You should also think about explaining how all of your algorithms work, including how you identify which cluster appoints should be associated with which true labels. Talk about any additions you've done and other tests. Ask yourself what you don't know and what you'd like to learn at the start of this project. Then those are good questions to ask and answer in your report notebook. Try to create something that you will be proud to show potential employers.