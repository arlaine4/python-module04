import pandas as pd


def howManyMedalsByCountry(df, c_name):
    if not isinstance(df, pd.DataFrame) or not isinstance(c_name, str):
        return None
    if 'Team' not in df.columns or 'Sex' not in df.columns or 'Medal' not in df.columns:
        return None
    infos = df.filter(['Team', 'Sport', 'Name', 'Medal', 'Year'])[df.Team == c_name]
    infos.dropna(subset=['Medal'], inplace=True)
    infos.Medal = infos.Medal.map(lambda n: n[0])
    dic = {year: None for year in infos.Year.unique()}
    for y in dic.keys():
        info = infos[infos.Year == y]
        info = info.drop_duplicates(subset=['Name', 'Medal', 'Sport'])
        medals_count = info.Medal.to_list()
        dic[y] = {'G': medals_count.count('G'),
                  'S': medals_count.count('S'),
                  'B': medals_count.count('B')}
    return dic
