"""
Advent of Code 2024
-------------------
Day 2: Red-Nosed Reports (Finished)

Part 1 (Finished):
    Question: How many reports are safe?
    Answer: 472

Part 2 (Finished):
    Question: How many reports are now safe?
    Answer: 520
-------------------

Author: Suyash Dayal
Originally Completed On: 27th December 2024
"""
from enum import Enum


class Sign(Enum):
    """Sign of the difference between 2 levels."""
    NOSIGN = 0
    POSITIVE = 1
    NEGATIVE = -1


def is_report_safe(report: list[int]) -> bool:
    """Returns a boolean indicating whether a report is deemed
    is safe based on given constraints.
    """
    prev_sign = Sign.NOSIGN
    first_ptr = 0
    second_ptr = 1
    while second_ptr < len(report):
        diff = report[second_ptr] - report[first_ptr]
        if diff == 0:
            return False
        if abs(diff) > 3:
            return False
        if diff > 0:
            if prev_sign == Sign.NOSIGN:
                prev_sign = Sign.POSITIVE
            elif prev_sign == Sign.NEGATIVE:
                return False
        else:
            if prev_sign == Sign.NOSIGN:
                prev_sign = Sign.NEGATIVE
            elif prev_sign == Sign.POSITIVE:
                return False
        first_ptr += 1
        second_ptr += 1
    return True


def find_safe_reports(input_filename: str) -> int:
    """Returns the count of reports that are deemed safe based on
    the 2 given conditions: levels are all increasing or decreasing
    (i.e., they are monotonic) and any two adjacent levels differ by
    at least 1 and at most 3.

    Parameters
    ----------
    input_filename: Name of input file.

    Returns
    -------
    A whole number indicating number of safe reports.
    """
    safe_reports = 0
    with open(input_filename, encoding="utf-8") as input_file:
        while report_string := input_file.readline()[:-1]:
            if is_report_safe(list(map(int, report_string.split()))):
                safe_reports += 1
    return safe_reports


def find_safe_reports_with_problem_dampener(input_filename: str) -> int:
    """Returns the count of reports that are deemed safe based on
    the 2 given conditions: levels are all increasing or decreasing
    (i.e., they are monotonic) and any two adjacent levels differ by
    at least 1 and at most 3.

    Due to the presence of problem dampener, the report is deemed safe
    if only one level is wrong and it is ignored.

    Parameters
    ----------
    input_filename: Name of input file.

    Returns
    -------
    A whole number indicating number of safe reports.
    """
    def apply_problem_dampener(original_report: list[int]) -> bool:
        """Apply problem dampening by removing one value present from the original report
        (at a time) and then reinspect the report. If it is deemed safe, return `True`;
        otherwise `False`.
        """
        for skip_idx, _ in enumerate(original_report):
            modified_report = original_report[:skip_idx] + original_report[skip_idx+1:]
            if is_report_safe(modified_report):
                return True
        return False

    safe_reports = 0
    with open(input_filename, encoding="utf-8") as input_file:
        while report_string := input_file.readline()[:-1]:
            original_report = list(map(int, report_string.split()))
            is_safe = is_report_safe(original_report)
            if is_safe:
                safe_reports += 1
            else:
                post_result = apply_problem_dampener(original_report)
                if post_result:
                    safe_reports += 1
    return safe_reports


if __name__ == "__main__":
    PUZZLE_INPUT_FILENAME = "day-2-input.txt"
    print(
        "Day 2 Answers:\n"
        f"  Part 1: {find_safe_reports(PUZZLE_INPUT_FILENAME)}\n"
        f"  Part 2: {find_safe_reports_with_problem_dampener(PUZZLE_INPUT_FILENAME)}"
    )
