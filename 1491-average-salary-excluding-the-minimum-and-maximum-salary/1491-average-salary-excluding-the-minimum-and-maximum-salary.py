class Solution:
    def average(self, salary: List[int]) -> float:
        maxx=max(salary)
        minn=min(salary)
        summ=sum(salary)-maxx-minn
        return summ/(len(salary)-2)
        