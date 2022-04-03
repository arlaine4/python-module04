from FileLoader import FileLoader

fl = FileLoader()
data = fl.load('../athlete_events.csv')
fl.display(data, 12)
# fl.display(data, -12)
# fl.display(data, 0)
# fl.display(data, 'bonsoir')
# fl.display(data, None)
