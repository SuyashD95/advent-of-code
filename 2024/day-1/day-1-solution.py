"""
Advent of Code 2024
-------------------
Day 1: Historian Hysteria (Finished)

Part 1 (Finished):
    Question: What is the total distance between your lists?
    Answer: 1590491

Part 2 (Finished):
    Question: What is their similarity score?
    Answer: 22588371 
-------------------

Author: Suyash Dayal
Originally Completed On: 4th December 2024
"""
from collections import Counter


def find_total_distance(puzzle_input_filename: str) -> int:
    """Returns the total distance between pairs of smallest nos.
    from the two lists.

    Parameters
    ----------
    puzzle_input_filename: Name of text file containing input dataset.

    Returns
    -------
    Total distance between number pairs.
    """
    hist_list_1 = []
    hist_list_2 = []
    with open(puzzle_input_filename, encoding="utf-8") as puzzle_file:
        while line := puzzle_file.readline()[:-1]:
            fst_loc_id, snd_loc_id = [int(loc_id) for loc_id in line.split("   ")]
            hist_list_1.append(fst_loc_id)
            hist_list_2.append(snd_loc_id)
    
    hist_list_1.sort()
    hist_list_2.sort()
    total = 0
    for loc_id1, loc_id2 in zip(hist_list_1, hist_list_2):
        total += abs(loc_id1 - loc_id2)
    return total


def find_similarity_score(puzzle_input_filename: str) -> int:
    """Returns the similarity score between the two lists of numbers.

    Parameters
    ----------
    puzzle_input_filename: Name of text file containing input dataset.

    Returns
    -------
    Similarity score between the two lists.
    """
    hist_list_1 = []
    hist_list_2 = []
    with open(puzzle_input_filename, encoding="utf-8") as puzzle_file:
        while line := puzzle_file.readline()[:-1]:
            fst_loc_id, snd_loc_id = [int(loc_id) for loc_id in line.split("   ")]
            hist_list_1.append(fst_loc_id)
            hist_list_2.append(snd_loc_id)

    hlist_2_freq_counter = Counter(hist_list_2)
    similarity_score = 0
    for loc_id in hist_list_1:
        freq_in_hlist2 = hlist_2_freq_counter.get(loc_id, 0)
        similarity_score += (loc_id * freq_in_hlist2)
    return similarity_score


if __name__ == "__main__":
    PUZZLE_INPUT_FILENAME = "day-1-input.txt"
    print(
        "Day 1 Answers:\n"
        f"  Part 1: {find_total_distance(PUZZLE_INPUT_FILENAME)}\n"
        f"  Part 2: {find_similarity_score(PUZZLE_INPUT_FILENAME)}"
    )

