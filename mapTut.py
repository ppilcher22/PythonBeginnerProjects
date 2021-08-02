table = [True, False, True, False, False]
nums = [1,3,7,8,9,6,4,3,6]
#result = list(map(lambda x: x*10, nums))

print(list(filter(lambda x : x % 3 == 0, list(map(lambda x: x*10, nums)))))