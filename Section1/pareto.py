import random
from collections import defaultdict

lst = [1,2,3,4,5,6,7,8,9,10]
nums = defaultdict(int)
x = 0
res = []
total = 1000

while x != 1000:
    for i in range(1000):
        rand_num = random.choice(lst)
        nums[rand_num] += 1
        lst.append(rand_num)
    res_lst = list(nums.items())
    res_lst.sort(reverse=True, key=lambda x: x[1])
    result = (res_lst[0][1] + res_lst[1][1])/1000
    res.append((result*total, result))
    lst = list(set(lst))
    nums = defaultdict(int)
    x += 1

val = 0
for i in res:
    val += i[0]

print(val/1000000)
