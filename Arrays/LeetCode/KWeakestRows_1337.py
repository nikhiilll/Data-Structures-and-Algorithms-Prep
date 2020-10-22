import operator

def kWeakestRows(mat, k):

    dict_rows = {}
    ret_rows = []

    for i in range(len(mat)):
        count = mat[i].count(1)
        if count not in dict_rows:
            dict_rows[count] = [i]
        else:
            dict_rows[count].append(i)

    for key in sorted(dict_rows.keys()):
        ret_rows += dict_rows[key]

    return ret_rows[:k]

mat = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
k = 2

print(kWeakestRows(mat, k))

"""



"""
