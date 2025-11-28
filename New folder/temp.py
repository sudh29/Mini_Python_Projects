import pandas as pd


def check_for_none_values(dataframe):
    """
    Check if any None (NaN) values are present in a Pandas DataFrame.

    Args:
        dataframe (pd.DataFrame): The DataFrame to check.

    Returns:
        bool: True if None (NaN) values are present, False otherwise.
    """
    return dataframe.isnull().values.any()


# Example usage
data = {"Column1": [1, 2, None, 4, 5], "Column2": ["a", "b", "c", None, "e"]}

df = pd.DataFrame(data)

if check_for_none_values(df):
    print("DataFrame contains None (NaN) values.")
else:
    print("DataFrame does not contain None (NaN) values.")
