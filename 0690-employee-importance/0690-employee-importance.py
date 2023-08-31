"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_dict = {employee.id: employee for employee in employees}
        def dfs(employe_id):
            targetempolyee = employee_dict[employe_id]
            totalimportance = targetempolyee.importance
            for subbordinatesid in targetempolyee.subordinates:
                totalimportance += dfs(subbordinatesid) 
                
            return totalimportance
        return dfs(id)
            
        
            
            
        