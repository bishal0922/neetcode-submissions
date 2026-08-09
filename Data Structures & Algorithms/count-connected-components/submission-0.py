class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # initialize a parent array
        parent = [i for i in range(n)]
        # rank array (rank is count of people in it)
        rank = [1] * n
        

        # union find

        # find 
        def find(node):
            curr = node

            # while node is its own parent
            while curr != parent[curr]:
                parent[curr] = parent[parent[curr]]
                curr = parent[curr]

            return curr

        # union
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2: return False

            # if the parent
            # parent of n1 > parent of n2:
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1]+=rank[p2]
            else:
                #rank of p2 is greater
                parent[p1] = p2
                rank[p2] += rank[p1]
        
            return True

        # iterate through all the edges
        #     union find on the edges
        #     res-=1
        
        result= n
        for u,v in edges:
            if union(u,v):
                result-=1
        
        return result




        