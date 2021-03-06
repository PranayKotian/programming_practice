#https://leetcode.com/problems/first-missing-positive/
#Title: First Missing Positive
#Difficulty: Hard
#Language: Python3
#Author: Pranay Kotian

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #Sorts list
        nums.sort()
        
        #Removes duplicates from list
        finList = []        
        for i in nums:
            if i not in finList:
                finList.append(i)
        
        #Iterates through list returning the first missing positive integer
        min = 1
        for i in finList:
            if (i < 1):
                continue
            if (i == min):
                min += 1
            else:
                return min
        return min

        """
        Runtime: 28 ms, faster than 94.51% of Python3 online submissions for First Missing Positive.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for First Missing Positive.
        """