from Komparator import *
from FileLoader import *

fl = FileLoader()
df = fl.load('athlete_events.csv')
k = Komparator(df)
# k.compare_histograms('Medal', 'Weight')
# k.density('Medal', 'Height')
k.compare_box_plots('Sex', 'Height')
