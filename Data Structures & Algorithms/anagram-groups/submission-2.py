from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #Aiming for solution of O(m*n) time and O(m) space
    #where m is # strings n is length longest string
        result = defaultdict(list)
        for str in strs:
            count = [0] * 26 #define array for character count
            for char in str:
                count[ord(char) - ord('a')] += 1 #ord'a' acts as index for count of each char
            result[tuple(count)].append(str) #the tuple of count is the key and str is value appended
        return list(result.values())    