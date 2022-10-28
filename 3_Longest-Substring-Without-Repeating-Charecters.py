class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSeen = set()
        j, m, l = 0, 0, 0
        
        while j<len(s):   
            while s[j] in charSeen:
                charSeen.remove(s[l])
                l+=1
            charSeen.add(s[j])
            m = max(m, j-l+1)
            j += 1
        
        return m
    
