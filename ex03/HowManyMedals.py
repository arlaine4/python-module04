from copy import deepcopy


def howManyMedals(df, name):
    infos = df.filter(['Name', 'Medal', 'Year'])[(df.Name == name)]
    infos.dropna(inplace=True)
    infos.drop('Name', axis=1, inplace=True)
    infos.Medal = infos.Medal.map(lambda name: name[0])
    #infos = infos.set_index('Year')
    sub_dict = {'G': 0, 'S': 0, 'B': 0}
    dic = {}
    # BORDEL BELOW
    for y in infos.Year.unique():
        dic[y] = sub_dict
        dic[y] = infos[infos.Year == y].Medal.to_list()
        print(infos[infos.Year == y].value_counts())
    print(infos)
    print(dic)