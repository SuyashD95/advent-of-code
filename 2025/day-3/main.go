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
func getBatteryBanks(absPath string) []string {
	iFile, err := os.Open(absPath)
	if err != nil {
		log.Fatalf("Cannot read open file at %v: %v\n", absPath, err)
	}
	defer iFile.Close()
	batteryBanks := make([]string, 0)
	lnReader := bufio.NewScanner(iFile)
	for lnReader.Scan() {
		bank := lnReader.Text()
		batteryBanks = append(batteryBanks, bank)
	}
	return batteryBanks
}

func main() {
	batteryBanks := getBatteryBanks("datasets/input.txt")
	fmt.Printf(
		"Day 3: Lobby\n\tPart 1: %v\n\tPart 2: Pending\n",
		solution.SolveFirstPuzzle(internal.BanksToOutputArrays(batteryBanks)),
	)
}
