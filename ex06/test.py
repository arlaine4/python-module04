from MyPlotLib import MyPlotLib
from FileLoader import FileLoader

fl = FileLoader()
df = fl.load('../athlete_events.csv')
mpl = MyPlotLib()
mpl.histogram(df, ['Height', 'Weight'])
