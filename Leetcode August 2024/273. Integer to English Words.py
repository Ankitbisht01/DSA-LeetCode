'''
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

Constraints:

0 <= num <= 231 - 1
'''
#Solution
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        bigString = ["Thousand", "Million", "Billion"]
        result = self.helper(num % 1000)
        num //= 1000
        
        for i in range(len(bigString)):
            if num > 0 and num % 1000 > 0:
                result = self.helper(num % 1000) + bigString[i] + " " + result
            num //= 1000
        
        return result.strip()

    def helper(self, num: int) -> str:
        below_ten = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        below_twenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        below_hundred = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        result = ""
        if num > 99:
            result += below_ten[num // 100] + " Hundred "
        
        num %= 100
        if num < 20 and num > 9:
            result += below_twenty[num - 10] + " "
        else:
            if num >= 20:
                result += below_hundred[num // 10] + " "
            num %= 10
            if num > 0:
                result += below_ten[num] + " "
        
        return result