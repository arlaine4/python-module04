from Komparator import *
from FileLoader import *
import os

fl = FileLoader()
df = fl.load(os.environ['CSV_PATH'])
k = Komparator(df)
# k.compare_box_plots('Medal', 1)
# k.compare_box_plots('Medal', 'Age')
k.compare_histograms('Medal', 'Height')
k.density('Medal', 'Weight')
