s = open("02.txt","r")
r = open("03.txt", "w")

thisKey = ""
thisValue = 0


for line in s:
  sum = line.strip().split('\t')
  author, average_rating = sum

  if author != thisKey:
    if author:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = author 
    thisValue = 0.0
  
  # apply the aggregation function
  thisValue += float(1)

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()
