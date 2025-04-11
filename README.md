<H1>1 Heuristics</H1>
<H2>1 Cristofides algorithm</H2>
This algorithm works in 6 steps: <br/>
1. Create a minimal spaning tree for all the nodes. <br/>
![image](https://github.com/user-attachments/assets/be8dde0a-d11f-4b92-8afb-0042285ce510)
2. Isolate nodes with a odd amount of connections
3. Connect all nodes in pairs and find a minimum length for the connections. <br/>
![image](https://github.com/user-attachments/assets/d30e13bb-149d-4b00-a458-60482f861b63)
4. Combine the connections from step 1 and 3 into a multigraph. (this means that some nodes can have multiple connections to the same node) <br/>
![image](https://github.com/user-attachments/assets/b65de972-c42f-4668-b5db-3670b7d0cb2b)

5. Generate Eulerian tour of the multigraph
6. Generate TSP from Eulerian tour (follow the Euleriantour and if you reach a already visited node skip it) <br/>
![image](https://github.com/user-attachments/assets/fcff6bb3-615c-4a38-9a95-1228739134c0)

<H2>1 Greedy heuristic</H2>
//todo <br/>

<H1>2 Optimizations</H1>
<H2>1 random swapping</H2>
//todo <br/>
<H2>2 k-opt improvement</H2>
//todo <br/>
<H2>2 simulated annealing</H2>
//todo <br/>
