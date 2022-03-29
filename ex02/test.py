from FileLoader import FileLoader
from ProportionBySport import proportionBySport

fl = FileLoader()
data = fl.load('../athlete_events.csv')
print('For 2004, Tennis and F:', end='\n')
print(proportionBySport(data, 2004, 'Tennis', 'F'), end="\n\n")
print('For 2008, Hockey and F:', end='\n')
print(proportionBySport(data, 2008, 'Hockey', 'F'), end="\n\n")
print('For 1964, Biathlon and M:', end='\n')
print(proportionBySport(data, 1964, 'Biathlon', 'M'), end="\n\n")
