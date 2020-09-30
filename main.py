
from pandas_similarity import IndexCalculator
import pandas as pd


raw = [
    [1050, "Ixelles", 0, 340000],
    [1050, "Ixelles", 0, 340000]
]
df = pd.DataFrame(raw, columns=['postal_code', 'city', 'property_type', 'price'])


# Run the app
if __name__ == '__main__':
    index = IndexCalculator(df).get_index()
    print(index)
