from YoungFellah import youngfellah
from FileLoader import FileLoader
import os

fl = FileLoader()
data = fl.load(os.environ['CSV_PATH'])
print(youngfellah(data, 1992))
print(youngfellah(data, 2004))
print(youngfellah(data, 2010))
print(youngfellah(data, 2003))
print(youngfellah(data, 'bonsoir'))
print(youngfellah(data, None))
