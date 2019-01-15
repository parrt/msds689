
class IsolationTreeEnsemble:
    def __init__(self, sample_size, n_trees=10):
        ...
        
    def fit(self, X, improved=False):
        if isinstance(X, pd.DataFrame):
            X = X.values
        ...
        return self

    def predict_from_anomaly_scores(self, scores, threshold):
        ...

    def predict(self, X, threshold):
        "Predict which are anomalous"
        ...

    def path_length(self, X):
        if isinstance(X, pd.DataFrame):
            X = X.values
        ...

    def anomaly_score(self, X):
        ...


class IsolationTree:
    def __init__(self, height_limit):
        ...

    def fit(self, X, improved=False):
        ...
        return self.root


class IsolationTree:
    def __init__(self, height_limit):
        ...

    def fit(self, X, improved=False):
        ...
        return self.root
