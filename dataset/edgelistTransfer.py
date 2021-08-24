import sys
name=sys.argv[1]

file=open(name+'.txt')
output1=open(name+'.csv','w')
output2=open(name+'-weight.txt','w')
for line in file:
    split=line.split()
    for i in range(len(split)-1):
        output1.write(split[0]+','+split[i+1]+'\n')
        output2.write(split[0]+' '+split[i+1]+' 1\n')

file.close()
output1.close()
output2.close()
