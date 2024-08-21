'''
There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.

 

Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
 
'''
#Solution
class Solution:
    def strangePrinter(self, s: str) -> int:
        # Get the length of the input string
        n = len(s)
        
        # Create a n x n matrix to store the minimum number of turns needed to print s[i:j+1]
        dp = [[0] * n for _ in range(n)]
        
        # Loop backwards over the matrix to fill in the upper diagonal
        for i in range(n-1, -1, -1):
            # Initialize the diagonal values to 1, since it takes one turn to print a single character
            dp[i][i] = 1
            
            # Loop forwards over the matrix to fill in the lower diagonal
            for j in range(i+1, n):
                # If s[i] and s[j] are the same character, we can print them together in one turn
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j-1]
                else:
                    # If s[i] and s[j] are different characters, we try to use the previously computed dp values
                    # and update the current dp value by taking the minimum value of the two possible options
                    dp[i][j] = float('inf')
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
        
        # The minimum number of turns needed to print the entire string s is stored in dp[0][n-1]
        return dp[0][n-1]
    
#Solution
class Solution:
    def strangePrinter(self, s: str) -> int:
        n=len(s)
        if not s:
            return 0

        dp=[[sys.maxsize]*n for _ in range(n)]

        for i in range(n):
            dp[i][i]=1

        for l in range(2,n+1):
            for i in range(n-l+1):
                j=i+l-1
                dp[i][j]=dp[i+1][j]+1

                for k in range(i+1,j+1):
                    if s[i]==s[k]:
                        dp[i][j]=min(dp[i][j],dp[i][k-1]+(dp[k+1][j] if j>k else 0))

        return dp[0][n-1]                        