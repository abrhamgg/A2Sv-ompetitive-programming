class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        started = False
        mine = 0
        piles = sorted(piles)
        while (len(piles) != 0):
            try:
                piles.pop(-1)
                coin = piles[-1]
                mine += coin
                piles.pop(-1)
                piles.pop(0)

            except:
                pass

        return mine
    
