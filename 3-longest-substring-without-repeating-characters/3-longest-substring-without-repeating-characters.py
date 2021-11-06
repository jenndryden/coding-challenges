class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sub = {}
        curr_sub_start = 0
        curr_sub_length = 0
        longest = 0

        for i, letter in enumerate(s):

            if letter in sub and sub[letter]>=curr_sub_start:
                curr_sub_start = sub[letter] 
                curr_sub_length = i - sub[letter]
                sub[letter] = i

            else: 
                curr_sub_length += 1
                sub[letter] = i

                if curr_sub_length > longest:
                    longest = curr_sub_length 

        return(longest)