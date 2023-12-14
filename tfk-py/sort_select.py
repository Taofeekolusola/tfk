def sort(nums):
    for i in range(5):
        m_pos = i
        for j in range(i,6):
            if nums[j] < nums[m_pos]:
                m_pos = j


        temp = nums[i]
        nums[i] = nums[m_pos]
        nums[m_pos] = temp
        print(nums)

nums = [4, 5, 2, 7, 8, 1, 9]
sort(nums)
print(nums)
