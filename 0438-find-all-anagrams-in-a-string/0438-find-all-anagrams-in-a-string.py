class Solution(object):
    def findAnagrams(self, s, p):
        fre_p=Counter(p)
        n=len(p)
        ana_list=[]
        anagram=s[:n]
        fre_a=Counter(anagram)
        if fre_a == fre_p:
            ana_list.append(0)
        for i in range(n,len(s)):
            r_char=s[i-n]
            char=s[i]
            fre_a[char]=fre_a.get(char,0)+1
            if fre_a[r_char] >1:
                fre_a[r_char]-=1
            else:
                del fre_a[r_char]
            if fre_a == fre_p:
                ana_list.append(i-n+1)             
        return ana_list
