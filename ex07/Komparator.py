import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


class Komparator:
    def __init__(self, df):
        self.df = df

    def density(self, categorical_var, numerical_var):
        if not isinstance(categorical_var, str) or not isinstance(numerical_var, str):
            return None
        if categorical_var not in self.df.columns or numerical_var not in self.df.columns:
            print(f'{categorical_var} or {numerical_var} not in df')
        df = self.df.filter([numerical_var, categorical_var])
        df.dropna(subset=[numerical_var, categorical_var], inplace=True)
        fig = plt.figure(figsize=(12, 12))
        single_values = list(df[categorical_var].unique())
        for value in single_values:
            sns.distplot(np.array(df.filter([numerical_var])[df[categorical_var] == value]), hist=False, label=value)
        plt.legend()
        plt.show()


    def compare_histograms(self, categorical_var, numerical_var):
        if not isinstance(categorical_var, str) or not isinstance(numerical_var, str):
            return None
        if categorical_var not in self.df.columns or numerical_var not in self.df.columns:
            print(f'{categorical_var} or {numerical_var} not in df')
            return None
        df = self.df.filter([numerical_var, categorical_var])
        df.dropna(subset=[numerical_var, categorical_var], inplace=True)
        fig = plt.figure(figsize=(12, 12))
        sns.histplot(data=df, x=numerical_var, hue=categorical_var, multiple='stack') 
        plt.show()
        """print(single_values)
        single_values = list(df[categorical_var].unique())
        x_values = [df[df[categorical_var] == value] for value in single_values]
        print(df.Weight.shape, len(x_values[0]))
        print(x_values)
        plt.hist(x=x_values, y=df[numerical_var], labels=single_values)"""
        """print(df.head())
        for new_col in single_values:
            df = df.insert(loc=1, column=new_col, value=np.array(df[df[categorical_var] == new_col]))
        print(df.head())"""
        #sns.histplot(data=df, x=numerical_var, hue=categorical_var, alpha=0.3)
        #plt.title(f'{categorical_var} over {numerical_var}')
        #plt.show()
