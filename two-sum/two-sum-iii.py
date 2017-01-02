'''
Two Sum III - Data structure design
Total Accepted: 311 Total Submissions: 1345

Design and implement a TwoSum class. It should support the following operations:add and find.
add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.
For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false

Author: Phil H. Cui
Date: 12/01/16
'''

class TwoSum( object ):

    def __init__( self ):
        self.lookup = dict()


    def add( self, val ):
        if val not in self.lookup:
            self.lookup[val] = 1
        else:
            self.lookup[val] += 1

    def find( self, val ):
        for key in self.lookup:
            num = val - key
            if num in self.lookup and ( num != key or self.lookup[key] > 1 ):
                return True

        return False


if __name__ == '__main__':
    twoSum = TwoSum()

    twoSum.add(1)
    twoSum.add(3)
    twoSum.add(5)

    print twoSum.find(4)
    print twoSum.find(7)
