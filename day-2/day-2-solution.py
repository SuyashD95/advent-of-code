"""
Advent of Code 2022
-------------------
Day 2: Rock Paper Scissors

Part 1 (Pending):
    Question: What would your total score be if everything goes exactly
    according to your strategy guide?
    Answer:
"""
from _typeshed import ReadOnlyBuffer


LOSS_PTS = 0
DRAW_PTS = 3
WIN_PTS = 6

ROCK_PTS = 1
PAPER_PTS = 2
SCISSORS_PTS = 3

SCORING_SYSTEM = {
    "Rock": {
        "Rock": ROCK_PTS + DRAW_PTS,
        "Paper": ROCK_PTS + LOSS_PTS,
        "Scissors": ROCK_PTS + WIN_PTS
    },
    "Paper": {
        "Rock": PAPER_PTS + WIN_PTS,
        "Paper": PAPER_PTS + DRAW_PTS,
        "Scissors": PAPER_PTS + LOSS_PTS
    },
    "Scissors": {
        "Rock": SCISSORS_PTS + LOSS_PTS,
        "Paper": SCISSORS_PTS + WIN_PTS,
        "Scissors": SCISSORS_PTS + DRAW_PTS
    }
}


def part_1_solution(puzzle_input_filename: str) -> int:
    """Return the answer to the question asked in 1st puzzle based
    on the given input.
    """
    return 0


if __name__ == "__main__":
    print(f"Day 2 (Part 1) Answer: {part_1_solution('day-2-input.txt')}")
