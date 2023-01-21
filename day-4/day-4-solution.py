"""
Advent of Code 2022
-------------------
Day 4: Camp Cleanup (Part 1 Finished)

Part 1 (Completed):
    Question: In how many assignment pairs does one range fully contain the other?
    Answer: 456

Part 2 (Pending):
    Question: In how many assignment pairs do the ranges overlap?
    Answer:
"""


# -------------------------- PART ONE SOLUTION ---------------------------
def is_one_range_subset_of_another_range(
        first_num_range: tuple[int, int],
        second_num_range: tuple[int, int]
        ) -> bool:
    """Returns True if the range of numbers represented by the one pair is a subset
    of the range numbers represented by the another pair.
    """
    first_range_min_num = first_num_range[0]
    first_range_max_num = first_num_range[1]
    second_range_min_num = second_num_range[0]
    second_range_max_num = second_num_range[1]

    if (
        first_range_min_num >= second_range_min_num
        and first_range_max_num <= second_range_max_num
    ):
        return True
    elif (
        second_range_min_num >= first_range_min_num
        and second_range_max_num <= first_range_max_num
    ):
        return True
    return False


def subset_assignment_pairs_count(puzzle_input_filename: str) -> int:
    """Returns the count of assignment pairs where one section (pair)
    is a subset of another pair or section.

    Parameters
    ----------
    puzzle_input_filename: Name of the file containing input dataset.
    """
    count = 0
    with open(puzzle_input_filename) as input_file:
        while pair_line := input_file.readline()[:-1]:
            first_section, second_section = pair_line.split(",")
            first_num_range = first_section.split("-")
            first_num_range = (
                int(first_num_range[0]),
                int(first_num_range[1]),
            )
            second_num_range = second_section.split("-")
            second_num_range = (
                int(second_num_range[0]),
                int(second_num_range[1]),
            )
            if is_one_range_subset_of_another_range(
                first_num_range, second_num_range
            ):
                count += 1
    return count
# ------------------------------------------------------------------------


# -------------------------- PART TWO SOLUTION ===========================
def count_overlapping_ranges(puzzle_input_filename: str) -> int:
    """Returns the count of pairs where the two given number ranges overlap
    with one another i.e., some of the numbers between the two ranges are
    the same.

    Parameters
    ----------
    puzzle_input_filename: Name of the file containing input dataset.
    """
    count = 0
    with open(puzzle_input_filename) as input_file:
        while pair_line := input_file.readline()[:-1]:
            first_section, second_section = pair_line.split(",")
            first_num_range = first_section.split("-")
            first_num_range = (
                int(first_num_range[0]),
                int(first_num_range[1]),
            )
            second_num_range = second_section.split("-")
            second_num_range = (
                int(second_num_range[0]),
                int(second_num_range[1]),
            )
    return count
# ========================================================================


if __name__ == "__main__":
    puzzle_input_filename = "day-4-input.txt"
    print(
        "Day 4 Answers:\n"
        f"  Part 1: {subset_assignment_pairs_count(puzzle_input_filename)}\n"
    )
