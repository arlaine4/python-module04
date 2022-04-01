import matplotlib.pyplot as plt


class MyPlotLib:
    @staticmethod
    def histogram(df, features):
        for feature in features:
            if feature not in df.columns:
                return None