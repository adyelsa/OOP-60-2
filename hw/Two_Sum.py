def two_sum(nums, target):


    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:


                return [i, j]

nums = [2, 5, 8, 12]

target = 13
print(two_sum(nums, target))


