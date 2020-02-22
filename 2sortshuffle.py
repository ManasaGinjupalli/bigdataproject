unsorted = open("01.txt", "r")
sorted = open("02.txt", "w")

datalist = unsorted.readlines()
datalist.sort()

for line in datalist:
    print (line)
    sorted.write(line)

unsorted.close()
sorted.close()