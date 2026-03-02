#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = [0]*26

        for ch in s:
            freq[ord(ch) - 97] += 1
        
        for ch in t:
            ind = ord(ch) - 97
            freq[ind] -= 1

            if freq[ind] < 0: return False
        
        return True

        
# @lc code=end

