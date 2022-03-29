import pandas as pd


class FileLoader:

    @staticmethod
    def load(path, sep=','):
        try:
            df = pd.read_csv(path, sep=sep)
        except FileNotFoundError:
            print(f"Invalid file {path}")
            return
        print(f'Loading dataset of dimensions {df.shape[0]} x {df.shape[1]}')
        return df

    @staticmethod
    def display(df, n):
        if type(n) is not int or not isinstance(df, pd.DataFrame):
            print('Error')
            return
        try:
            if 0 > n >= (df.shape[0] * - 1) - n:
                print(df.tail(abs(n)))
            elif 0 <= n <= df.shape[0]:
                print(df.head(n))
        except:
            print("Error in dataset")
