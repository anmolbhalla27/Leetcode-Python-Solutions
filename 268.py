nums = [3,0,1]
dictionary = {}
for i in nums:
    if i in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] = 0
for i in range(0,len(nums)+1):
    if i not in dictionary:
        print(i)