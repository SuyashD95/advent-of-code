package solution

import (
	// "fmt"
	"strconv"
	"strings"
	"suyashd95/aoc/2025/internal"
)

/* This function returns `true` fi given product ID is invalid;
 * otherwise returns `false`.
 * It is considered as an enhanced version of `isPidInvalid()` in which
 * subsequence (of variable length) of product ID needs to be repeated at least twice.
 */
func isPidInvalid2(pid uint64) bool {
	const BASE_DECIMAL = 10
	const MIN_REPEATS = 2
	sPid := strconv.FormatUint(pid, BASE_DECIMAL)
	midPt := len(sPid) / 2
	// fmt.Printf("Computing Pid: %v's state... It is ", sPid)
	for subseqLen := midPt; subseqLen > 0; subseqLen-- {
		prefix := sPid[:subseqLen]
		subSeq := sPid
		isPrefixPresent := true
		for isPrefixPresent {
			cutSubSeq, _ := strings.CutPrefix(subSeq, prefix)
			isPrefixPresent = strings.HasPrefix(cutSubSeq, prefix)
			// fmt.Printf("  %#v substring after cutting %#v prefix -> %#v (%v),\n", subSeq, prefix, cutSubSeq, isPrefixPresent)
			subSeq = cutSubSeq
		}
		if subSeq == "" {
			// fmt.Println("invalid")
			return true
		}
	}
	// fmt.Println("valid")
	return false
}

/* Returns the answer of Day 2 Part Two puzzle of Advent of Code 2025 challenge  */
func SolveSecondPuzzle(pidRanges []internal.IDRange) uint64 {
	var invalidIDTotal uint64
	pidValidityCache := make(map[uint64]bool)
	for _, pidRange := range pidRanges {
		for pid := pidRange.Start; pid <= pidRange.End; pid++ {
			if valid, ok := pidValidityCache[pid]; ok {
				if !valid {
					invalidIDTotal += pid
				}
			} else {
				isInvalid := isPidInvalid2(pid)
				pidValidityCache[pid] = !isInvalid
				if isInvalid {
					invalidIDTotal += pid
				}
			}
		}
	}
	return invalidIDTotal
}
