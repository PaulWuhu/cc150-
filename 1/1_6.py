# string compression
# aabcccccaaa ------->a2b1c5a3
# if the compressed string would not bevome smaller than the orginal string, you return the orginal string

def string_compression(s):
    ans = ""
    i = 0
    t = 0
    while i < len(s)-1:
        if s[i]==s[i+1]:
            t += 1
        if i == len(s)-2:
            t += 1
            ans += s[i]
            ans += str(t)
        elif s[i]!=s[i+1]:
            t += 1
            ans += s[i]
            ans += str(t)
            t=0
        i += 1
    if len(s) == 1:
        return f"1{s}"
    if len(ans)<len(s):
        return ans
    return s

print(string_compression("b"))
