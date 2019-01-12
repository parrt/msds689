# Isolation Forest Implementation

do in parallel 5%

select features rather than random feature 5%

Get cancer data into `cancer.csv`:

```python
from sklearn.datasets import load_breast_cancer
import pandas as pd

cancer = load_breast_cancer()
df = pd.DataFrame(data=cancer.data, columns=cancer.feature_names)
df.to_csv("cancer.csv", index=False)
```

Sample code

https://github.com/mgckind/iso_forest/blob/master/iso_forest.py