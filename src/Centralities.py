#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 03:35:15 2018

@author: gaokuang
"""

import sys
import networkx as nx
import os


net_name=sys.argv[1]
G=nx.DiGraph()
G = nx.read_edgelist('../dataset/'+net_name+'.csv', delimiter=',', nodetype=str,create_using=G)
print('degree...')
degree=nx.degree_centrality(G)
degree_s=sorted(degree.items(),key=lambda item:item[1],reverse=True)
f=open('../centralities/'+net_name+'degree.txt','w')
for item in degree_s:
    f.write(item[0]+',')
f.close()
del degree,degree_s

print('closeness...')
closeness=nx.closeness_centrality(G)
closeness_s=sorted(closeness.items(),key=lambda item:item[1],reverse=True)
f=open('../centralities/'+net_name+'closeness.txt','w')
for item in closeness_s:
    f.write(item[0]+',')
f.close()
del closeness,closeness_s

print('betweenness...')
betweenness=nx.betweenness_centrality(G)
betweenness_s=sorted(betweenness.items(),key=lambda item:item[1],reverse=True)
f=open('../centralities/'+net_name+'betweenness.txt','w')
for item in betweenness_s:
    f.write(item[0]+',')
f.close()
del betweenness,betweenness_s


