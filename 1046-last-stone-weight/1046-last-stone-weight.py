class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapify(stones)

        a = heappop(stones)
        while stones:
            b = heappop(stones)
            d = -abs(a - b)
            if d != 0:
                heappush(stones, d)
            a = 0 if not stones else heappop(stones)
        
        return -a

            

        return 0 if not stones else stones[0]         