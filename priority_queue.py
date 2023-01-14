# singly linked list node
class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next


# A complete binary tree ADT based on a singly linked list
class BinaryTree:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, key):
        newest = Node(key, None)
        if self.tail is None:
            self.tail = newest
            self.head = newest
        else:
            self.tail.next = newest
            self.tail = newest
        self.size += 1

    def get_parent(self, i):
        if i == 0:
            return None
        return self.find((i - 1) // 2)

    def get_left_child(self, i):
        return self.find(2 * i + 1)

    def get_right_child(self, i):
        return self.find(2 * i + 2)

    def del_min(self):
        if self.size == 0:
            return None
        retval = self.find(0)
        self.__swap(self.head, self.tail)
        self.__del_tail()
        self.size -= 1
        self.perc_down(0)
        return retval

    def perc_up(self):
        i = self.size - 1
        while (i - 1) // 2 >= 0:
            node_i = self.__find_node(i)
            node_p = self.__find_node((i - 1) // 2)
            if node_i.key < node_p.key:
                self.__swap(node_p, node_i)
            i = (i - 1) // 2

    def perc_down(self, i):
        while (i * 2 + 1) <= self.size - 1:
            mc_pos = self.__find_min_child(i)
            node_mc = self.__find_node(mc_pos)
            node_i = self.__find_node(i)
            if node_i.key > node_mc.key:
                self.__swap(node_i, node_mc)
            i = mc_pos

    def __del_tail(self):
        if self.size == 1:
            self.tail = None
            return
        new_tail = self.__find_node(self.size - 2)
        new_tail.next = None
        self.tail = new_tail

    def __find_min_child(self, i):
        if i * 2 + 2 > self.size - 1:
            return i * 2 + 1
        else:
            if self.get_left_child(i) < self.get_right_child(i):
                return i * 2 + 1
            else:
                return i * 2 + 2

    @staticmethod
    def __swap(ni, nj):
        tmp = nj.key
        nj.key = ni.key
        ni.key = tmp

    def __find_node(self, i):
        if self.head is None:
            return None
        curr = self.head
        if i == 0:
            return curr
        pos = 0
        while curr.next:
            curr = curr.next
            pos += 1
            if pos == i:
                return curr
        return None

    def find(self, i):
        res = self.__find_node(i)
        if res:
            return res.key
        return None


# a minimum priority queue based on the complete binary tree
class PriorityQueue:
    def __init__(self):
        self.heap = BinaryTree()

    def insert(self, k):
        self.heap.add(k)
        self.heap.perc_up()

    def delMin(self):
        return self.heap.del_min()


if __name__ == '__main__':
    # 9,5,6,2,3
    queue = PriorityQueue()
    data = [9, 5, 6, 2, 3]
    for ele in data:
        queue.insert(ele)
    print(queue.delMin())
    print(queue.delMin())
    print(queue.delMin())
    print(queue.delMin())
    print(queue.delMin())


