class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #dfs problem where if we visited the same node that we already visited then it is a problem
        # get a graph (node -> [connected nodes])
        adj = defaultdict(list)
        for a, b in edges: 
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        #dfs 
        def valid(node, parent):
            
            if node in visited: return False #we already visited cannot be a tree

            visited.add(node) # we 'visited it'

            #search through its next nodes and then dfs on them
            for next_nodes in adj[node]:
                #we visite the parent
                if next_nodes == parent:
                    continue
                if not valid(next_nodes, node):
                    return False

            return True
        

        if not valid(0, -1):
            return False
        
        return len(visited) == n



