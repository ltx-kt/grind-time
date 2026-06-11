"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        start = Interval(0,0)
        for i in intervals:
            if i.start < start.end:
                # print(i.start, start.end)
                return False
            start = i
        return True


