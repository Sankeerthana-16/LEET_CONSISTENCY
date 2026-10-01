class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        arr=[]
        a=0
        for i in range(len(nums)):
            a=a+nums[i]
            arr.append(a)


            #nums[i] +=nums[i-1]
        return arr
            
                
            
        