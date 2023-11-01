# PROBLEM : Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: false

# Example 2:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Date:01/11/23

# create a empty hashset and store the elements.
# if the element already exists in the hashset then it's a duplicate.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)   
        return False
    
