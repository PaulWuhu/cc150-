# URLify


# replace white sapcee in the string with %20
def Urlift(s):
    news =""
    for i in s.strip():
        if i == " ":
            news += "%20"
        else:
            news+= i
    return news

print(Urlift("Mr John Smith        "))
