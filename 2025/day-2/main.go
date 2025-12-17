package main

import (
	"fmt"
	"log"
	"os"
	"strings"
	"suyashd95/aoc/2025/internal"
	"suyashd95/aoc/2025/solution"
)

/* Returns range of product IDs from the input file  */
func extractIDRanges(absPath string) []internal.IDRange {
	inputFile, err := os.ReadFile(absPath)
	if err != nil {
		log.Fatalf("Unable to read file: %s (%v)", absPath, err)
	}
	rangeString, _ := strings.CutSuffix(string(inputFile), "\n")
	ranges, err := internal.NewIDRanges(rangeString)
	if err != nil {
		log.Fatalf("Unable to get ranges for analysis. Reason: %v", err)
	}
	return ranges
}

func main() {
	idRanges := extractIDRanges("datasets/input.txt")
	fmt.Printf(
		"Day 2: Gift Shop\n\tPart 1: %d\n\tPart 2: Pending\n",
		solution.SolveFirstPuzzle(idRanges),
	)
}
