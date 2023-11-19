from typing import Optional
from pydantic import BaseModel
from collections import defaultdict, namedtuple
from ordered_set import OrderedSet

class TimeIntervals:
    def __init__(self,):
        self.EmployeeShift = namedtuple('EmployeeShift', ['shiftTime', 'empName', 'isEnd'])
        self.Output = namedtuple('Output', ['startTime', 'endTime', 'empNames'])
        pass

    class Input(BaseModel):
        inputs: Optional[Optional[list]] = None

    class Outputs(BaseModel):
        answer: Optional[list] = None
    

    def compare_by_time(a, b):
        if a.shiftTime == b.shiftTime:
            return a.empName < b.empName
        return a.shiftTime < b.shiftTime

    def solution(self,n, employees, shifts):
        print(n,employees,shifts)
        sorted_shifts = []

        for i in range(n):
            shift_start, shift_end = shifts[i]
            sorted_shifts.append(self.EmployeeShift(shift_start, employees[i], False))
            sorted_shifts.append(self.EmployeeShift(shift_end, employees[i], True))

        sorted_shifts.sort(key=lambda x: (x.shiftTime, x.empName))

        prev_time = sorted_shifts[0].shiftTime
        op = []
        names = []

        for shift in sorted_shifts:
            curr_time = shift.shiftTime
            name = shift.empName
            is_end = shift.isEnd

            if prev_time != curr_time:
                names.sort()
                o = self.Output(prev_time, curr_time, list(names))
                op.append(o)
                prev_time = curr_time

            if is_end:
                names.remove(name)

            if name not in names and not is_end:
                names.append(name)
        ans = []
        ans.append(str(len(op)))
        for o in op:
            ans.append(str(o.startTime)+" "+ str(o.endTime)+" "+ str(len(o.empNames))+" "+ ' '.join(o.empNames))

        return ans

    # @staticmethod

    def solve(self,input):
        
        n = int(input[0])
        employees = list(input[1].split(' '))
        c = 2
        shifts = []
        for _ in range(n):
            shift = list(map(int, input[c].split(' ')))
            shifts.append(shift)
            c+=1

        
        return self.solution(n, employees, shifts)

                