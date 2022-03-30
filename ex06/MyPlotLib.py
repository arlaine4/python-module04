import matplotlib.pyplot as plt


class MyPlotLib:
    @staticmethod
    def histogram(df, features):
        lst_plots = []
        lst_titles = [f for f in features]
        lst_x_axis = []
        lst_y_axis = []
        for feature in features:
            if feature not in df.columns:
                return None
            df.dropna(subset=[feature], inplace=True)
            lst_plots.append(plt.hist(df[feature]))
        fig, ax = plt.subplots(len(features), 1, sharex=True)
        for i, feature in enumerate(features):
            ax.plot
            plt.title(lst_titles[i])
            plt.hist(df[feature])
        plt.show()
