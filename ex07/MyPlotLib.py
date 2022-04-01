import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import sys
import warnings
warnings.filterwarnings('ignore')


class MyPlotLib:
    @staticmethod
    def get_lines_cols(len_f):
        if len_f % 2 == 0:
            lines = len_f / 2
            cols = 2
        else:
            cols = len_f
            lines = 1
        return lines, cols

    @staticmethod
    def histogram(data, features):
        if not isinstance(features, list) or not isinstance(data, pd.DataFrame):
            return None
        if len(features) <= 1:
            sys.exit('Not enough features')
        fig = plt.figure(figsize=(len(features) + 10, len(features) + 5))
        lines, cols = MyPlotLib.get_lines_cols(len(features))
        for i, feature in enumerate(features):
            if feature not in data.columns:
                print(f'Found invalid feature name : {feature}')
                return None
            fig.add_subplot(lines, cols, i + 1)
            plt.hist(data[feature])
            plt.title(feature)
        plt.show()

    @staticmethod
    def density(data, features):
        if not isinstance(features, list) or not isinstance(data, pd.DataFrame):
            return None
        if len(features) <= 1:
            sys.exit('Not enough features')
        for i, feature in enumerate(features):
            if feature not in data.columns:
                print(f'Found invalid feature name {feature}')
                return None
            sns.distplot(np.array(data[feature]), hist=False, label=feature)
            plt.legend()
        plt.show()

    @staticmethod
    def pair_plot(data, features):
        if not isinstance(features, list) or not isinstance(data, pd.DataFrame):
            return None
        if len(features) <= 1:
            sys.exit('Not enough features')
        lst_features = [f for f in features if f in data.columns]
        if len(lst_features) != len(features):
            print('Invalid feature in feature list')
            return None
        df_features = data.filter([f for f in lst_features])
        sns.pairplot(df_features, diag_kind='hist')
        plt.show()

    @staticmethod
    def box_plot(data, features):
        if not isinstance(features, list) or not isinstance(data, pd.DataFrame):
            return None
        if len(features) <= 1:
            sys.exit('Not enough features')
        lst_features = [f for f in features if f in data.columns]
        if len(lst_features) != len(features):
            print('Invalid feature in feature list')
            return None
        df_features = data.filter([f for f in lst_features])
        df_features.dropna(inplace=True)
        fig, ax = plt.subplots()
        data = np.array(df_features)
        ax.boxplot(data)
        plt.xticks([i for i in range(1, len(features) + 1)], [feature for feature in features])
        plt.show()
