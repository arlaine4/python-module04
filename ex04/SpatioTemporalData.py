import pandas as pd


class SpatioTemporalData:
    def __init__(self, df):
        self.df = df

    def when(self, location):
        if not isinstance(location, str):
            return None
        tmp_df = self.df.filter(['Year', 'City'])[self.df.City == location]
        tmp_df.drop_duplicates(subset=['Year'], inplace=True)
        return list(tmp_df.Year.unique())

    def where(self, date):
        if not isinstance(date, int):
            return None
        tmp_df = self.df.filter(['Year', 'City'])[self.df.Year == date]
        tmp_df.drop_duplicates(subset=['City'], inplace=True)
        return list(tmp_df.City.unique())
