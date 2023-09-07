# determind if a string only have unquine character, without extra dataset


# using data structure

def unquine(s):
    maps = {}
    for i in s:
        if i in maps:
            return False
        if i not in maps:
            maps[i] = 1
            print(i)

    return True

def unquine2(s):
    sorted(s)
    for i in range(len(s)-2):
        if s[i] == s[i+1]:
            return False
    return True

print(unquine2("asd"))
print(unquine2("hello"))
