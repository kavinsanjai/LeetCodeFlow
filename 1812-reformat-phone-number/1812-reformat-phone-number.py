class Solution(object):
    def reformatNumber(self, number):
        new=[]
        number=number.replace(" ","")
        number=number.replace("-","")
        n=len(number)
        i=0
        while n > 0:
            if n>4:
                new.append(number[i:i+3])
                i+=3
                n-=3

            elif n==4:
                new.append(number[i:i+2])
                new.append(number[i+2:])
                i+=4
                n-=4
            else:
                new.append(number[i:])
                break                
        
        return '-'.join(new)
        
        