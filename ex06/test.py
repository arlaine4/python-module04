from MyPlotLib import MyPlotLib
from FileLoader import FileLoader

fl = FileLoader()
df = fl.load('../athlete_events.csv')
mpl = MyPlotLib()
# mpl.histogram(df, [])
# mpl.histogram(df, ['Height'])
# mpl.histogram(df, ['Height', 'Weight'])
# mpl.histogram(df, ['Height', 'Weight', 'Age'])

# mpl.density(df, [])
# mpl.density(df, ['Height'])
# mpl.density(df, ['Height', 'Weight'])
# mpl.density(df, ['Height', 'Weight', 'Age'])

# mpl.pair_plot(df, [])
# mpl.pair_plot(df, ['Height'])
# mpl.pair_plot(df, ['Height', 'Weight'])
# mpl.pair_plot(df, ['Height', 'Weight', 'Age'])

# mpl.box_plot(df, [])
# mpl.box_plot(df, ['Height'])
# mpl.box_plot(df, ['Height', 'Weight'])
# mpl.box_plot(df, ['Height', 'Weight', 'Age'])
