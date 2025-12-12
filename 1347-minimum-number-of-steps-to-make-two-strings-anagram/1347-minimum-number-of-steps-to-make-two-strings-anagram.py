class Solution:
    def minSteps(self, s: str, t: str) -> int:
        fres=Counter(s)
        fret=Counter(t)
        new_fre=fret-fres
        return sum(new_fre.values())