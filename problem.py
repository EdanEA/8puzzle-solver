from typing_extensions import Self
from eight import Eight

class Node:
    def __init__(self, state: str, parent: Self | None = None, path_cost: int = 0, action: str | None = None):
        self.state = state
        self.path_cost = path_cost
        self.action = action
        self.parent = parent
        self.path = []
        self.base = self.from_state()

    def from_state(self) -> Eight:
        return Eight(self.state)

class Problem:
    def __init__(self, initial: Node, goal: str):
        self.initial = initial
        self.goal = goal

    def is_goal(self, state: str) -> bool:
        return state == self.goal

    def result(self, state: Node, action: str) -> Node:
        res = Node(state.state, state, state.path_cost + 1, action)

        res.base.move(action)
        res.state = res.base.order

        return res
