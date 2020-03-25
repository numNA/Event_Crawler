import csv

def save_to_file(events):
  file = open("events.csv",mode ="w",encoding = 'utf-8' )
  writer = csv.writer(file)
  writer.writerow(["place","title", "period", "price", "url"])
  for event in events:
    writer.writerow(list(event.values()))
  return