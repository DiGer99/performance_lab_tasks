def count_steps(nums: list[int]) -> int:
    nums.sort()

    median = nums[len(nums) // 2]
    total = sum(abs(num - median) for num in nums)

    return total
