class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        n = len(nums)
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1

        for key, val in hashMap.items():
            if val > n // 2:
                return key