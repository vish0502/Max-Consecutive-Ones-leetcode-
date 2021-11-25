class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        m=0
        s=0
        c=[]
        n=len(nums)
        for i in range(0,n):
            if (nums[i] == 1):
                count+=1
                c.append(count)
            else:
                count=0
        if (len(c)!=0):
            s=max(c)
        
        m=max(s,m,count)
        return m
        