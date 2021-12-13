import bottle
import data
import json
import processing
import csv


@bottle.route('/')
def first() :
  return bottle.static_file('index.html', root=".")


@bottle.route('/js')
def jS() :
  return bottle.static_file('front.js', root=".")


@bottle.route("/bar")
def bar() :
  x = []
  y = []
  with open('data.csv') as f :
    reader = csv.reader(f)
    headers = next(f)
    for line in reader :
      if (line[1] not in x) :
        x.append(line[1])
        y.append(float(line[6]))
  object = [{
    "x" : x,
    "y" : y,
    "type":"bar"
  }]
  return json.dumps(object)


@bottle.route('/pie')
def pie() :
  sums = [0, 0, 0, 0]
  date = '2020-12-14T00:00:00.000' 
  with open('data.csv') as f :
    reader = csv.reader(f)
    headers = next(f)
    for line in reader :
      if (line[0] > date) :
        date = line[0]
  with open('data.csv') as f :
    reader = csv.reader(f)
    headers = next(f)
    for line in reader :
      if (line[0] == date) :
        sums[0] += int(line[2])
        sums[1] += int(line[3])
        sums[2] += int(line[4])
        sums[3] += int(line[5])
  object = [{
    "values" : [sums[0],sums[1],sums[2],sums[3]],
    "labels" : ["Janssen", "Moderna", "Pfizer", "Other"],
    "type":"pie"
  }]
  return json.dumps(object)


@bottle.post('/line')
def line() :
  content = bottle.request.body.read().decode()
  content = json.loads(content)
  with open('data.csv') as f :
    reader = csv.reader(f)
    headers = next(f)
    targetLis = []
    for line in reader :
      if (line[1] == content) :
        targetLis.append(line)
  targetLis.sort()
  x = []
  y = []
  for val in targetLis :
    x.append(val[0])
    y.append(float(val[6]))
  object = [{
    "x" : x,
    "y" : y,
    "type" : "scatter"
  }]
  return json.dumps(object)

import os.path

def load_data():
  csv_file = 'data.csv'
  if not os.path.isfile(csv_file):
    url = 'https://data.cdc.gov/resource/unsk-b7fc.json?$limit=50000&$where=location!=%27US%27'
    info = data.json_loader(url)
    heads = ['date','location','administered_janssen','administered_moderna','administered_pfizer', 'administered_unk_manuf','series_complete_pop_pct']
    data.save_data(heads, info, 'data.csv')

load_data()

bottle.run(host="0.0.0.0", port=8080, debug=True)