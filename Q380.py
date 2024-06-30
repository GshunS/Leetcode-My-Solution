# 380. Insert Delete GetRandom O(1)
import random


class RandomizedSet(object):

    def __init__(self):
        self.a_dict = {}
        self.a_list = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.a_dict:
            return False
        self.a_list.append(val)
        self.a_dict[val] = len(self.a_list) - 1
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.a_dict:
            current_index = self.a_dict[val]
            self.a_dict[self.a_list[-1]] = current_index

            self.a_list[current_index], self.a_list[-1] = self.a_list[-1], self.a_list[current_index]
            self.a_list.pop()

            del self.a_dict[val]
            return True
        return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.a_list)

obj = RandomizedSet()
