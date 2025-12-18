package internal

import (
	"log"
	"strconv"
	"strings"
)

func BanksToOutputArrays(batteryBanks []string) [][]int {
	banks := make([][]int, 0)
	for _, bank := range batteryBanks {
		// fmt.Printf("Bank: %#v ( ", bank)
		batteries := make([]int, 0)
		for battery := range strings.SplitSeq(bank, "") {
			output, err := strconv.Atoi(battery)
			if err != nil {
				log.Fatalf(
					"Unable to convert battery output to an integer (%#v of %#v): %#v",
					output,
					battery,
					err,
				)
			}
			// fmt.Printf("%#v ", output)
			batteries = append(batteries, output)
		}
		// fmt.Printf(")\n")
		banks = append(banks, batteries)
	}
	// fmt.Println(banks)
	return banks
}
