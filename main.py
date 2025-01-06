import sqlite3
from time import time
from threading import Thread
from multiprocessing import Process

from eight import Eight
from search import best_first_search, manhattan, num_out_of_place
from problem import Node, Problem

goal = "123456780"

def run_agent() -> None:
    while True:
        try:
            con = sqlite3.connect("solutions.db")
            break
        except sqlite3.OperationalError:
            continue

    running = True
    while running:
        try:
            db = con.cursor()
            res = db.fetchone()

            base = Eight(expected=goal)

            if base.unsolvable():
                print(f"{base.order}: unsolvable, skipping\n")
                continue

            db.execute(f"SELECT * FROM eight WHERE start_state={base.order} AND goal_state={goal}")
            if res is None:
                print(f"{base.order}")

                final = best_first_search(Problem(Node(base.order), goal), manhattan, sub_eval=None, path_limit=32)
                output = []

                while final.parent is not None:
                    output.insert(0, final.action)
                    final = final.parent

                print(f"{output}")
                print()

                exists = len(output) != 0

                db.execute(f"INSERT INTO eight (start_state, goal_state, solution, sol_exists, sol_cost) VALUES ({base.order}, {goal}, \"{str(output)}\", {exists}, {len(output)})")
                con.commit()
            else:
                print(f"{res[0]} | {res[1]}")
                print(f"{res[2]}")
        except KeyboardInterrupt:
            running = False

    return

if __name__ == "__main__":
    start = time()
    run_agent()
    end = time()

print(f"total runtime: {(end - start) / 60:.2f} minutes")
