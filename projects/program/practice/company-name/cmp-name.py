# import itertools
# lst = ['pros']
# combinatorics = itertools.product([True, False], repeat=len(lst) - 1)
#
# solution = []
# for combination in combinatorics:
#     i = 0
#     one_such_combination = [lst[i]]
#     for slab in combination:
#         i += 1
#         if not slab: # there is a join
#             one_such_combination[-1] += lst[i]
#         else:
#             one_such_combination += [lst[i]]
#     solution.append(one_such_combination)
#
# print(solution)


# --------------------------------------------------
# from itertools import combinations
# a = ['p', 'r', 'o', 's']
# a = "".join(a)
# cuts = []
# for i in range(0,len(a)):
#     cuts.extend(combinations(range(1,len(a)),i))
# for i in cuts:
#     last = 0
#     output = []
#     for j in i:
#         output.append(a[last:j])
#         last = j
#     output.append(a[last:])
#     print(output)

# --------------------------------------------------
# def split_combinations(L):
#     for split in range(1, len(L)):
#         for combination in split_combinations(L[split:]):
#             yield [L[:split]] + combination
#     yield [L]
#
# print (list(split_combinations('abcd')))

# --------------------------------------------------
# from itertools import combinations
# def split_string(s, t):
#     return [s[start:finish] for start, finish in zip((None, ) + t, t + (None, ))]
#
# def split_combinations(s):
#     for i in range(len(s)):
#         for split_points in combinations(range(1, len(s)), i):
#             yield split_string(s, split_points)
# split_combinations('pro')

# --------------------------------------------------
'''
sohoj hok prithibir kaj
prithibir kajgulo sohoj koray amader lokkho
prithibi automated hok -> The world is automatic

manus noy, jontro kaj koruk. -> People do not work, machines work
kaj hok soshoj -> work is easy
jibon hok soshoj and sundor -> Life is easy and beautiful
jibonke soshoj koro -> Making life easier
jibonke sohoj kore tola -> Making life easier
jibonke soshoj koray amader lokkho -> Our goal is to make life easier
jobonke dekhar somoy ber koro -> Find out the time of life
device thakte manus keno. -> Why are people staying in the appliance?
'''
# --------------------------------------------------
# A Python program to print all
# permutations using library function
from itertools import permutations

# Get all permutations of [1, 2, 3]
perm = permutations([])

# Print the obtained permutations
for i in perm:
    print(i)

# --------------------------------------------------
# Python function to print permutations of a given list
# def permutation(lst):
#     # If lst is empty then there are no permutations
#     if len(lst) == 0:
#         return []
#
#         # If there is only one element in lst then, only
#     # one permuatation is possible
#     if len(lst) == 1:
#         return [lst]
#
#         # Find the permutations for lst if there are
#     # more than 1 characters
#
#     l = []  # empty list that will store current permutation
#
#     # Iterate the input(lst) and calculate the permutation
#     for i in range(len(lst)):
#         m = lst[i]
#
#         # Extract lst[i] or m from the list.  remLst is
#         # remaining list
#         remLst = lst[:i] + lst[i + 1:]
#
#         # Generating all permutations where m is first
#         # element
#         for p in permutation(remLst):
#             l.append([m] + p)
#     return l
#
#
# # Driver program to test above function
# data = list('123')
# for p in permutation(data):
#     print
#     p

# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------