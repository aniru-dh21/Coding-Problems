class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop(0)
        salary.pop(len(salary)-1)
        s = sum(salary)
        return float(s/len(salary))
