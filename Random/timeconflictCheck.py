
'''
Problem Statement:
Given a list of tuples, where each tuple contains (start_time, end_time, person_name), determine if there is any overlap in the meeting times for the same person. If a person has two meetings that overlap in time, return True (conflict exists), otherwise return False.

'''







def checkConflict(meetings: list) -> bool:

        intervals.sort(key=lambda x : x[0])
        
        for i in range(len(meetings) - 1):
                if meetings[i][1] > meetings[i+1][0]:
                        return False
        return True





intervals = [(0,30),(5,10),(15,20)]# Output: false

print(checkConflict(intervals))
intervals = [(5,8),(9,15)] # Output: true
print(checkConflict(intervals))
