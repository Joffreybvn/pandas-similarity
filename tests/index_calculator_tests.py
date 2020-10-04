
import unittest
import pandas as pd
from pandas_similarity import IndexCalculator


class IndexCalculatorTestCase(unittest.TestCase):

    def test_similarity_index(self):
        """Unit test for /v1/status"""

        # Define a dataframe
        df = pd.DataFrame([
            [1050, "Ixelles", 0, 360000],
            [1050, "Ixelles", 1, 340000]],
            columns=['postal_code', 'city', 'property_type', 'price'])

        index = IndexCalculator(df).get_index()

        # Check the status code and data
        self.assertEqual(index, 0.6667)


if __name__ == '__main__':
    unittest.main()
