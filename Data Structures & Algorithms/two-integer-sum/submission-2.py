class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         sum = nums[i] + nums[j]
        #         if sum == target:
        #             return [i, j]

        seen = {}
        for idx, num in enumerate(nums):
            needed = target - num
            
            if needed in seen:
                return [seen[needed], idx]
            seen[num] = idx
             