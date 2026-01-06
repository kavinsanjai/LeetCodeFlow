class Solution(object):
    def totalFruit(self, fruits):
        count=1
        fre={}
        fre[fruits[0]]=1
        l=0
        max_count=1

        for i in range(1,len(fruits)):
            value=fruits[i]
            fre[value]=fre.get(value,0)+1

            while len(fre)>2:
                r_value=fruits[l]

                if fre[r_value]>1:
                    fre[r_value]-=1
                else:
                    del fre[r_value]
                l+=1

            max_count=max(max_count,i-l+1)
            
        return max_count


        