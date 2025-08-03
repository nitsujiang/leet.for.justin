class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = Counter()
        m = float('inf') # Used for indirect exchanges
        for f1 in basket1:
            freq[f1] += 1
            m = min(m, f1)

        for f2 in basket2:
            freq[f2] -= 1
            m = min(m, f2)
        
        merge = []
        for k, c in freq.items():
            # If the sum is odd -> no excess that can be distributed evenly
            if c % 2 != 0:
                return -1
            # Redistribute the excess half floored
            merge.extend([k] * (abs(c) // 2))

        # The baskets are already equal
        if not merge:
            return 0

        merge.sort()
        return sum(min(2 * m, x) for x in merge[:len(merge) // 2])

