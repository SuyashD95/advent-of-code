package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"suyashd95/aoc/2025/internal"
	"suyashd95/aoc/2025/solution"
)

/* Returns a slice containing rotations that has to be processed to get the answer. */
func getRotationsFromInput(absPath string) []internal.Rotation {
	rotations := make([]internal.Rotation, 0)
	iFile, err := os.Open(absPath)
	if err != nil {
		log.Fatalf("Cannot read input.txt: %v\n", err)
	}
	defer iFile.Close()

	lnReader := bufio.NewScanner(iFile)
	for lnReader.Scan() {
		rotation := lnReader.Text()
		r, err := internal.MakeRotation(rotation)
		if err != nil {
			log.Fatalf("Illegal rotation encountered: %v", err)
		}
		rotations = append(rotations, *r)
	}
	return rotations
}

func main() {
	rotationSeq := getRotationsFromInput("input.txt")
	fmt.Printf(
		"Day 1: Secret Entrance\n\t1st Puzzle: %v\n\t2nd Puzzle: Pending\n",
		solution.SolveFirstPuzzle(rotationSeq),
	)
}
