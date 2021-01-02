import random


class RandomizedSet:

    # approach
    # hashtable - O(1) insert and delete
    # maintain a list with data -> but deleting the element is O(n)

    # to delete in O(1) -> we might need to swap the element with the last element and delete it

    # hashtable store data and index

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashtable = dict()
        self.datalist = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

        if val not in self.hashtable:
            self.datalist.append(val)
            self.hashtable[val] = len(self.datalist) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

        if val in self.hashtable:
            index = self.hashtable[val]
            lastelement = self.datalist[-1]

            self.datalist[index] = lastelement
            self.datalist.pop()

            self.hashtable[lastelement] = index
            del self.hashtable[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        n = len(self.datalist)
        randIndex = random.randint(0, n - 1)
        return self.datalist[randIndex]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()