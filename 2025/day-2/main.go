package main

import (
	"fmt"
	"log"
	"os"
	"strings"
	"suyashd95/aoc/2025/internal"
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
	idRanges := extractIDRanges("datasets/sample1.txt")
	fmt.Println(idRanges)
	fmt.Printf("Day 2: Gift Shop\n\tPart 1: Pending\n\tPart 2: Pending\n")
}
