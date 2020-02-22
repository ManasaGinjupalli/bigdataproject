i = open("purchases.txt", "r")
c = open("c.txt", "w")


for line in i:
  data = line.strip().split('    ')
  if (len(data) == 6):
    date, time, store, item, cost, payment = data
    c.write(store + "," + cost+ "\n")

i.close()
c.close()


