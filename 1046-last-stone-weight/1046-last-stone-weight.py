class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda stone: -stone, stones))
        heapq.heapify(stones)
        
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            
            if first != second:
                heapq.heappush(stones, first-second)
        
        return 0 if not stones else -stones[0]
        