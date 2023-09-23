# https://leetcode.com/problems/longest-string-chain/?envType=daily-question&envId=2023-09-23

class Solution:

    def longestStrChain(self, words):
        words.sort(key=len)
        word_to_length = {} 
        max_chain_length = 1 #minm possible longest chain

        for word in words:
            word_to_length[word] = 1 # minm contribution to longest chain
            for i in range(len(word)): # iterate the whole word and remove the ith char
                predecessor = word[:i] + word[i + 1:] # Tried to remove a chr and generate a predecssor
                if predecessor in word_to_length: # if it's already exist or not
                    #if exist increase the contribution by 1 of the ancestor
                    word_to_length[word] = max(word_to_length[word], word_to_length[predecessor] + 1) 
            # update the maxm chain length
            max_chain_length = max(max_chain_length, word_to_length[word])

        return max_chain_length


'''
   'abc'

   pred = { 'ac', 'ab' 'bc'}

'''