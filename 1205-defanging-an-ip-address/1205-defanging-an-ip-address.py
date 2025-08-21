class Solution(object):
    def defangIPaddr(self, address):
        return re.sub(r'\.','[.]',address)        
        