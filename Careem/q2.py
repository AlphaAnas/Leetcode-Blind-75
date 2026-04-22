# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


# buhut complex hojae ga classes se
# class Player:
#     def __init__(self, idx, skill):
#         self.idx = idx
#         self.r = 0
#         self.skill = skill

def solution(skills):
    n = len(skills)
    result = [0] * n
    final = []
    teams = []
    for i in range(n):
        teams.append([skills[i], 1, i])
    
    # print("teams: ", teams)

    while(len(teams) > 1): #atleast two teams tou hn
        print("teams",teams)
        print("final:", final)
        l = teams.pop(0)
        r = teams.pop(0)
        if l[0] > r[0]:
            # print("l", l)
            # print("r", r)
            l[1] += 1
            # print("winner: ", l)
            final.append(r[1])
            teams.append(l)
        else:
            r[1] += 1
            print("winner: ", r)
            final.append(l[1])
            teams.append(r)

    print(final)

solution([3,4,2,1])






    
