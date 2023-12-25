import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def create_dataframe(dataset) -> pd.DataFrame:
    return pd.read_csv(dataset)


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Function to handle missing, duplicate, and incorrect values in the dataset"""
    df.drop_duplicates(keep='first', inplace=True)  # drop duplicate rows
    df.dropna(inplace=True)                         # drop rows with missing values

    # Converting Rupee to USD for discounted prices
    df.discounted_price = df.discounted_price.replace("[₹,]", "", regex=True).astype(float)
    df.discounted_price = (df.discounted_price * .012).round(2)

    # Converting Rupee to USD for actual prices
    df.actual_price = df.actual_price.replace("[₹,]", "", regex=True).astype(float)
    df.actual_price = (df.actual_price * .012).round(2)

    # removing the trailing '%' and converting the value to float dtype
    df.discount_percentage = df.discount_percentage.str.rstrip("%").astype("float") / 100

    # replacing all '|' inputs with 0 and modify the dtype of rating as type float
    df.rating = df.rating.replace('[|]', '0', regex=True).astype(float)
    # removing all commas and modify the dtype of rating_count as type int
    df.rating_count = df.rating_count.replace('[,]', '', regex=True).astype(float)

    return df


def get_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Function to take a dataframe and return the summary statistics for numerical columns."""
    return df.describe()


def show_univariate_analysis(df: pd.DataFrame):
    """Function to show the analysis of individual variables using the seaborn library."""
    pass


def main():
    # Reading the dataset into a dataframe
    amazon_df = create_dataframe(r'.\amazon.csv')

    # cleaning the dataset
    clean_dataset(amazon_df)

    # print(amazon_df.info())


if __name__ == '__main__':
    main()