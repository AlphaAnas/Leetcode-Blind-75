
'''
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of rooms required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is NOT considered a conflict at 8.


'''
def minMeetingRooms(intervals) -> int:

    count = 0
    maxCount = 0
    start = [i[0] for i in intervals]
    start.sort()
    end = [i[1] for i in intervals]
    end.sort()
    s = start[0]
    e = end[0]
    while s < len(start) and e < len(end):
        if start[s] < end[e]:
            s += 1
            count += 1
        elif start[s] >=end[e]:
            e += 1
            count -= 1
        maxCount = max(maxCount, count)
    return maxCount


print(minMeetingRooms([(0,40),(5,10),(15,20)])) # output 2
print(minMeetingRooms( intervals = [(4,9)])) # output 1

