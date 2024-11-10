def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    x = 1
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            nums[x] = nums[i+1]
            x+=1
    print(nums[:x])

nums = [1,1,2,2,3,3,3,4]
removeDuplicates(nums)