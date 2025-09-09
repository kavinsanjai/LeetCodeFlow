class Solution(object):
    def distributeCandies(self, candyType):
        unique_candy=set(candyType)
        uni_len=len(unique_candy)
        pos_can=len(candyType)/2
        if uni_len<pos_can:
            return uni_len
        else:
            return pos_can
        