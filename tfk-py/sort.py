def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
nums =[1,3,2,5,4,6,8,9,10,7]
sort(nums)
print(nums)
