'''
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Constraints:

1 <= num < 231
 
'''

#Solution1
#Pyhon3 Code
class Solution:
    def findComplement(self, num: int) -> int:
        num = str(bin(num))[2: ]
        res = 0
        for i in range(len(num) - 1, -1, -1):
            if num[i] == "0":
                res += pow(2, (len(num) - 1) - i)

        return res
    
#Solution2
class Solution:
    def findComplement(self, num: int) -> int:
        # Step 1: Get the number of bits in 'num'
        num_bits = num.bit_length()
        
        # Step 2: Create a mask with all bits set to 1 for the same length as 'num'
        mask = (1 << num_bits) - 1
        
        # Step 3: XOR 'num' with 'mask' to get the complement
        return num ^ mask
