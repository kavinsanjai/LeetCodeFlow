class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        abs=arr[1]-arr[0]
        sub_list=[]
        n=len(arr)
        for i in range(1,n):
            if (abs>(arr[i]-arr[i-1])):
                    abs=arr[i]-arr[i-1]
        for i in range(1,n):
            if(abs==arr[i]-arr[i-1]):
                sub_list.append([arr[i-1],arr[i]])
        return sub_list
    
        