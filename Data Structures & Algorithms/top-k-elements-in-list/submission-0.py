class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #returns k number of most frequent elements (no order needed)
        count = {}
        freq = [[] for i in range (len(nums) + 1)] #list of lists for each num

        for num in nums:
            count[num] = 1 + count.get(num, 0) #count dict contains frequency of each number
        for num, cnt in count.items():
            freq[cnt].append(num) #appends num(s) at index of its count

        result = []
        for i in range(len(freq) - 1, 0, -1): #iterate from last index ie largest freq
            for num in freq[i]:
                result.append(num)
                if len(result) == k: 
                    return result

        