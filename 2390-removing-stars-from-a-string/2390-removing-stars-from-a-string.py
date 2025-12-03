class Solution(object):
    def removeStars(self, s):
        stack=[]
        for i in range(0,len(s)):
            if s[i]=='*' and stack:
                stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)
        