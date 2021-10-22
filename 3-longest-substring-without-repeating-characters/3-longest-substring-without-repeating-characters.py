class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sub = {}
        curr_sub_start = 0
        curr_length = 0
        longest = 0 
        
        if len(s) < 1:
            return 0
        
        for i, letter in enumerate(s):
            
            if letter in sub and sub[letter] >= curr_sub_start:
                curr_sub_start = sub[letter]+1
                curr_length = i - sub[letter]
                sub[letter] = i
            
            else:
                sub[letter] = i 
                curr_length += 1
                if curr_length > longest:
                    longest = curr_length
            
        return(longest)        