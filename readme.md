# Instruction

********************************
The data is obtained from [SNAP](http://snap.stanford.edu/data/index.html),[KONECT](http://konect.uni-koblenz.de/networks/)  

1.The format of the data set is often not uniform, so preprocessing is required：  

- If the original file is txt, use /dataset/quick_process.py to get csv and txt with weights

- If the original file is gml, use Gephi to get the csv
   

2.Next, the network data set will be imported into FANMOD, depending on the network size, the running time will vary. Finally, you will get detailed network motif description, including type and Z-score value. The result is as follows：

<img src="..\pic\pic1.png" alt="drawing" width="400"/>

3.The motif with the largest z-score value is selected as the target motif, and the motif_computation function is called according to the calculation formula of the adjacency matrix of the motif. Because the time complexity of matrix calculation is very large, and the calculation efficiency of python is not as good as that of C and matlab, the calculation of the adjacency matrix of the motif of a larger network is run on matlab, using the weighing.m file. 

<img src="..\pic\pic2.png" alt="drawing" width="400"/>

4.The obtained directed graph based on the motif is calculated using the edge betweenness centrality algorithm.

5.Save the obtained centrality to the /centralities folder, and sort the edges or nodes according to the centrality value of the edges. 

6.Perform immune operations on the network and simulate in the SIR model, and call NDLib library functions. If it is an algorithm for connecting edges, use the drawCutEdge function, if it is an algorithm for a node, use the drawCutNode function. This operation is to make the algorithms for nodes and edges comparable.

7.The drawCutNode function and drawCutEdge function will save the data of the final state of the propagation in the trend_list, and then will save the data in the trend_list to the /output folder.

8.The calculations for other comparison algorithms, and the process is similar to 4, 5, 6, and 7. 

********************************

