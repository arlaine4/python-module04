class SpatioTemporalData:
    def __init__(self, df):
        self.df = df

    def when(self, location):
        if not isinstance(location, str):
            return None
        try:
            tmp_df = self.df.filter(['Year', 'City'])[self.df.City == location]
        except KeyError:
            print('Year or City not df columns')
            return None
        tmp_df.drop_duplicates(subset=['Year'], inplace=True)
        return list(tmp_df.Year.unique())

    def where(self, date):
        if not isinstance(date, int):
            return None
        try:
            tmp_df = self.df.filter(['Year', 'City'])[self.df.Year == date]
        except KeyError:
            print('Year or City not in df columns')
            return None
        tmp_df.drop_duplicates(subset=['City'], inplace=True)
        return list(tmp_df.City.unique())
