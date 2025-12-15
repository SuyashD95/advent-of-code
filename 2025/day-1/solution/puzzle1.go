package solution

import (
	"suyashd95/aoc/2025/internal"
)

/* Returns the solution to the first puzzle of Day 1 of AoC2025. */
func SolveFirstPuzzle(rotations []internal.Rotation) int {
	const DIAL_MIN_POSITION = 0
	const DIAL_START_POSITION = 50
	const DIAL_MAX_VALUE = 99
	dial := make([]int, DIAL_MAX_VALUE+1)
	for i := range dial {
		dial[i] = i
	}

	dialReachesZero := 0
	dialCurrentPosition := DIAL_START_POSITION
	for _, r := range rotations {
		if r.Direction == "R" {
			dialCurrentPosition = (dialCurrentPosition + r.Steps) % len(dial)
		} else {
		}

		if dialCurrentPosition == DIAL_MIN_POSITION {
			dialReachesZero += 1
		}
	}
	return dialReachesZero
}
