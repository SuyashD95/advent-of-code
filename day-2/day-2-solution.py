"""
Advent of Code 2022
-------------------
Day 2: Rock Paper Scissors

Part 1 (Completed):
    Question: What would your total score be if everything goes exactly
    according to your strategy guide?
    Answer: 10941

Part 2 (Pending):
    Question: What would your total score be if everything goes exactly
    according to your strategy guide (following the correction made for
    decoding the second column)?
    Answer:
"""

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


def _opponent_column_decoder(guide_char: str):
    """Return the string describing the object that was represented
    by the given character.

    Mappings:
        A -> Rock
        B -> Paper
        C -> Scissors

    Parameters
    ----------
    guide_char: The character present in the right hand column of puzzle input.

    Raises
    ------
    ValueError: Invalid value was provided.
    """
    if guide_char == "A":
        return "Rock"
    elif guide_char == "B":
        return "Paper"
    elif guide_char == "C":
        return "Scissors"
    else:
        raise ValueError(
            "Invalid `guide_char` value was passed. Valid values are 'A', "
            "'B' & 'C'."
        )


# -------------------------- PART 1 SOLUTION -----------------------------
def _player_column_decoder(guide_char: str):
    """Return the string describing the object that was represented
    by the given character.

    Mappings:
        X -> Rock
        Y -> Paper
        Z -> Scissors

    Parameters
    ----------
    guide_char: The character present in the right hand column of puzzle input.

    Raises
    ------
    ValueError: Invalid value was provided.
    """
    if guide_char == "X":
        return "Rock"
    elif guide_char == "Y":
        return "Paper"
    elif guide_char == "Z":
        return "Scissors"
    else:
        raise ValueError(
            "Invalid `guide_char` value was given. Valid values are 'X', "
            "'Y' & 'Z'."
        )


def calculate_guide_total_score(puzzle_input_filename: str) -> int:
    """Returns the total score based on the set of inputs provided in
    the provided file, according to the rules of the game.

    Parameters
    ----------
    puzzle_input_filename: Name of the file containing puzzle's input dataset.
    """
    total_score = 0

    with open(puzzle_input_filename) as puzzle_file:
        while file_line := puzzle_file.readline():
            left_col_char, right_col_char = file_line.split()
            opponent_game_obj = _opponent_column_decoder(left_col_char)
            player_game_obj = _player_column_decoder(right_col_char)
            round_score = SCORING_SYSTEM[player_game_obj][opponent_game_obj]
            total_score += round_score

    return total_score
# ------------------------------------------------------------------------


# -------------------------- PART 2 SOLUTION -----------------------------
def find_guide_total_score(puzzle_input_filename: str) -> int:
    """Returns the total score based on the set of inputs provided in
    the provided file, according to the rules of the game.

    Parameters
    ----------
    puzzle_input_filename: Name of the file containing puzzle's input dataset.
    """
    total_score = 0

    with open(puzzle_input_filename) as puzzle_file:
        pass

    return total_score
# ------------------------------------------------------------------------


if __name__ == "__main__":
    puzzle_input_filename = "day-2-input.txt"
    print("Day 2 Answers:")
    print(f"\tPart 1: {calculate_guide_total_score(puzzle_input_filename)}")
    print(f"\tPart 2: {find_guide_total_score(puzzle_input_filename)}")
