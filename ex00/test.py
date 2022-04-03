from FileLoader import FileLoader
import os

fl = FileLoader()
data = fl.load(os.environ['CSV_PATH'])
fl.display(data, 12)
# fl.display(data, -12)
# fl.display(data, 0)
# fl.display(data, 'bonsoir')
# fl.display(data, None)
