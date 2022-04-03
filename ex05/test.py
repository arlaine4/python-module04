from FileLoader import FileLoader
from HowManyMedalsByCountry import howManyMedalsByCountry
import os

fl = FileLoader()
data = fl.load(os.environ['CSV_PATH'])
print(howManyMedalsByCountry(data, 'France'), end='\n\n')
print(howManyMedalsByCountry(data, 'okay'), end='\n\n')
print(howManyMedalsByCountry(data, 1), end='\n\n')
print(howManyMedalsByCountry(data, ''), end='\n\n')
