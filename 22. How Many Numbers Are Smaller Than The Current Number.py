def smaller_numbers_than_current(nums):
    counts = [0] * len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[j] < nums[i]:
                counts[i] += 1
    return counts