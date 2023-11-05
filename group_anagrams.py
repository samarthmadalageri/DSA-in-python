# PROBLEM: Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Date:03/11/23

# we create a key where the indexes of the list denote the charaters from a-z and the values at those indexes represent the no. of times they have occured in a word
# if two words are anagrams of each other then they will have same key.

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
     res = defaultdict(list) #mapping charCount to list of anagrams

     for s in strs:
         count = [0] * 26  #a ... z
         for c in s:
             count[ord(c) - ord('a')] += 1
         res[tuple(count)].append(s)   #we can't use list as key because they are mutable hence we use tuple.
         
     return res.values()