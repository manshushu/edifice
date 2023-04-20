class Solution:
    def missingNumber(self,nums:List[int])-> int:
        i,j =0,len(nums)-1
        while i<=j:
            m=(i+j)//2
            if nums[m]==m:i=m+1
            else: j=m-1
        return i