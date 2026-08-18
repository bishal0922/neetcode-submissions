class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i):
            if i == len(jobs):
                return 0
            if i in cache: return cache[i]

            res = dfs(i+1)

            j = 0
            while j < len(jobs):
                if jobs[i][1] <= jobs[j][0]:
                    break
                j+=1


            cache[i] = res = max(res, jobs[i][2] + dfs(j))
            return res

        return dfs(0)
            

        