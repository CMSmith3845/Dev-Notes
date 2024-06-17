# nums = input(print("Enter a series of numbers seperatred by commas"))

# -10 ** 9 <=nums[i] <= 10 ** 9
# -10 ** 9 <= target <= 10 **9

class Solution:
    def twoSum(self, nums: List[int], target: int -> List[int]):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (i != j and nums[j] == target)
                return [i, j]
        return []
