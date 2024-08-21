'''
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

'''
#Solution
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change5=0
        change10=0
        change20=0
        for i in range(len(bills)):
            if bills[i]==5:
                change5+=1
            elif bills[i]==10:
                change10+=1
                change5-=1
            elif bills[i]==20:
                if change10>0 :
                    change5-=1
                    change10-=1
                else:
                    change5-=3
                change20+=1
            if change5<0 or change10<0 or change20<0:
                return False
        return True