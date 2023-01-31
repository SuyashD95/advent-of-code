"""
Advent of Code 2022
-------------------
Day 5: Supply Stacks (Part 1 Finished)

Part 1 (Finished):
    Question: After the rearrangement procedure completes, what crate
    ends up on top of each stack?
    Answer: FCVRLMVQP
"""
from io import TextIOWrapper

NO_CRATE = " "


def make_crates_matrix(puzzle_file: TextIOWrapper) -> list[list[str]]:
    """Utility function that builds a matrix of characters representing
    the crates placed in N stacks.

    Parameters
    ----------
    puzzle_file: An object representing textual content in file.

    Returns
    -------
    A list containing lists with each having a fixed number of characters.
    """
    crates_matrix = []
    while input_line := puzzle_file.readline()[:-1]:
        crate_layer = []
        for crate_char in input_line:
            if crate_char in ["[", "]"]:
                crate_char = NO_CRATE
            crate_layer.append(crate_char)
        crates_matrix.append(crate_layer)
    return crates_matrix


def create_movelist(puzzle_file: TextIOWrapper) -> list[dict[str, int]]:
    """Utility function that builds a list of dictionaries where each
    dictionary codefies the instruction for crane operator to move N crates
    from one stack to another stack.

    Parameters
    ----------
    puzzle_file: An object representing textual content in file.

    Returns
    -------
    A list of maps with each containing 3 key-value pairs: 'from_stack',
    'to_stack', and 'move_quantity'.
    """
    movelist = []
    while input_line := puzzle_file.readline()[:-1]:
        move_quantity, from_stack, to_stack = map(
            int,
            input_line.split(" ")[1::2]
        )
        movelist.append({
            "from_stack": from_stack,
            "to_stack": to_stack,
            "move_quantity": move_quantity
        })
    return movelist


def extract_crate_stacks(
        crates_matrix: list[list[str]]
) -> dict[int, list[str]]:
    """
    Utility function that finds and returns a mapped collection of
    stacks, each containing a set of crates such that the topmost crate is
    placed at the end of stack list.

    Parameters
    ----------
    crates_matrix: A matrix of characters representing the crates arranged
    in stacked fashion.

    Returns
    -------
    A dictionary where key represents the stack number and its value is a
    list of characters representing the crates arranged in ascending order
    where topmost crate is placed at the end of list.
    """
    crate_indices = []
    for index, element in enumerate(crates_matrix[-1]):
        if element != NO_CRATE:
            crate_indices.append(index)

    crate_stacks: dict[int, list[str]] = {}
    for stack_num, index in enumerate(crate_indices, start=1):
        crate_stacks[stack_num] = []
        for layer in crates_matrix[-2::-1]:
            if (crate := layer[index]) != NO_CRATE:
                crate_stacks[stack_num].append(crate)

    return crate_stacks


# -------------------------- PART ONE SOLUTION ---------------------------
def list_crates_at_top_of_rearranged_stacks(puzzle_input_filename: str) -> str:
    """Returns a string containing the name of crates that are placed at
    the top of the stacks after they are rearrangement procedure mentioned
    in the input file is performed.

    Parameters
    ----------
    puzzle_input_filename: Name of the file containing input dataset.

    Returns
    -------
    A string containing name of crates that are placed at top of stacks.
    """
    with open(puzzle_input_filename) as puzzle_file:
        crate_matrix = make_crates_matrix(puzzle_file)
        move_order_list = create_movelist(puzzle_file)
        crate_stacks = extract_crate_stacks(crate_matrix)

        for move_map in move_order_list:
            for _ in range(move_map["move_quantity"]):
                try:
                    top_crate = crate_stacks[move_map["from_stack"]].pop()
                except IndexError:
                    break
                crate_stacks[move_map["to_stack"]].append(top_crate)

        top_crate_list = []
        for stack in crate_stacks.values():
            top_crate_list.append(stack[-1])
    return "".join(top_crate_list)
# ------------------------------------------------------------------------


if __name__ == "__main__":
    puzzle_input_filename = "day-5-input.txt"
    print(
        "Day 5 Answers:\n"
        f"  Part 1: {list_crates_at_top_of_rearranged_stacks(puzzle_input_filename)}\n"
    )
