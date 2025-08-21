class Solution(object):
    def findOcurrences(self, text, first, second):
        sen_list=text.split()
        new=[]
        for i in range(1,len(sen_list)):
            if sen_list[i]==second:
               if sen_list[i-1]==first:
                    if i!=len(sen_list)-1:
                        new.append(sen_list[i+1])
        return new      
        