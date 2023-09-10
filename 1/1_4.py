# palindrome permutaion

def palindrome(s):
    odd = 0
    maps ={}
    news = s.lower().replace(" ","")
    for i in news:
        if i in maps:
            maps[i] += 1
        else:
            maps[i] =1
    for i,j in maps.items():
        if j %2 !=0:
            odd += 1
    return odd <=1

print(palindrome("tacT coa"))
