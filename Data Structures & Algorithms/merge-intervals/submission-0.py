class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1: return intervals

        intervals.sort(key = lambda x : x[0]) #sort by start times

        result = [] # store the final "merged" intervals
        result.append(intervals[0]) # start with the final


        # we want to linearly go through the array
            # we want to see if at any i we can merge it with our existing final set of intervals
            # interval start time <= end time (latest time in our result array)
                # update the end time in our latest/last element in result
            # if start time > end time 
                # add to our result

        for i, interval in enumerate(intervals[1:]):
            latest_time = result[-1]

            # 1,3 is our latest time and 2,6 is our ith interval
            # here 
            if interval[0] <= latest_time[1]:
                #update the latest time
                # result[-1] = [old_start, new end]
                result[-1] = [latest_time[0], max(latest_time[1],interval[1])]
            else:
                result.append(interval)

        
        return result

        # time is 
        # space is O(n) worse case we store all the intervals 