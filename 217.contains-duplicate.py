#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for ele in nums:
            if ele in hashset:
                return True
            hashset.add(ele)
        return False

        
# @lc code=end

