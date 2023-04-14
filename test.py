def twosum(nums,targets):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==targets:
                return [i,j]

print(twosum([2,7,11,15],9))