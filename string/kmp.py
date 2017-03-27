def kmp(s, t, pos):
    i = pos
    j = 1
    while i <= s[0] and j <= t[0]:
        if (j==0 || s[i] == t[j]):
            i += 1
            j += 1
        else:
            j = 
