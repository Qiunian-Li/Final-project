import os
from priority_queue import PriorityQueue
from graphviz import Digraph


def convert_to_digraph(tree):
    dot = Digraph(comment='Tree Structure')
    edges = []
    for i in range(tree.size):
        dot.node(f'{i}', f'{tree.find(i)}')
        lc_pos = 2 * i + 1
        rc_pos = 2 * i + 2
        if lc_pos < tree.size:
            dot.node(f'{lc_pos}', f'{tree.find(lc_pos)}')
            edges.append(f"{i}{lc_pos}")
        if rc_pos < tree.size:
            dot.node(f'{rc_pos}', f'{tree.find(rc_pos)}')
            edges.append(f"{i}{rc_pos}")
    dot.edges(edges)
    return dot


if __name__ == '__main__':
    os.environ['PATH'] = os.pathsep + r'D:\soft\Graphviz\bin'
    q = PriorityQueue()
    data = [9, 5, 6, 2, 3]
    for ele in data:
        q.insert(ele)
    dot_data = convert_to_digraph(q.heap)
    dot_data.render('./Tree-Structure.gv', view=True)


