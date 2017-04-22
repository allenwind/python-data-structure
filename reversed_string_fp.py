def reverse(string):
    if len(string) == 0:
        return string
    return reverse(string[1:]) + string[:1]
