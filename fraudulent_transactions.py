from typing import Optional
from pydantic import BaseModel

class FraudTransact:
    def __init__(self,):
        pass

    class Input(BaseModel):
        inputs: Optional[Optional[list]] = None

    class Output(BaseModel):
        answer: Optional[list] = None

    def cyclic(self,g):
        """Return True if the directed graph g has a cycle.
        g must be represented as a dictionary mapping vertices to
        iterables of neighbouring vertices. For example:

        >>> cyclic({1: (2,), 2: (3,), 3: (1,)})
        True
        >>> cyclic({1: (2,), 2: (3,), 3: (4,)})
        False

        """
        path = set()

        def visit(vertex):
            path.add(vertex)
            for neighbour in g.get(vertex, ()):
                if neighbour in path or visit(neighbour):
                    return True
            path.remove(vertex)
            return False

        return not any(visit(v) for v in g)

    # @staticmethod
    def solve(self,input):
        ans= ["Ineligible", "Eligible"]
        graph = {}
        for t in input:
            s,e = list(map(int,t.split(' ')))
            if s != e:
                if s in graph:
                    graph[s].append(e)
                else:
                    graph[s] = [e]

        # print()
        

        return ans[int(self.cyclic(graph))]
                