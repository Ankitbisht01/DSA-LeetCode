'''
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

'''
#Solution
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def total_pairs(mid, nums, k):
            a = 1
            total = 0
            i = 0
            while (i < n):
                while (a < n) and (nums[a] - nums[i] <= mid):
                    a += 1
                total += a - i - 1
                i += 1
            return total

        nums.sort()
        l = 0
        r = nums[-1] - nums[0]
        while l < r:
            mid = (l + r) // 2
            if (total_pairs(mid, nums, k)) >= k:
                r = mid
            else:
                l = mid + 1
        return l