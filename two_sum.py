# PROBLEM: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Date:03/11/23

# we use hashmap to store values and their index
# enumerate function gives us the value and it's index

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevmap = {}      #value:index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevmap:
                return [prevmap[diff], i]
            prevmap[n] = i
        return
