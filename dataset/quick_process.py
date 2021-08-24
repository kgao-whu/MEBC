import sys
name=sys.argv[1]

file=open(name+'.txt')
output1=open(name+'.csv','w')
output2=open(name+'-weight.txt','w')
for line in file:
    split=line.split()
    output1.write(split[0]+','+split[1]+'\n')
    output2.write(split[0]+' '+split[1]+' 1\n')
file.close()
output1.close()
output2.close()
