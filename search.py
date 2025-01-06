from typing_extensions import Callable
from problem import Node, Problem

def best_first_search(problem: Problem, eval: Callable[[Node, str], int], sub_eval: Callable[[Node, str], int] | None = None, path_limit = 2 ** 32):
    node = problem.initial
    init_eval = 0

    if sub_eval is not None:
        init_eval = eval(node, problem.goal) + sub_eval(node, problem.goal)
    else:
        init_eval = eval(node, problem.goal)

    frontier: list[tuple[int, Node]] = [ (init_eval, node) ]
    reached: dict[str, Node] = { node.state: node }

    while len(frontier) > 0:
        t_priority, next = frontier.pop(0)

        if(next.path_cost > path_limit):
            continue

        if problem.is_goal(next.state):
            return next

        child_list = expand(problem, next)

        for child in child_list:
            s = child.state
            s_not_reached = True

            if s in reached.keys():
                s_not_reached = False

            if s_not_reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                priority = 0

                if sub_eval is None:
                    priority = eval(child, problem.goal)
                else:
                    priority = eval(child, problem.goal) + sub_eval(child, problem.goal)

                frontier.append((priority, child))
                frontier.sort(key = priority_sort)

    return Node("000000000", None, -1, None)

# so much memory usage
# visited = {}

def expand(problem: Problem, node: Node) -> list[Node]:
    # if node.state not in visited.keys():
    #     visited[node.state] = 1
    # else:
    #     visited[node.state] += 1

    moves = node.base.available_moves()
    output = []

    for move in moves:
        new_node = problem.result(node, move)

        if new_node.parent is not None and new_node.parent.parent is not None and new_node.parent.parent.state == new_node.state:
            continue

        output.append(new_node)

    return output

def priority_sort(tup: tuple[int, Node]):
    return tup[0]

# ineffective and probable wasteful heuristic
def num_out_of_place(node: Node, goal: str):
    state = node.state
    count = 0

    for i in range(0, 9):
        if state[i] != goal[i]:
            count += 1

    return count

# somewhat better than above
def manhattan(node: Node, goal: str) -> int:
    out = 0

    for i in range(0, 9):
        out += node.base.distance_from_expected(i, goal)

    return out
