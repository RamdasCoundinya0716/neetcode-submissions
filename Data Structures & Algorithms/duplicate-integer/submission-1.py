class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return True if len(nums) != len(set(nums)) else False - Good but takes extra space of O(n)
        # better approach to use hashmap
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        for key in hashMap.values():
            if key >= 2:
                return True
        return False
