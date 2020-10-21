# def minimumAbsDifference(arr):

#     diff_dict = {}
#     n = len(arr)

#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             abs_diff = abs(arr[i] - arr[j])
#             if abs_diff not in diff_dict:
#                 if arr[i] < arr[j]:
#                     diff_dict[abs_diff] = [[arr[i], arr[j]]]
#                 else:
#                     diff_dict[abs_diff] = [[arr[j], arr[i]]]
#             else:
#                 if arr[i] < arr[j]:
#                     diff_dict[abs_diff].append([arr[i], arr[j]])
#                 else:
#                     diff_dict[abs_diff].append([arr[j], arr[i]])
    
#     for k in sorted(diff_dict):
#         return sorted(diff_dict[k])

def minimumAbsDifference(a):

    result = []
    min_diff = float('inf')
    n = len(arr)

    for i in range(n - 1):
        for j in range(i + 1, n):
            print(result)
            abs_diff = abs(a[i] - a[j])
            if abs_diff == min_diff:
                if a[i] < a[j]:
                    result.append([a[i], a[j]])
                else:
                    result.append([a[j], a[i]])
            elif abs_diff < min_diff:
                min_diff = abs_diff
                result.clear()
                if a[i] < a[j]:
                    result.append([a[i], a[j]])
                else:
                    result.append([a[j], a[i]])
    
    return sorted(result)





arr = [4,2,1,3]
print(minimumAbsDifference(arr))


"""
def minimumAbsDifference(self, a: List[int]) -> List[List[int]]:
        a.sort()
        ans, diff = [], float('inf')
        for i in range(1, len(a)):
            if diff >= a[i] - a[i - 1]:
                if diff > a[i] - a[i - 1]:
                    # ans.clear()           # modified to the follow to achieve O(1) time, credit to @vivek_23.
                    ans = []
                    diff = a[i] - a[i - 1]
                ans.append([a[i - 1], a[i]])
        return ans


"""