class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        final = []
        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        
        for interval in intervals:
            if interval[0] <= curr_end:
                curr_end = max(interval[1], curr_end)
            else:
                final.append([curr_start, curr_end])
                curr_start = interval[0]
                curr_end = interval[1]
        final.append([curr_start, curr_end])
        return final