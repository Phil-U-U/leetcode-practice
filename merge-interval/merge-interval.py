'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].


Author: Phil H. Cui
Date: 11/30/16

'''




class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        res = []
        if len( intervals ) == 0 or intervals[0] == None:
            return res

        else:
            intervals = sorted( intervals, key = lambda x:x.start )

            newInterval = intervals[0]

            for interval in intervals[1:]:
                if newInterval.end < interval.start:
                    res.append( newInterval )
                    newInterval = interval
                elif newInterval.start > interval.end:
                    res.append( interval )
                else:
                    newInterval.start = min( newInterval.start, interval.start )
                    newInterval.end = max( newInterval.end, interval.end )

            res.append( newInterval )

            # for interval in res:
            #     print [interval.start, interval.end]
            return res


if __name__ == '__main__':
    intervals = [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]
    print Solution().merge(intervals)
