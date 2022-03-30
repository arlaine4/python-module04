from FileLoader import FileLoader
from HowManyMedalsByCountry import howManyMedalsByCountry

fl = FileLoader()
data = fl.load('../athlete_events.csv')
print(howManyMedalsByCountry(data, 'France'))
print(howManyMedalsByCountry(data, 'okay'))
print(howManyMedalsByCountry(data, 1))
print(howManyMedalsByCountry(data, ''))
