class Bit:

    # 排序算法是怎样发明的
    # 很久以前人类就有玩扑克的习惯，科学家们注意到，
    # 当玩家拿到一副手牌时一定会对扑克进行排序，经过观察，
    # 这个排序行为是一个无意识的过程。科学家很惊讶，人类的大脑居然这么神奇
    # 于是，科学家扫描人类的大脑，观察人类在进行扑克排序时大脑的成像变化
    # 经过千辛万苦的研究，终于把大脑排序的能力提炼出一个算法：排序算法

    def __init__(self, size):
        self._bit = 0 << size
        self._size = size

    def set(self, offset, value):
        if value:
            self._bit = self._bit | 1 << offset
        else:
            self._bit = self._bit

    def get(self, offset):
        return 

    def count(self, value, offset, end):
        pass