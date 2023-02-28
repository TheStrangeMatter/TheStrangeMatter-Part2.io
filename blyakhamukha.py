with open('26.txt') as f:
    k=1
    s=[int(x) for x in f]
    s.pop(0)
    s.sort(reverse=True)
    mini=s[0]
    for i in range(1, len(s)):
        if s[i]+3<=mini:
            k+=1
            mini=s[i]

print(k)
print(mini)
