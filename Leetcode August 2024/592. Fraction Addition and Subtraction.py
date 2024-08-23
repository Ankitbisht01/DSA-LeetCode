'''
Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.

 

Example 1:

Input: expression = "-1/2+1/2"
Output: "0/1"
Example 2:

Input: expression = "-1/2+1/2+1/3"
Output: "1/3"
Example 3:

Input: expression = "1/3-1/2"
Output: "-1/6"
 

Constraints:

The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
The number of given fractions will be in the range [1, 10].
The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
'''#Solution
class Solution:
    def fractionAddition(self, expression: str) -> str:

        numerator = 0
        denominator = 2520

        for frac in expression.split("+"):
            for j, f in enumerate(frac.split("-")):
                if f == "":
                    continue
                n, d = [int(v) for v in f.split("/")]
                if j == 0:
                    numerator += denominator // d * n
                else:
                    numerator -= denominator // d * n


        if numerator == 0:
            return "0/1"
        
        for factor in (2, 3, 5, 7):
            while (numerator % factor == 0) and (denominator % factor == 0):
                numerator //= factor
                denominator //= factor

        return f"{numerator}/{denominator}"
        

        

        