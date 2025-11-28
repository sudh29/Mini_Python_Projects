# # import pandas as pd

# # data = {
# #     'Team': ['A', 'B', 'C'],
# #     'Q1': [10, 20, 30],
# #     'Q2': [15, 25, 35]
# # }
# # df = pd.DataFrame(data)
# # print("Original DataFrame:\n", df)
# # m_df = pd.melt(df, id_vars=['Team'], var_name='Quarter', value_name='Score')
# # print("Original DataFrame:\n", m_df)


# a = 'sudhanshu is a good boy and a good hacker'
# target = 'good'

# def count_word(ip,tar):
#     n= len(ip)
#     m = len(tar)
#     count = 0
#     i=0
#     while i<n-m:
#         # print(ip[i:i+m],tar,ip[i:i+m] == tar)
#         if ip[i:i+m] == tar:
#             count+=1
#         i+=1
#     return count

# print(count_word(a,target))


# # input =  colections.documents(['cell_id' == ''])

# books  = ['id', 'name','auther_id']
# authors = ['id','name']


# select * from books as b
# right join author as a on b.author_id = a.id


"""
Consider a matrix where each cell contains either a 0 or a 1. Any cell containing a 1 is called a filled cell. Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally.
In the following grid, all cells marked X are connected to the cell marked Y.
XXX
XYX
XXX
If one or more filled cells are also connected, they form a region. Note that each cell in a region is connected to zero or more cells in the region but is not necessarily directly connected to all the other cells in the region.
Given an nxm matrix, find and print the number of cells in the largest region in the matrix. Note that there may be more than one region in the matrix.
For example, there are two regions in the following 3x3 matrix. The larger region at the top left contains 3 cells. The smaller one at the bottom right contains 1.
110
100
001

110
101
001

111
010
111
"""

# def solve(mat,i,j,n,m):
#     max_count = 0
#     count_so_far = 0
#     for i in range(n):
#         for j in range(m):
#             if mat[i][j] == 1:
#                 if (i-1>=0 and mat[i-1][j]==1) or (i+1<n and mat[i+1][j]==1) or (j-1>=0 and mat[i][j-1]==1) or (j+1<m and mat[i][j+1]==1) or (i-1>=0 and j-1>=0 and mat[i-1][j-1]==1) or (i-1>=0 and j+1<m and mat[i-1][j+1]==1) or (i+1<n and j+1 < m and mat[i+1][j+1] ==1) or (i+1<n and j-1>=0 and mat[i+1][j-1]==1):
#                     count_so_far+=1
#                 else:
#                     count_so_far = 1
#         max_count = max(max_count,count_so_far)
#     return max_count


# matrix = [[1,1,0],[1,0,0],[0,0,1]]

# res = solve(matrix,0,0,len(matrix),len(matrix[0]))
# print(res)


# matrix = [[1,1,1],[0,1,0],[1,1,1]]

# res = solve(matrix,0,0,len(matrix),len(matrix[0]))
# print(res)


# matrix = [[1,1,0],[1,0,1],[0,0,1]]

# res = solve(matrix,0,0,len(matrix),len(matrix[0]))
# print(res)

"""
1 1 1 0 1
0 0 1 0 0
1 1 0 1 0
0 1 1 0 0
0 0 0 0 0
0 1 0 0 0
0 0 1 1 0
"""

# matrix = [[1,1,1,0,1],[0,0,1,0,0],[1,1,0,1,0],[0, 1, 1, 0, 0],[0, 0, 0, 0, 0],[0, 1, 0, 0, 0],[0, 0, 1, 1, 0]]

# res = solve(matrix,0,0,len(matrix),len(matrix[0]))
# print(res)


# def solve(mat, n, m):
#     def is_valid(x, y):
#         return 0 <= x < n and 0 <= y < m and mat[x][y] == 1

#     def dfs(x, y):
#         stack = [(x, y)]
#         directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
#         count = 0
#         while stack:
#             i, j = stack.pop()
#             if mat[i][j] == 1:
#                 mat[i][j] = 0
#                 count += 1
#                 for dx, dy in directions:
#                     if is_valid(i + dx, j + dy):
#                         stack.append((i + dx, j + dy))
#         return count

#     max_count = 0
#     for i in range(n):
#         for j in range(m):
#             if mat[i][j] == 1:
#                 max_count = max(max_count, dfs(i, j))
#     return max_count

# matrix = [[1,1,1,0,1],[0,0,1,0,0],[1,1,0,1,0],[0, 1, 1, 0, 0],[0, 0, 0, 0, 0],[0, 1, 0, 0, 0],[0, 0, 1, 1, 0]]

# res = solve(matrix,len(matrix),len(matrix[0]))
# print(res)


def decorator(func):
    def wrapper():
        res = func()
        res = res.capitalize()
        res = res.split("/")
        return res

    return wrapper


@decorator
def hello():
    return "hello/world"


# print(hello())


"""
reverse a string by preserving the spaces example
input: "abc de"
output:"edc ba"
"""


def reverse1(ip):
    n = len(ip)
    space_idx = []
    for i in ip:
        if i == " ":
            space_idx.append(ip.index(i))
    # print(space_idx)
    ip_list = ip.split(" ")
    ip = [i for i in "".join(ip_list)]
    # print(ip)
    i = 0
    j = len(ip) - 1
    while i < j:
        ip[i], ip[j] = ip[j], ip[i]
        i += 1
        j -= 1
    ip = "".join(ip)
    # print(ip)
    for i in range(n):
        if i in space_idx:
            ip = ip[:i] + " " + ip[i:]
    # print(ip)
    return ip


input1 = "abc de"
# print(reverse1(input1))


# temp = {'name': ['abc','xyz'], 'age':[23,34]}

temp = {"name": ["abc", "xyz", 1, 4, 2, 3.5]}
temp2 = {"name": ["abc", "xyz", 1, 4, 2, 3.5, "filename", "star", 56]}
import pandas as pd

df = pd.DataFrame(temp)
df2 = pd.DataFrame(temp2)
# print(df)
# print(df2)

n2 = df2["name"].tolist()
n1 = df["name"].tolist()
n3 = [i for i in n2 if i not in n1]
# print(n3)
new_df = df2[df2["name"].isin(n3)]
# print(new_df)


list1 = [1, 2, 3, 4]

# print(list1)

a = list1[0:2]
# print(a)


def dec1(func):
    def wrapper():
        res = func()
        res = res.capitalize()
        res = res.split("/")
        return res

    return wrapper


# @dec1()
def test():
    return "test/123"


# print(test())


A = ["iron", "man", "one"]
String1 = "Hi I am Ironman and I can be maniron and Ironmanone"

# def print_index(ip, name):
#     new_list = []
#     for i in range(len(name)):
#         print(name[i])
#         for j in range(len(name)):
#             if i==j:
#                 continue
#             data = ''.join(name[0:j]) + name[i] + ''.join(name[j+1:])
#             print(data)

#     print(new_list)
#     print()

# res = {}
# for word in new_list:
#     n=len(word)
#     for i in range(len(ip)-n+1):
#         data = ip[i:i+n].lower()
#         # print(i,data,word.lower())
#         if data == word.lower():
#             if word in res:
#                 res[word].append(i)
#             else:
#                 res[word] = [i]
# print(res)
# print_index(String1, A)
