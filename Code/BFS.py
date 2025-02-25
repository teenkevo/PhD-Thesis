# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## BREADTH FIRST SEARCH ALGORITHM
# %% [markdown]
# ### Vertex Class

# %%
# Definition of the vertex class with 4 instance variables and 1 function
class Vertex:

	# Constructor taking the Name argument n
	def __init__(self, n):

		# Assign the n argument to self.name              
		self.name = n

		# An empty list is also setup for the neighbours
		self.neighbors = list()         
		
		# Set and initialize the distance to a high number
		self.distance = 9999

		# Initialize the color to black (unvisited)            
		self.color = 'black'           
	
	# add_neighbor function which takes v(vertex letter name)
	def add_neighbor(self, v):

		# if that vertex is not already in self-vertex's neighbors
		if v not in self.neighbors:

			# add it to the neighbours list     
			self.neighbors.append(v) 

			# and sort the list (store the neighbours as a sorted list)   
			self.neighbors.sort()       

# %% [markdown]
# ### Graph Class

# %%
# Definition of the graph class with an empty vertices dictionary and 4 functions
class Graph:
    vertices = {}  
	
    # Create a function that adds a vertex, it takes a vertex object
	def add_vertex(self, vertex):

        #First check if the vertex variable passed in is actually a 
        # vertex object ANDCheck if it is not already in vertices the 
        # dictionary
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            # Add the vertex to the vertices dictionary and return True, 
            # otherwise, False 
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False
	
    # Create a function that adds an edge, by passing in 
    # the letter name of the vertices u and v at either end of that edge
	def add_edge(self, u, v):

        # First check if the both vertices u and v are valid vertices 
        # in the graph: IF TRUE,
		if u in self.vertices and v in self.vertices:

            # Iterate through the keys:value pairs in the vertices dictionary
			for key, value in self.vertices.items():

                # Find the vertex at either end of the edge, THEN
                # add the other vertex at the other end of the edge as 
                # its neighbour and return True after adding the edge. 
                # Otherwise, return False
				if key == u:
					value.add_neighbor(v)
				if key == v:
					value.add_neighbor(u)
			return True
		else:
			return False

    # Create a function to print the graph		
	def print_graph(self):

        # Iterate through the vertices AND for each key
		for key in sorted(list(self.vertices.keys())):

            # print out the key, name of the vertex and a list 
            # of all of its neighbours 
			print(key + 
                str(self.vertices[key].neighbors) + 
                "  " + 
                str(self.vertices[key].distance))

    # Create a function to execute the Breadth First Search, 
    # it needs a starting point. 
    # It takes a vertex object (vert) as a starting point	
	def bfs(self, vert):

        # Create an empty queue that BFS will use to process the vertices
		q = list()

        # Set the starting point vertex distance to 0, 
        # since the distance from any vertex to itself is 0
		vert.distance = 0

        # Set the starting point vertex color to red, 
        # since that is the starting point and it is already being visited
		vert.color = 'red'

        # Loop through each of the starting point's neighbours
		for v in vert.neighbors:

            # Set their distances from the starting point vertex to 1
			self.vertices[v].distance = vert.distance + 1

            # Append those neighbours to the queue
			q.append(v)
		
        # As long as there is still items on the queue,
		while len(q) > 0:

            # pop them off one by one
			u = q.pop(0)

            # Since u is just the letter name of the vertex, we want 
            # to get the vertex object so we assign the vertex 
            # object(self.vertices[u]) to node_u
			node_u = self.vertices[u]

            # and then set node_u's color to red since we are going to 
            # visit that vertex
			node_u.color = 'red'
			
            # Iterate through node_u's neightbours and for each vertex 
            # v in its neigbours, 
			for v in node_u.neighbors:

                # first get the vertex object self.vertices[v] since 
                # v only gives us the letter name assign that object to 
                # the node_v variable
				node_v = self.vertices[v]

                # Check if node_v's neighbours have not been visited 
                # yet (colored black), IF TRUE,
				if node_v.color == 'black':

                    # append that neighbour vertex to the queue
					q.append(v)

                    # Check if that neighbour's distance is greater 
                    # that 1 more of node_u's distance from the source. IF TRUE,
					if node_v.distance > node_u.distance + 1:

                        # Then update node_v's distance to node_u's distance + 1
						node_v.distance = node_u.distance + 1

# %% [markdown]
# #### Create a Graph object

# %%
g = Graph()

# %% [markdown]
# #### Add vertices to the graph

# %%
# OPTION 1
# Let a be a vertec object with a letter name 'A'
a = Vertex('A')

# and then add the vertex to the graph
g.add_vertex(a)

# OPTION 2
# Using a for loop to create vertices
# For all letters in range A through K (this will look at A upto J)
for i in range(ord('A'), ord('K')):

    # one by one, add vertex with that letter name to the graph
	g.add_vertex(Vertex(chr(i)))

# %% [markdown]
# #### Add edges to the graph

# %%
# Create a list of edge names
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']

#loop through the edges in the edges list
for edge in edges:

    # add the edge using the first letter and the second letter
    # one by one, all the edges will be added into the neighbours list 
    # for each of our the vertices
	g.add_edge(edge[:1], edge[1:])

# %% [markdown]
# #### Call the Breadth First Search function, assign a starting point and print graph 

# %%
# Assign a starting point (here it is vertex --> a)
g.bfs(a)

#Print the graph
g.print_graph()


