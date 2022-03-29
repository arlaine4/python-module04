from YoungFellah import youngfellah
from FileLoader import FileLoader

fl = FileLoader()
data = fl.load('../athlete_events.csv')
test1 = youngfellah(data, 2004)
print(test1)
test2 = youngfellah(data, 1991)
print(test2)
