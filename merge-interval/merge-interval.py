# Definition for an interval.
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
            intervals = intervals.sort( key = lambda x:x.start )
            print intervals
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

            return res


if __name__ == '__main__':
    intervals = [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]
    print Solution().merge(intervals)
