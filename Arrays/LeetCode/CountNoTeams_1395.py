from collections import defaultdict

def numTeams(rating):

    possible_teams = 0

    if len(rating) < 3:
        return 0
    
    nos_greater = defaultdict(int)
    nos_smaller = defaultdict(int)

    for i in range(len(rating) - 1):
        for j in range(i + 1, len(rating)):
            if rating[j] > rating[i]:
                nos_greater[i] += 1
            else:
                nos_smaller[i] += 1
    
    for i in range(len(rating) - 2):
        for j in range(i + 1, len(rating)):
            if rating[i] < rating[j]:
                possible_teams += nos_greater[j]
            else:
                possible_teams += nos_smaller[j]
    
    return possible_teams


rating = [4,7,9,5,10,8,2,1,6]
print(numTeams(rating))

