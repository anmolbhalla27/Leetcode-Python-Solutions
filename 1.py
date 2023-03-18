nums = [2,7,11,15]
target = 9
dic={}
for i, n in enumerate(nums):
    rem = target - n
    if rem in dic:
        print([dic[rem], i])
    dic[n] = i