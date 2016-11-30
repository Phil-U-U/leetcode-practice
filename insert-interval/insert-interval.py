class Intervals( object ):
    def __init__( self, s = 0, e = 0 ):

        self.start = s
        self.end = e



class Solution( object ):


    def insertInterval( self, intervals, newInterval ):
        res = []

        for interval in intervals:

            if newInterval[1] < interval[0]:
                res.append( newInterval )
                newInterval = interval
            elif newInterval[0] > interval[1]:
                res.append( interval )
            else:
                newInterval[0] = min( interval[0], newInterval[0] )
                newInterval[1] = max( interval[1], newInterval[1] )

        res.append( newInterval )

        return res


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution_interval_object(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []

        for interval in intervals:
            if newInterval.end < interval.start:
                res.append( newInterval )
                newInterval = interval
            elif newInterval.start > interval.end:
                res.append( interval )
            else:
                newInterval.start = min( interval.start, newInterval.start )
                newInterval.end = max( interval.end, newInterval.end )

        res.append( newInterval )

        return res



if __name__ == '__main__':
    solution = Solution()
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print "Expected:{}-Answer:{}".format("[1,5],[6,9]", solution.insertInterval( intervals, newInterval))

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,9]
    print "Expected:{}-Answer:{}".format("[1,2],[3,10],[12,16]", solution.insertInterval( intervals, newInterval))
