package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	const absPath = "input.txt"
	iFile, err := os.Open(absPath)
	if err != nil {
		log.Fatalf("Cannot read input.txt: %v\n", err)
	}
	defer iFile.Close()

	lnReader := bufio.NewScanner(iFile)
	for lnReader.Scan() {
		rotations := lnReader.Text()
		fmt.Printf("%s\n", rotations)
	}
}
