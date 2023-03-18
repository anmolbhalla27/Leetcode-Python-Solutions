height = [1,8,6,2,5,4,8,3,7]
beg = 0
end = len(height) - 1
maxWater = 0
while(beg < end):
    area = min(height[beg], height[end]) * (end - beg)
    maxWater = max(maxWater, area)
    if height[end] > height[beg]:
        beg += 1
    else:
        end -= 1
print(maxWater)