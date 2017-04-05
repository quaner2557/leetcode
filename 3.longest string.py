class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lis = {}
        n ,start = 0, 0

        for i in range(len(s)):
            if s[i] in lis and start <= lis[s[i]] :
                start = lis[s[i]]+1
            else:
                n = max(n,i-start+1)

            lis[s[i]] = i

        return n

s=Solution()
s.lengthOfLongestSubstring("abcabcbb")
