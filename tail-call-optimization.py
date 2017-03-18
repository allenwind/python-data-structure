"""
尾递归学习：
定义：一个函数最后一个动作是一个函数定义的情形
说明：函数调用的中间结果传入自身，调用，遇到结束情形返回结果


调用自身函数(Self-called)
计算仅占用常量栈空间(Stack Space)

语法上：

function foo(data) {
    a(data);
    return b(data);
}



"""

#example



def power(x, n):
    if n<=0:
        return 1
    return x * power(x, n-1)


def power_tail(x, n, t=1):
    if n<=0:
        return t
    return power(x, n-1, x*t)
