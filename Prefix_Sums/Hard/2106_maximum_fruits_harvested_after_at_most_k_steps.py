class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # Extra 1 to avoid out of pounds when using i - 1 for prefix array  
        max_pos = max(fruits[-1][0], startPos + k) + 2
        prefix = [0] * max_pos

        for pos, amount in fruits:
            prefix[pos + 1] += amount
        
        for i in range(1, max_pos):
            prefix[i] += prefix[i - 1]

        res = 0
        for steps_left in range(k + 1):
            left = max(startPos - steps_left, 0)
            right = max(startPos + (k - 2 * steps_left), 0)
            res = max(res, prefix[right + 1] - prefix[left])

        for steps_right in range(k + 1):
            right = startPos + steps_right
            left = max(startPos - (k - 2 * steps_right), 0)
            res = max(res, prefix[right + 1] - prefix[left])
        return res



