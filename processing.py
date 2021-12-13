
def init_dictionary(data, key) :
  newDict = {}
  for x in range(len(data)) :
    if key in data[x] :
      newDict[data[x].get(key)] = 0
  return newDict

def max_value(data,date):
  x = ''
  for i in data:
    if i[date] > x:
      x = i[date]
  return x

def sum_matches(data,key,value,key2):
  retval = 0
  for i in data:
    if i[key] == value:
      retval = retval + int(i[key2]) 
  return retval
    

def copy_matching(data,key,value):
  retval = []
  for i in data:
    if i[key] == value:
      retval.append(i)
  return retval
