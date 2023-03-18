nums = [3,1,2,2,3]
# main = []
# val =int(input("enter:"))
# for i in range(0,len(nums)):
#     if nums[i] != val:
#         main.append(nums[i])
#     else:
#         i = i + 1
# main.sort()
# print(main)
val =int(input("enter:"))
k = 0
for i in range(0,len(nums)):
    if nums[i] != val:
        # nums[k] = nums[i]
        k += 1
print(k)
# print(nums)