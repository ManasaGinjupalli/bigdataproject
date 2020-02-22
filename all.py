print ("hello, world!")
print ('hello, bearcat!')
print ('\n')

for x in range(0, 3):   # NOTE colon... whitespace matters; use spaces
    print ("Now x is %i" % (x))
    print ("Now x/3 is %.2f" % (x/3))
    
for x in range(0, 5):
    print ('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
   
for x in range(0, 5):
    print ("{0}\t{1}".format(x, x*x*x))

print ('\n')
#x = 1
#while True:
#    print ("Infinite loop. x is %i" % (x))
#    x += 1
print ('\n===========================\n')
 
s = '    Python programming    '
print (len(s))
print (len(s.strip()))
print (max(s))
print (s.count("p"))
print (s.lower().count("p"))
print (s.lower().replace("p","pw"))
print (s.lower().find("p"))
print (s.lower().find("z"))
print (s.lower().index("p"))
#print (s.lower().index("z"))

f = open("d.txt","r")  # open file, read-only
o = open("o.txt", "w") # open file, write
for line in f:  
    data = line.strip().split("    ") 
    print (data)
    print (len(data))
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print ("{0}\t{1}".format(store, cost))
        o.write("{0}\t{1}\n".format(store, cost))
f.close()
o.close()

with open("p.txt", "w") as myfile:
    myfile.write("Purchase Amount: {0}".format(5.32))
print ('\n===========================\n')

n = open("o.txt","r")  # open file, read-only
s = open("s.txt", "w") # open file, write
lines = n.readlines()
lines.sort()
print(lines)
for line in lines:
	s.write(line)
n.close()
s.close()
