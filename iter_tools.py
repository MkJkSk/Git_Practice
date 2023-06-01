from itertools import permutations

def generate_permutations(lst):
    my_perm = list(permutations(lst))
    return my_perm


my_list=[1,2,3]
result=generate_permutations(my_list)
for perm in result:
    print(perm)
