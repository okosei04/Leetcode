class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def solve(total, k):
            minVal = min(total,k)
            ans = minVal * (2* total - minVal + 1) // 2
            if k > total:
                ans += k - total

            return ans
        
        def check(index, seg, n, maxSum):
            prevN = index
            totalN = n - index - 1
            prevS = solve(seg-1, prevN)
            if prevS > maxSum:
                return False
            
            totalS = solve(seg-1, totalN)
            if totalS > maxSum:
                return False
            
            if prevS + totalS + seg <= maxSum:
                return True
            
            return False

        start, end = 0, maxSum
        ans = 1

        while start <= end:
            mid = start + (end - start) // 2
            if check(index, mid, n, maxSum):
                ans = mid
                start = mid + 1
            else:
                end = mid - 1

        return ans  

        