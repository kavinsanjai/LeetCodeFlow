class Solution(object):
    def checkIfExist(self, arr):
        arr.sort()
        for i in arr:
            if i*2 in arr:
                if i*2!=0:
                    return True
                elif  (i*2==0 and arr.count(0) >1):
                    return True
        return False
        