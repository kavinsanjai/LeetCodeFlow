class Solution(object):
    def lengthOfLongestSubstring(self,s):
        seen=set()
        l=0
        count=0
        max_count=0
        for i in range(0,len(s)):
            while s[i] in seen :
                seen.remove(s[l])
                l+=1
            seen.add(s[i])
            count=len(seen)
            max_count=max(count,max_count)
        return max_count


