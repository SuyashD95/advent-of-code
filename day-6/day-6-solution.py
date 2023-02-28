"""
Advent of Code 2022
-------------------
Day 6: Tuning Trouble (Finished)

Part 1 (Completed):
    Question: How many characters need to be processed before the first
    start-of-packet marker is detected?
    Answer: 1034

Part 2 (Completed):
    Question: How many characters need to be processes before the first
    start-of-message marker is detected?
    Answer: 2472
-------------------

Author: Suyash Dayal
Originally Completed On: 28th February 2023
"""
from typing import Optional
from collections import deque


def char_count_till_end_of_unique_substring(
    base_string: str,
    unique_substr_length: int
) -> Optional[int]:
    """Returns the number of characters that were required to be searched to
    find a substring from the provided string where each character is
    different.

    Parameters
    ----------
    base_string: The original string to be searched.
    unique_substr_length: A natural number greater than 1, representing the
    length of the unique substring.

    Returns
    -------
    Returns no. of characters that were processed in the base string to find
    a substring of the provided length, where each character is different.

    In case, no substring is found to be satisfying the uniqueness criterion,
    the function returns `None`.
    """
    substr_window = deque(maxlen=unique_substr_length)
    for index, char in enumerate(base_string):
        if index < unique_substr_length:
            substr_window.append(char)
            continue
        if len(set(substr_window)) == unique_substr_length:
            return index
        else:
            substr_window.popleft()
            substr_window.append(char)

    if len(set(substr_window)) == unique_substr_length:
        return len(base_string)


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
        return char_count_till_end_of_unique_substring(
            datastream, REQUIRED_UNIQUE_CHARS
        )
# ------------------------------------------------------------------------


# -------------------------- PART TWO SOLUTION ---------------------------
def chars_counted_to_find_start_of_message_marker(
    puzzle_input_filename: str,
) -> Optional[int]:
    """Returns the number of characters that were needed to be processed
    in the given datastream to detect the start-of-message marker (which
    is a sequence of 14 characters that are all different).

    Parameters
    ----------
    puzzle_input_filename: Name of the file containing input dataset.

    Returns
    -------
    Number of characters processed before finding the start-of-message marker.
    """
    REQUIRED_UNIQUE_CHARS = 14

    with open(puzzle_input_filename) as puzzle_file:
        datastream = puzzle_file.read()[:-1]
        return char_count_till_end_of_unique_substring(
            datastream, REQUIRED_UNIQUE_CHARS
        )
# ------------------------------------------------------------------------


if __name__ == "__main__":
    puzzle_input_filename = "day-6-input.txt"
    print(
        "Day 6 Answers:\n"
        f"  Part 1: {characters_processed_to_find_start_marker(puzzle_input_filename)}\n"
        f"  Part 2: {chars_counted_to_find_start_of_message_marker(puzzle_input_filename)}\n"
    )
