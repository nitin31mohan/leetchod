#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

from collections import defaultdict
from typing import List
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            result[tuple(count)].append(s)
        
        return list(result.values())
        
# @lc code=end

