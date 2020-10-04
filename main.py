
from pandas_similarity import IndexCalculator
import pandas as pd

# Usage example
df = pd.DataFrame([
    [1050, "Ixelles", 0, 360000],
    [1050, "Ixelles", 1, 340000]],
    columns=['postal_code', 'city', 'property_type', 'price'])


# Run the app
if __name__ == '__main__':
    index = IndexCalculator(df).get_index()
    print(index)
