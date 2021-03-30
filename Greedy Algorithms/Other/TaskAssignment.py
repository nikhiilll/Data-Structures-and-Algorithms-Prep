from collections import defaultdict

def taskAssignment(k, tasks):
    """
    TC: O(nlogn)
    SC: O(n)
    """
    ans = []
    hashmap = defaultdict(list)
    for i, duration in enumerate(tasks):
        hashmap[duration].append(i)
    
    tasks.sort()

    for i in range(k):
        j = -(i + 1)
        idx1, idx2 = hashmap[tasks[i]].pop(), hashmap[tasks[j]].pop()
        ans.append([idx1, idx2])
    
    return ans