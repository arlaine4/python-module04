from FileLoader import FileLoader
from SpatioTemporalData import SpatioTemporalData
import os

fl = FileLoader()
data = fl.load(os.environ['CSV_PATH'])
sp = SpatioTemporalData(data)
print(sp.where(2000))
print(sp.where(1980))
print(sp.when('London'))
print(sp.when('Athina'))
print(sp.when('Paris'))
print(sp.when('ah bon'))
print(sp.where(0))
