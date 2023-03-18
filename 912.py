nums = [5,2,3,1]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1 
            j += 1
        else:
            i += 1
            j += 1
print(nums)