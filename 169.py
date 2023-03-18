nums = [2,2,1,1,1,2,2,3]
dic = {}
for i in range(len(nums)):
    if nums[i] not in dic:
        i = nums[i]
        dic[i] = 1
    else:
        if nums[i] in dic:
            i = nums[i]
            dic[i] += 1
print(dic)
ans = 0
maxx = 0
for i in dic:
    if dic[i] > maxx:
        maxx = dic[i] 
        ans = i
print(ans)