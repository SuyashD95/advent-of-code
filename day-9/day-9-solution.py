"""
Advent of Code 2022
-------------------
Day 9: Rope Bridge (Pending)

Part 1 (Pending):
    Question: Simulate your complete hypothetical series of motions. How many
    positions does the tail of the rope visit at least once?
    Answer:
-------------------

Author: Suyash Dayal
"""
import math

MOVE_UNIT = 1


def extract_direction_and_distance(input_line: str) -> tuple[str, int]:
    """Extracts the direction and distance from the input line.

    Parameters
    ----------
    input_line: Input line containing the direction and distance.

    Returns
    -------
    Returns a tuple containing the direction and distance.
    """
    return input_line[0], int(input_line[1:])


def calculate_line_segment_length(
        start_position: tuple[int, int],
        end_position: tuple[int, int]
) -> int:
    """Calculates the length of the line segment between the start and end
    positions.

    Parameters
    ----------
    start_position: The starting position of the line segment.
    end_position: The ending position of the line segment.

    Returns
    -------
    Returns an integer representing the length of the line segment.
    """
    return math.sqrt((end_position[0] - start_position[0]) ** 2 + (end_position[1] - start_position[1]) ** 2)


def get_rope_tail_position(
        new_head_position: tuple[int, int],
        old_head_position: tuple[int, int],
        current_tail_position: tuple[int, int],
) -> tuple[int, int]:
    """Returns the position of the rope tail after the rope head moves.

    Parameters
    ----------
    new_head_position: The new position of the rope head.
    old_head_position: The old position of the rope head.
    current_tail_position: The current position of the rope tail.

    Returns
    -------
    Returns the new position of the rope tail.
    """
    distance_between_head_and_tail = calculate_line_segment_length(
        start_position=new_head_position,
        end_position=current_tail_position
    )
    if distance_between_head_and_tail <= 1:
        return current_tail_position
    else:
        return old_head_position


def populate_tail_positions_map(
    start_position: tuple[int, int],
    head_movement_instructions: list[tuple[int, int]]
) -> dict[int, set[int]]:
    """Populates the visited positions map with the positions visited by the
    rope tail.

    Parameters
    ----------
    start_position: The starting position of both rope's head and tail knots.
    head_movement_instructions: The list of movement instructions for the rope head.

    Returns
    -------
    Returns a dictionary containing the positions visited by the rope
    tail. The key is the x-coordinate and the value is a set of y-coordinates.

    Raises
    ------
    ValueError: If an invalid move direction is encountered.
    """
    head_knot_position = start_position
    current_tail_position = start_position
    tail_knot_positions = {start_position[0]: {start_position[1]}}
    for move_direction, move_distance in head_movement_instructions:
        if move_direction == "U":
            for _ in range(move_distance):
                new_head_position = (head_knot_position[0], head_knot_position[1] + MOVE_UNIT)
                new_tail_position = get_rope_tail_position(
                    new_head_position,
                    head_knot_position,
                    current_tail_position
                )
                if new_tail_position not in tail_knot_positions:
                    tail_knot_positions[new_tail_position[0]] = {new_tail_position[1]}
                else:
                    tail_knot_positions[new_tail_position[0]].add(new_tail_position[1])
        elif move_direction == "D":
            new_head_position = (head_knot_position[0], head_knot_position[1] - MOVE_UNIT)
            new_tail_position = get_rope_tail_position(
                new_head_position,
                head_knot_position,
                current_tail_position
            )
            if new_tail_position not in tail_knot_positions:
                tail_knot_positions[new_tail_position[0]] = {new_tail_position[1]}
            else:
                tail_knot_positions[new_tail_position[0]].add(new_tail_position[1])
        elif move_direction == "L":
            new_head_position = (head_knot_position[0] - MOVE_UNIT, head_knot_position[1])
            new_tail_position = get_rope_tail_position(
                    new_head_position,
                    head_knot_position,
                    current_tail_position
                )
            tail_knot_positions[new_tail_position[0]].add(new_tail_position[1])
        elif move_direction == "R":
            new_head_position = (head_knot_position[0] + MOVE_UNIT, head_knot_position[1])
            new_tail_position = get_rope_tail_position(
                    new_head_position,
                    head_knot_position,
                    current_tail_position
                )
            tail_knot_positions[new_tail_position[0]].add(new_tail_position[1])
        else:
            raise ValueError(f"Invalid move direction: {move_direction}")
    return tail_knot_positions


# Part 1 Solution
# ---------------
def find_unique_positions_visited_by_tail(puzzle_input_filename: str) -> int:
    """Returns the unique number of positions visited by the tail of the rope
    after completing the series of motions given in the input file.

    Parameters
    ----------
    puzzle_input_filename: Name of the input file.

    Returns
    -------
    Returns an integer representing the no. of positions visited by rope's tail
    knot.
    """
    with open(puzzle_input_filename, "r", encoding="utf-8") as puzzle_input_file:
        head_movement_instructions = []
        while input_line := puzzle_input_file.readline()[:-1]:
            move_direction, move_distance = extract_direction_and_distance(input_line)
            head_movement_instructions.append((move_direction, move_distance))
        tail_knot_positions = populate_tail_positions_map(
            start_position=(0, 0),
            head_movement_instructions=head_movement_instructions
        )
        print(f"Tail Knot Positions: {tail_knot_positions}")
    return 0


if __name__ == "__main__":
    PUZZLE_INPUT_FILENAME = "day-9-input.txt"
    print(find_unique_positions_visited_by_tail(PUZZLE_INPUT_FILENAME))
