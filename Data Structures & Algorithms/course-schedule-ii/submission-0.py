class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #toplogoical sort
        adj = defaultdict(list)
        indeg = [0] * numCourses

        # p -> c
        for c, p in prerequisites:
            adj[p].append(c)
            indeg[c]+=1

        #node and indegree # course and list of prereq
        queue = deque() # popleft() and then append()

        for n in range(numCourses):
            if n not in adj: 
                adj[n] = []
        
        print(adj)
        # get a queu and add starting nodex (indeg = 0)
        for n in range(len(indeg)):
            if indeg[n] == 0:
                queue.append(n)
         
        print(f"queue is {queue}")
        result = []

        while queue:
            popped = queue.popleft()
            result.append(popped)

            courses = adj[popped]

            for course in courses:
                indeg[course]-=1
                if indeg[course]== 0:
                    queue.append(course)
        
        if len(result) != numCourses:  #cycle
            return []
        
        return result