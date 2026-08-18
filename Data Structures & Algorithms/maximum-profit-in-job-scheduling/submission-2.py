class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        jobs = sorted(zip(startTime, endTime, profit))
        n = len(jobs)
        cache = {}

        def dfs(i):
            if i == n:
                return 0

            if i in cache: return cache[i]

            res = dfs(i+1)

            j = i

            while j < n:
                if jobs[i][1] <= jobs[j][0]:
                    break
                j+=1

            cache[i] = output = max(res, jobs[i][2] + dfs(j))
            return output

        
        return dfs(0)

