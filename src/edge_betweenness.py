import sys
import networkx as nx


net_name=sys.argv[1]
G=nx.DiGraph()
G = nx.read_edgelist('dataset/'+net_name+'.csv', delimiter=',', nodetype=str,create_using=G)
print('edge betweenness...')
edge_betweenness=nx.edge_betweenness_centrality(G)
edge_betweenness_s=sorted(edge_betweenness.items(),key=lambda item:item[1],reverse=True)

f=open('centralities/'+net_name+'edge_betweenness.txt','w')

for item in edge_betweenness_s:
    f.write(item[0][0]+' '+item[0][1]+' '+str(item[1])+'\n')
f.close()
del edge_betweenness,edge_betweenness_s
