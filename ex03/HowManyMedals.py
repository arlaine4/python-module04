from copy import deepcopy
import pandas as pd


def howManyMedals(df, name):
    if not isinstance(df, pd.DataFrame) or not isinstance(name, str):
        return None
    if 'Name' not in df.columns or 'Sex' not in df.columns or 'Medal' not in df.columns:
        return None
    infos = df.filter(['Name', 'Medal', 'Year'])[(df.Name == name)]
    infos.dropna(inplace=True)
    infos.drop('Name', axis=1, inplace=True)
    infos.Medal = infos.Medal.map(lambda n: n[0])
    dic = {year: None for year in infos.Year.unique()}
    for y in dic.keys():
        medals_count = infos[infos.Year == y].Medal.to_list()
        dic[y] = {'G': medals_count.count('G'),
                  'S': medals_count.count('S'),
                  'B': medals_count.count('B')}
    return dic
