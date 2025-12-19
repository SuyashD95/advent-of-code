package internal

import (
	"fmt"
	"log"
	"strings"
)

const MAX_ONLINE_BATTERIES_IN_PACK = 12

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

func (bb BatteryBank) ToString() string {
	var builder strings.Builder
	if _, err := builder.WriteString("H -> "); err != nil {
		log.Fatalf("Unable to write head string into builder: %w", err)
	}
	for node := bb.Head; node != nil; node = node.Next {
		if _, err := builder.WriteString(fmt.Sprintf("%s -> ", node.ToString())); err != nil {
			log.Fatalf("Unable to append battery string into builder: %w", err)
		}
	}
	if _, err := builder.WriteString("X\n"); err != nil {
		log.Fatalf("Unable to write EOL string into builder: %w", err)
	}
	return builder.String()
}
