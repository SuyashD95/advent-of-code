package solution

import (
	"strconv"
	"suyashd95/aoc/2025/internal"
)

/* This function returns `true` fi given product ID is invalid;
 * otherwise returns `false`.
 */
func isPidInvalid(pid uint64) bool {
	const BASE_DECIMAL = 10
	sPid := strconv.FormatUint(pid, BASE_DECIMAL)
	midPt := len(sPid) / 2
	fstHalf, sndHalf := sPid[:midPt], sPid[midPt:]
	return fstHalf == sndHalf
}

/* Returns the answer of Day 2 Part One puzzle of Advent of Code 2025 challenge  */
func SolveFirstPuzzle(pidRanges []internal.IDRange) uint64 {
	var invalidIDTotal uint64
	for _, pidRange := range pidRanges {
		for pid := pidRange.Start; pid <= pidRange.End; pid++ {
			if isPidInvalid(pid) {
				invalidIDTotal += pid
			}
		}
	}
	return invalidIDTotal
}
