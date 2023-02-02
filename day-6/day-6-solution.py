"""
Advent of Code 2022
-------------------
Day 6: Tuning Trouble (Pending)

Part 1 (Pending):
    Question: How many characters need to be processed before the first
    start-of-packet marker is detected?
    Answer:
"""


def characters_processed_to_find_start_market(
    puzzle_input_filename: str
) -> int:
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
    return 0


if __name__ == "__main__":
    puzzle_input_filename = "day-6-input.txt"
    print(
        "Day 6 Answers:\n"
        f"  Part 1: {characters_processed_to_find_start_market(puzzle_input_filename)}\n"
    )
