package internal

import (
	"fmt"
	"log"
	"math"
	"strings"
)

const MAX_BATTERIES_IN_PACK = 12

type Battery struct {
	Joltage int
	Next    *Battery
}

func (b Battery) ToString() string {
	return fmt.Sprintf("%d", b.Joltage)
}

type BatteryBank struct {
	Head *Battery
}

func NewBatteryList(joltage int) *BatteryBank {
	return &BatteryBank{
		Head: &Battery{
			Joltage: joltage,
			Next:    nil,
		},
	}
}

/* Adds a new Battery element to the end of existing sequence of batteries. */
func (bb *BatteryBank) Append(joltage int) {
	var parentNode *Battery
	for node := bb.Head; node != nil; node = node.Next {
		parentNode = node
	}
	parentNode.Next = &Battery{
		Joltage: joltage,
		Next:    nil,
	}
}

/* Returns the total output that is produced by the sequence of
 * batteries in the bank.
 */
func (bb BatteryBank) CalculateOutput() int64 {
	var totalOutput int64
	var currentDepth int
	for node := bb.Head; node != nil; node = node.Next {
		currentDepth += 1
		totalOutput += int64(node.Joltage) * int64(math.Pow10(MAX_BATTERIES_IN_PACK-currentDepth))
	}
	return totalOutput
}

/* Prints a string representing the sequence of batteries present in the list */
func (bb BatteryBank) ToString() string {
	var builder strings.Builder
	if _, err := builder.WriteString("H -> "); err != nil {
		log.Fatalf("Unable to write head string into builder: %v", err)
	}
	for node := bb.Head; node != nil; node = node.Next {
		if _, err := builder.WriteString(fmt.Sprintf("%s -> ", node.ToString())); err != nil {
			log.Fatalf("Unable to append battery string into builder: %v", err)
		}
	}
	if _, err := builder.WriteString("X\n"); err != nil {
		log.Fatalf("Unable to write EOL string into builder: %v", err)
	}
	return builder.String()
}
