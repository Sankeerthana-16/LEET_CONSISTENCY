class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        dump = x
        revnum=0
        while(x>0):
            last_digit = x%10
            
            x=x//10
            revnum = (revnum*10)+last_digit
        if dump == revnum:
            return True
        else:
            return False