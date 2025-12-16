package solution

import (
	"suyashd95/aoc/2025/internal"
)

const DIAL_MIN_VALUE = 0
const DIAL_MAX_VALUE = 99
const DIAL_START_POSITION = 50
const DIAL_TARGET_POSITION = 0
const DIRECTION_RIGHT = "R"
const DIRECTION_LEFT = "L"

/* Returns the solution to the part 1 puzzle of Day 1 of AoC2025. */
func SolveFirstPuzzle(rotations []internal.Rotation) int {
	dialReachesZero := 0
	dialCurrentPosition := DIAL_START_POSITION

	if dialCurrentPosition == DIAL_TARGET_POSITION {
		dialReachesZero += 1
	}
	for _, r := range rotations {
		switch r.Direction {
		case DIRECTION_RIGHT:
			for i := 0; i < r.Steps; i++ {
				if dialCurrentPosition == DIAL_MAX_VALUE {
					dialCurrentPosition = DIAL_MIN_VALUE
				} else {
					dialCurrentPosition += 1
				}
			}
		case DIRECTION_LEFT:
			for i := 0; i < r.Steps; i++ {
				if dialCurrentPosition == DIAL_MIN_VALUE {
					dialCurrentPosition = DIAL_MAX_VALUE
				} else {
					dialCurrentPosition -= 1
				}
			}
		}
		if dialCurrentPosition == DIAL_TARGET_POSITION {
			dialReachesZero += 1
		}
	}
	return dialReachesZero
}

/* Returns the solution to the part 2 puzzle of Day 1 of AoC2025. */
func SolveSecondPuzzle(rotations []internal.Rotation) int {
	dialReachesZero := 0
	dialCurrentPosition := DIAL_START_POSITION

	if dialCurrentPosition == DIAL_TARGET_POSITION {
		dialReachesZero += 1
	}
	for _, r := range rotations {
		switch r.Direction {
		case DIRECTION_RIGHT:
			for i := 0; i < r.Steps; i++ {
				if dialCurrentPosition == DIAL_MAX_VALUE {
					dialCurrentPosition = DIAL_MIN_VALUE
				} else {
					dialCurrentPosition += 1
				}
				if dialCurrentPosition == DIAL_TARGET_POSITION {
					dialReachesZero += 1
				}
			}
		case DIRECTION_LEFT:
			for i := 0; i < r.Steps; i++ {
				if dialCurrentPosition == DIAL_MIN_VALUE {
					dialCurrentPosition = DIAL_MAX_VALUE
				} else {
					dialCurrentPosition -= 1
				}
				if dialCurrentPosition == DIAL_TARGET_POSITION {
					dialReachesZero += 1
				}
			}
		}
	}
	return dialReachesZero
}
