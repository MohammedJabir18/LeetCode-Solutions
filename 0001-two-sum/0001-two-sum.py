class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def two_sum_recursive(nums, target, index=0, seen={}):
            if index == len(nums):
                return None

            num = nums[index]
            complement = target - num
            if complement in seen:
                return [seen[complement], index]

            seen[num] = index
            return two_sum_recursive(nums, target, index + 1, seen)
        return two_sum_recursive(nums, target)
