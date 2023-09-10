# oneway
# if a character can be added remove or replace and two string is the same, we return ture

def oneway(s1,s2):
    # loop through the first string and put the character in the map
    # loop through 2nd string and
    if s1 == s2:
        return True
    indx1 = 0
    indx2 = 0
    dif = False
    while indx1<len(s1) and indx2<len(s2):
        if s1[indx1] == s2[indx2]:
            indx1 += 1
            indx2 += 1
        elif s1[indx1] != s2[indx2]:
            if dif:
                return False
            dif = True
            if len(s1) == len(s2):
                indx1 += 1
                indx2 += 1
            elif len(s1)<len(s2):
                indx2 += 1
            else:
                indx1+=1
    return True

print(oneway("pale","bales"))
