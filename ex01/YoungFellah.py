def youngfellah(df, year):
    dico = {'f': 'nan', 'm': 'nan'}
    try:
        dico['f'] = df.filter(['Year', 'Sex', 'Age'])[(df.Sex == 'F') & (df.Year == year)].min().Age
        dico['m'] = df.filter(['Year', 'Sex', 'Age'])[(df.Sex == 'M') & (df.Year == year)].min().Age
    except KeyError:
        print('Columns Year, Sex or Age not present in dataframe, returning empty dict')
    return dico
