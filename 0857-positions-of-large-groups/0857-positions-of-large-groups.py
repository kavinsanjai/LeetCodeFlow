class Solution(object):
    def largeGroupPositions(self, s):
        start = 0
        end = 0
        len1 = 0   
        new = []

        for i in range(len(s)):
            if i > 0 and s[i] != s[i-1]:
                if len1 >= 3:
                    new.append([start, end])
                start = i
                len1 = 0
            end = i
            len1 += 1

        if len1 >= 3:
            new.append([start,end])
        return new
