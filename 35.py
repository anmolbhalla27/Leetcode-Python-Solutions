nums = [1,3,5,6]
target = 5
beg = 0
end = len(nums) - 1
while (beg <= end):
    mid = (beg + end)//2
    if nums[mid] == target:
        print(mid)
    elif nums[mid] < target:
        beg = mid + 1
    else:
        end = mid -1 
print(end + 1)