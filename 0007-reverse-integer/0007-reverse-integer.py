class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        negative = x<0
        if negative:
            x = abs(x)
        while (x>0):
            ld = x%10
            x=x//10
            rev=(rev*10)+ld
        if negative:
            rev = -rev 
        if rev>2147483647 or rev <-2147483648:
            return 0
            
        return rev 

        