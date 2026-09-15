class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s_nums = sorted(nums)
        for x in range(len(s_nums)):
            if x == 0: continue
            if s_nums[x-1] == s_nums[x]:
                return True

        return False
        
