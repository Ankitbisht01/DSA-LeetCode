'''
You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.
'''
#Solution
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minNum = arrays[0][0]
        maxNum = arrays[0][-1]
        maxDistance = 0
        for i in range(1, len(arrays)):
            maxDistance = max(maxDistance, abs(arrays[i][-1] - minNum), abs(maxNum - arrays[i][0]))
            minNum = min(minNum, arrays[i][0])
            maxNum = max(maxNum, arrays[i][-1])
        return maxDistance