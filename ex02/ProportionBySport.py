def proportionBySport(df, year, sport, gender):
    subdf_all = df.filter(['Sport', 'Sex', 'Name', 'Year'])[(df.Year == year) & (df.Sex == gender)]
    subdf_sport = subdf_all[(subdf_all.Sport == sport)]
    subdf_sport = subdf_sport.drop_duplicates(subset=['Name'])
    subdf_all = subdf_all.drop_duplicates(subset=['Name'])
    return subdf_sport.shape[0] / subdf_all.shape[0]

