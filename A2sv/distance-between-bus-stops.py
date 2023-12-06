class Solution:
	def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
		first = min(start, destination)
		second = max(start, destination)
		return min(sum(distance[first:second]), sum(distance) - sum(distance[first:second]))