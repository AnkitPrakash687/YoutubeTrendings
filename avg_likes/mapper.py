i = open("purchases.txt", "r")
o = open("o.txt", "w")

for line in i:
  data = line.strip().split('    ')
  if (len(data) == 6):
    date, time, store, item, cost, payment = data
    o.write(store + "\t" + cost+ "\n")

i.close()
o.close()
