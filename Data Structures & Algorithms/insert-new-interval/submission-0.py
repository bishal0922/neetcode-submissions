class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # intervals i am thinking of a line segmenet
        # what we can do is initial a 

        result = []
        i = 0


        # go through the interval
        for i, interval in enumerate(intervals):
            # if you can insert before insert and return
                # before means newinterval[1] end i before start of interval[i][0]
            if newInterval[1] < interval[0]:
                result.append(newInterval)
                return result + intervals[i:] 
            elif newInterval[0] > interval[1]:
                result.append(intervals[i])
            else:
                start = min(interval[0], newInterval[0])
                end = max(interval[1], newInterval[1])
                newInterval = [start, end]
        
        result.append(newInterval)

        return result

            # if you can insert after the interval continue
                # new interval[0] is after interval[i][1]
                # jsut continue , insert current to result (seen it)
            
            # if the end of new interval is greater than start of i[0], get the new interval 
            # start is min
            # end is max
            # that is the new newinterval now

             
            



