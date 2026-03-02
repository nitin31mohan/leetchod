#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tgt_dct = {}    # {val: idx}

        for idx, val in enumerate(nums):
            if not (target - val) in tgt_dct:
                tgt_dct[val] = idx
            else:
                return [tgt_dct[(target - val)], idx]
            

        
# @lc code=end
