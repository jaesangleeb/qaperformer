import pandas as pd
from collections import defaultdict


#1 Null 값을 찾아야함

class QAPerformer:

    def __init__(self, df, anchor=None):
        """
        :param df: Input DataFrame
        :param anchor: Anchor value for rolling. e.g. ord_date | ord_ymd | ord_dt
        """
        self.df = df
        self.anchor = anchor

    def null_counter(self, how: str = 'all', cols: list = None) -> pd.DataFrame:
        """
        :param how: You should input 'all' or 'specify'
        :param cols: If you pass 'specify' you should specify columns in list type
        :return: Extract report with type of dataframe contains counts of null values, ratio of null values
        """
        if how == 'all':
            df = self.df

        if how == 'specify':
            if isinstance(cols, list):
                raise ValueError(
                    'if you pass parameter how=\'specify\',you should pass parameter [cols] as type of list')

            df = self.df[[i for i in cols]]

        return pd.DataFrame(data={"N/A": df.isnull().sum(),
                                  "Ratio": df.isnull().sum() / df.shape[0]}).T

    def cartesian_counter(self, how='all', cols: list = None) -> pd.DataFrame:
        """
        :param how: You should input 'all' or 'specify'
        :param cols: If you pass 'specify' you should specify columns in list type
        :return: Extract report with type of dataframe contains counts of null values, ratio of duplicated values
        """

        if how == 'all':
            df = self.df

        if how == 'specify':
            if isinstance(cols, list):
                raise ValueError(
                    'if you pass parameter how=\'specify\',you should pass parameter [cols] as type of list')

            df = self.df[[i for i in cols]]

        dic = defaultdict(int)

        for i in list(df.columns):
            result = [df[df[i].duplicated()][i].nunique(), df[df[i].duplicated()][i].nunique() / df.shape[0]]
            dic[f"{i}"] = result

        return pd.DataFrame(data=dic, index=["Dups", "Ratio"])



