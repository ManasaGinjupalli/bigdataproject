s = open("02.txt","r")
r = open("03.txt", "w")

thisKey = ""
thisValue = 0


for line in s:
  sum = line.strip().split('\t')
  title, authors = sum

  if title != thisKey:
    if title:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = title 
    thisValue = 0.0
  
  # apply the aggregation function
  thisValue += float(1)

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()