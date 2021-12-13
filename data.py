import csv
import json
import urllib.request

def json_loader(string):
  response = urllib.request.urlopen(string)
  content = response.read().decode()
  jsonblob = json.loads(content)
  return jsonblob

def make_values_numeric(keys, dic) :
  for key in keys :
    dic[key] = float(dic[key])
  return dic



def save_data(strList, dicts, filename) :
  with open(filename, 'w') as f :
    writer = csv.writer(f)
    writer.writerow(strList)
    for dict in dicts :
      tempList = []
      for key in strList :
        tempList.append(dict[key])
      writer.writerow(tempList)

def load_data(filename) :
  retVal = []
  with open(filename) as f :
    reader = csv.reader(f)
    headers = next(reader)
    for line in reader :
      tempDict = {}
      count = 0
      for key in headers :
        tempDict[key] = line[count]
        count += 1
      retVal.append(tempDict)
  return retVal

def dic_list_gen(string,list):
  acc = []
  for values in range(len(list)):
    acctwo = {}
    for elements in range(len(list[values])):
      acctwo[string[elements]] = list[values][elements]
    acc.append(acctwo)
  return acc

def read_values(fname):
  lst = []
  with open(fname) as f:
    reader = csv.reader(f)
    header = next(reader)
    for i in reader:
      lst.append(i)
  return list(lst)

def make_lists(keys,dic):
  lst = []
  for d in dic:
    sublst = []
    for s in keys:
      sublst.append((d[s]))
    lst.append(sublst)
  return lst

def write_values(fname,lst):
  with open(fname, 'a') as f:
    writer = csv.writer(f)
    for i in lst:
      writer.writerow(i)
  return None

