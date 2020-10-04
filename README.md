# Pandas Similarity

[![Generic badge](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue)](https://www.python.org/downloads/release/python-380/)

Pandas similarity is a small library that count and return a similarity index between the entries of a dataframe.

This index can be used to remove very similar observations in a Dataframe. This is useful when you have Dataset coming from different sources about the same subject.

### Installing
Install and update using pip:

```Shell
pip install pandas-similarity
```

### A simple example

*IndexCalculator* return a **normalized index between 0 and 1**.

```Python
import pandas as pd
from pandas_similarity import IndexCalculator

# Create a Pandas Dataframe.
df = pd.DataFrame([
    [1050, "Ixelles", 0, 360000],
    [1050, "Ixelles", 1, 340000]],
    columns=['postal_code', 'city', 'property_type', 'price'])

# Print the index of similarity between all entries of the dataframe.
print(IndexCalculator(df).get_index())

# Index: 0.6667
```

In this example, we have a Dataframe with two observations, where *price* and *property_type* are different. The similarity index returned by *IndexCalculator* is *0.667*.

## About the author
Author: [Joffrey Bienvenu](https://github.com/Joffreybvn), Junior developper & ML student @ [Becode](https://becode.org/).