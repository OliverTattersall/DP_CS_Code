
def sym_list(lst):

    lst2 = lst.copy()[::-1]
    return lst+lst2

print(sym_list([1,2,3]))
