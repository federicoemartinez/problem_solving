# https://leetcode.com/problems/reveal-cards-in-increasing-order/
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        ret_deck = [None]*len(deck)
        deck.sort(key=lambda x:-x)
        skip = False
        while(deck):
            i = 0
            while i < len(ret_deck):
                if ret_deck[i] is None:
                    if not skip: 
                        ret_deck[i] = deck.pop()
                    skip = not skip
                    i+=1
                else:
                    i+=1
                        
                    
        return ret_deck
