# determind if string 1 is a permutation of string2





# NlogN with sort
def permutation1(s1,s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

def perumation2(s1,s2):
    if len(s1) != len(s2):
        return False
    maps1 = {}
    for i in s1:
        if i not in maps1:
            maps1[i] = 1
        else:
            maps1[i] += 1
    maps2 = {}
    for i in s1:
        if i not in maps2:
            maps2[i] = 1
        else:
            maps2[i] += 1
    return maps1 == maps2



print(perumation2("123ss","32ss1"))
