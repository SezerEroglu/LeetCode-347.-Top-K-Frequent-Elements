from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1

        return [
            sublist[1]
            for sublist in sorted(
                hashMap.items(), key=lambda item: item[1], reverse=True
            )[0:k]
        ]
