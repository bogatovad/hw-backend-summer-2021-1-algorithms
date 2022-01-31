from collections import deque
from tkinter import N
from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        res:list[Node] = []
        searched = []
        res.append(self._root)
        searched.append(self._root)
        def dfs_(res, searched, node):
            for u in node.outbound:
                if not u in searched:
                    searched.append(u)
                    res.append(u)
                    dfs_(res, searched, u)
        
        dfs_(res, searched, self._root)
        return res

    def bfs(self) -> list[Node]:
        res:list[Node] = []
        search_queue:deque = deque()
        search_queue.append(self._root)
        search_queue += self._root.outbound
        searched = []
        
        while search_queue:
            node_ = search_queue.popleft()
            if not node_ in searched:
                
                search_queue += node_.outbound
                searched.append(node_)
                res.append(node_)
        
        return res

            


