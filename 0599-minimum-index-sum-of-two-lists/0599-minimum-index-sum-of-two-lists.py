class Solution(object):
    def findRestaurant(self, list1, list2):
        result = float("inf") 
        new=[]
        for i in range(0,len(list1)):
            for j in range(0,len(list2)):
                if list1[i]==list2[j]:
                    if i+j < result:
                        result=i+j
                        new = [list1[i]]
                    elif i + j == result:  
                        new.append(list1[i])   
        return new                   
