package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"suyashd95/aoc/2025/internal"
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
	fmt.Println(rotationSeq)
}
