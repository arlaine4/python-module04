import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import warnings
import sys
warnings.filterwarnings('ignore')


class Komparator:
    def __init__(self, df):
        if df is None:
            sys.exit('Invalid DataFrame')
        self.df = df

    def density(self, categorical_var, numerical_var):
        if not isinstance(categorical_var, str) or not isinstance(numerical_var, str):
            print(f'Error in args for {categorical_var} or {numerical_var}')
            return None
        if categorical_var not in self.df.columns or numerical_var not in self.df.columns:
            print(f'{categorical_var} or {numerical_var} not in df')
        df = self.df.filter([numerical_var, categorical_var])
        df.dropna(subset=[numerical_var, categorical_var], inplace=True)
        fig = plt.figure(figsize=(12, 12))
        single_values = list(df[categorical_var].unique())
        for value in single_values:
            sns.distplot(np.array(df.filter([numerical_var])[df[categorical_var] == value]),
                         hist=False, label=value)
        plt.legend()
        plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        if not isinstance(categorical_var, str) or not isinstance(numerical_var, str):
            print(f'Error in args for {categorical_var} or {numerical_var}')
            return None
        if categorical_var not in self.df.columns or numerical_var not in self.df.columns:
            print(f'{categorical_var} or {numerical_var} not in df')
            return None
        df = self.df.filter([numerical_var, categorical_var])
        df.dropna(subset=[numerical_var, categorical_var], inplace=True)
        fig = plt.figure(figsize=(12, 12))
        single_values = list(df[categorical_var].unique())
        for value in single_values:
            plt.hist(np.array(df.filter([numerical_var])[df[categorical_var] == value]),
                     alpha=0.3, label=value)
        plt.xlabel(numerical_var)
        plt.title(f'{categorical_var} over {numerical_var}')
        plt.legend()
        plt.show()

    def compare_box_plots(self, categorical_var, numerical_var):
        if not isinstance(categorical_var, str) or not isinstance(numerical_var, str):
            print(f'Error in args for {categorical_var} or {numerical_var}')
            return None
        if categorical_var not in self.df.columns or numerical_var not in self.df.columns:
            print(f'{categorical_var} or {numerical_var} not in df')
            return None
        df = self.df.filter([numerical_var, categorical_var])
        df.dropna(subset=[categorical_var, numerical_var], inplace=True)
        ax = df.boxplot(by=categorical_var,
                        flierprops={'markerfacecolor': 'orange', 'marker': 'o'})
        ax.set_xlabel(categorical_var)
        plt.show()

