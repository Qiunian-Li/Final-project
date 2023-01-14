import random
from priority_queue import PriorityQueue


def insert(k):
    PriorityQueue().insert(k)


def delMin(q):
    q.delMin()


def test_insert(benchmark):
    key = random.randint(1, 100)
    benchmark(insert, key)


def test_delMin(benchmark):
    q = PriorityQueue()
    q.insert(random.randint(1, 100))
    benchmark(delMin, q)

