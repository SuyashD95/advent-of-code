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


def is_1st_pair_subset_of_2nd_pair(
        first_pair: tuple[int, int],
        second_pair: tuple[int, int]
        ) -> bool:
    """Returns True if the range of numbers represented by the first pair is a subset
    of the range numbers represented by the second pair.
    """
    first_pair_low_bound = first_pair[0]
    first_pair_high_bound = first_pair[1]
    second_pair_low_bound = second_pair[0]
    second_pair_high_bound = second_pair[1]

    if (
        first_pair_low_bound >= second_pair_low_bound
        and first_pair_high_bound <= second_pair_high_bound
    ):
        return True
    return False


def is_2nd_pair_subset_of_1st_pair(
        first_pair: tuple[int, int],
        second_pair: tuple[int, int]
        ) -> bool:
    """Returns True if the range of numbers represented by the second pair is
    a subset of the range numbers represented by the first pair pair.
    """
    first_pair_low_bound = first_pair[0]
    first_pair_high_bound = first_pair[1]
    second_pair_low_bound = second_pair[0]
    second_pair_high_bound = second_pair[1]

    if (
        second_pair_low_bound >= first_pair_low_bound
        and second_pair_high_bound <= first_pair_high_bound
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
            first_pair = first_section.split("-")
            first_pair = (int(first_pair[0]), int(first_pair[1]),)
            second_pair = second_section.split("-")
            second_pair = (int(second_pair[0]), int(second_pair[1]),)
            if (
                is_1st_pair_subset_of_2nd_pair(first_pair, second_pair)
                or is_2nd_pair_subset_of_1st_pair(first_pair, second_pair)
            ):
                count += 1
    return count


if __name__ == "__main__":
    puzzle_input_filename = "day-4-input.txt"
    print(
        "Day 4 Answers:\n"
        f"  Part 1: {subset_assignment_pairs_count(puzzle_input_filename)}\n"
    )
