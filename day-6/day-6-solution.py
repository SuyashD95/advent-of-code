"""
Advent of Code 2022
-------------------
Day 6: Tuning Trouble (Part 1 Finished)

Part 1 (Completed):
    Question: How many characters need to be processed before the first
    start-of-packet marker is detected?
    Answer: 1034

Part 2 (Pending):
    Question: How many characters need to be processes before the first
    start-of-message marker is detected?
    Answer:
"""
from typing import Optional


# -------------------------- PART ONE SOLUTION ---------------------------
def characters_processed_to_find_start_marker(
    puzzle_input_filename: str,
) -> Optional[int]:
    """Returns the number of characters that were needed to be processed
    in the given datastream to detect the start-of-packet marker (which
    is a sequence of 4 characters that are all different).

    Parameters
    ----------
    puzzle_input_filename: Name of the file containing input dataset.

    Returns
    -------
    Number of characters processed before finding the start marker.
    """
    REQUIRED_UNIQUE_CHARS = 4

    with open(puzzle_input_filename) as puzzle_file:
        datastream = puzzle_file.read()[:-1]
        window_char_list = []
        for index, char in enumerate(datastream):
            if index < REQUIRED_UNIQUE_CHARS:
                window_char_list.append(char)
                continue
            if len(set(window_char_list)) == REQUIRED_UNIQUE_CHARS:
                return index
            else:
                window_char_list.pop(0)
                window_char_list.append(char)
# ------------------------------------------------------------------------


if __name__ == "__main__":
    puzzle_input_filename = "day-6-input.txt"
    print(
        "Day 6 Answers:\n"
        f"  Part 1: {characters_processed_to_find_start_marker(puzzle_input_filename)}\n"
    )
