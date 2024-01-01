from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for point in points:
            x, y = point
            distance = x**2 + y**2
            distances.append((point, distance))

        distances.sort(key=lambda x: x[1])

        result = [point for point, _ in distances[:k]]
        return result
