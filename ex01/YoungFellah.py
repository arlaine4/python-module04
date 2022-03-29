def youngfellah(df, year):
    dico = {'f': 'nan', 'm': 'nan'}
    dico['f'] = df.filter(['Year', 'Sex', 'Age'])[(df.Sex == 'F') & (df.Year == year)].min().Age
    dico['m'] = df.filter(['Year', 'Sex', 'Age'])[(df.Sex == 'M') & (df.Year == year)].min().Age
    return dico
