from collections import defaultdict

#列表的谓词分组

class PList(list):

    def partition(self, *funcs):
        parts = defaultdict(list)
        for item in self:
            for func in funcs:
                result = func(item)
                if result:
                    parts[func.__name__].append(item)
                    break
        return tuple(parts.values())

if __name__ == '__main__':
    p = PList([1, 2, 3, 4])

    def isEvent(i):
        if i % 2 == 0:
            return True

    def isNotEvent(i):
        if i % 2 != 0:
            return True

    result = p.partition(isEvent, isNotEvent)
        
        
