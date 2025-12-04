class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        new_interval=[]
        inserted = False
        
        if len(intervals) == 0:
            return [newInterval]

        for i in range(len(intervals)):
            if newInterval[0] < intervals[i][0]:
                intervals.insert(i, newInterval)
                inserted = True
                break

        if not inserted:
            intervals.append(newInterval)
        # intervals.append(newInterval)
        # intervals.sort()
        # print(intervals)
        # new_interval=[]
        for i in range(0,len(intervals)):
            if not new_interval:
                new_interval.append(intervals[i])
            elif new_interval[-1][1]>=intervals[i][0]:
                new_interval[-1][1]=max(new_interval[-1][1],intervals[i][1])
            else:
                new_interval.append(intervals[i])
        return new_interval



        