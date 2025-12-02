class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        u,v=edges[0]
        if u==edges[1][0] or u==edges[1][1]:
            return u
        return v

        