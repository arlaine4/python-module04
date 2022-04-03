from FileLoader import FileLoader
from HowManyMedals import howManyMedals
import os

fl = FileLoader()
df = fl.load(os.environ['CSV_PATH'])
print(howManyMedals(df, 'Kjetil Andr Aamodt'))
print(howManyMedals(df, 'Gary Abraham'))
print(howManyMedals(df, 'Yekaterina Konstantinovna Abramova'))
print(howManyMedals(df, 'Kristin Otto'))
