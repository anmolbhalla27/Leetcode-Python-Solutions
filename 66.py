digits = [1,2,3]
s = ""
for ele in digits:
    s += str(ele)
a = int(s) + 1
digits.clear()
digits = [int(ele) for ele in str(a)]
print(digits)