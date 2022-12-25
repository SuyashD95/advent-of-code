"""
Advent of Code 2022
-------------------
Day 1: Calorie Counting (Finished)

Part 1 (Completed):
    Question: Find the Elf carrying the most Calories. How many total
    Calories is that Elf carrying?
    Answer: 72017

Part 2 (Completed):
    Question: Find the top three Elves carrying the most Calories. How
    many Calories are those Elves carrying in total?
    Answer: 212520
-------------------

Author: Suyash Dayal
Orignally Completed On: 24th December 2022
"""


# -------------------------- PART 1 SOLUTION -----------------------------
def find_max_calories(filename: str) -> int:
    """Returns the maximum calories that is carried by an elf."""
    NEWLINE_CHAR = "\n"

    max_calories = 0
    current_elf_calories = 0
    with open(filename, "r") as file:
        while line_of_text := file.readline():
            if (line_of_text != NEWLINE_CHAR):
                calories = int(line_of_text)
                current_elf_calories += calories
            else:
                max_calories = max(max_calories, current_elf_calories)
                current_elf_calories = 0
    max_calories = max(max_calories, current_elf_calories)

    return max_calories
# ------------------------------------------------------------------------


# --------------------------- PART 2 SOLUTION ----------------------------
def set_max_calories(max_3_calories: list[int], calorie_candidate: int):
    """A helper function that is used for filling the provided
    tuple based on given calorie value.
    """
    LARGEST = 0
    SECOND_LARGEST = 1
    THIRD_LARGEST = 2

    if calorie_candidate > max_3_calories[LARGEST]:
        max_3_calories[THIRD_LARGEST] = max_3_calories[SECOND_LARGEST]
        max_3_calories[SECOND_LARGEST] = max_3_calories[LARGEST]
        max_3_calories[LARGEST] = calorie_candidate
    elif calorie_candidate > max_3_calories[SECOND_LARGEST]:
        max_3_calories[THIRD_LARGEST] = max_3_calories[SECOND_LARGEST]
        max_3_calories[SECOND_LARGEST] = calorie_candidate
    elif calorie_candidate > max_3_calories[THIRD_LARGEST]:
        max_3_calories[THIRD_LARGEST] = calorie_candidate


def sum_of_3_highest_calories(filename: str) -> int:
    """Returns the total calories carried by 3 elfs carrying the
    largest amount of calories in the journey.
    """
    max_3_calories = [0, 0, 0]
    current_elf_calories = 0

    with open(filename, "r") as file:
        while calorie_line := file.readline():
            if (calorie_line != "\n"):
                calories = int(calorie_line)
                current_elf_calories += calories
            else:
                set_max_calories(max_3_calories, current_elf_calories)
                current_elf_calories = 0
    set_max_calories(max_3_calories, current_elf_calories)

    return sum(max_3_calories)
# ------------------------------------------------------------------------


if __name__ == "__main__":
    puzzle_input_filename = "day-1-input.txt"
    print("Day 1 Answers:")
    print(f"\tPart 1: {find_max_calories(puzzle_input_filename)}")
    print(f"\tPart 2: {sum_of_3_highest_calories(puzzle_input_filename)}")
