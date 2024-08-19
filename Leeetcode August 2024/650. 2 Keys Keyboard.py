'''
There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

 

Example 1:

Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Example 2:

Input: n = 1
Output: 0
 

Constraints:

1 <= n <= 1000
'''
#solution
class Solution:
    def minSteps(self, n: int) -> int:
      dp = [0] * (n+1)
      
      # how to form a number A:
      # Find the largest number B such that B = A/k
      # Given B is formed with i steps, it takes i + 1 + (k-1) steps to form A
      # - i steps to produce B
      # - 1 step to copy B
      # - (k-1) steps to paste B (k-1) timest to get kB

      for i in range(1, n):
        i = i + 1 # 1 indexed
        for j in reversed(range(1, i//2+1)):
          if i != i // j * j:
            continue
          
          # j is the largest factor of i
          factor = i // j
          dp[i] = dp[j] + factor
          break
      
      return dp[-1]