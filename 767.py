import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s):
        count = Counter(s)
        
        maxHeap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(maxHeap)
        
        prev = (0, '')
        result = []
        
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            result.append(char)
            
            if prev[0] < 0:
                heapq.heappush(maxHeap, prev)
            
            freq += 1
            prev = (freq, char)
        
        res = ''.join(result)
        
        return res if len(res) == len(s) else ""
