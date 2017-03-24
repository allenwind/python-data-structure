#b进制
#a(n-1)...a(0) = a(n-1)*b^(n-1) + ... + a(0)*b^(0)
import string
s = string.digits + string.ascii_lowercase
def n_to_int(n, base):
    length = len(n)
    count = 0
    for i in n:
        i = int(i)
        count += i*base**(length-1)
        length -= 1
    return count

#10 translate n
 #divmod(x//y, x%y)
def int_to_n(d, n):
    result = ''
    while True:
        d, t = divmod(d, n)
        result += s[t]
        if d == 0:
            break
    return reversed(result)




