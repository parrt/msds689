from sklearn.datasets import load_breast_cancer
import pandas as pd

cancer = load_breast_cancer()
df = pd.DataFrame(data=cancer.data, columns=cancer.feature_names)
df['diagnosis'] = cancer.target
df.loc[df.diagnosis==0,'diagnosis'] = -1
df.loc[df.diagnosis==1,'diagnosis'] = 0
df.loc[df.diagnosis==-1,'diagnosis'] = 1
df.to_csv("cancer.csv", index=False)
