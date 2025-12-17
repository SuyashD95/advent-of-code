package solution

import (
	"fmt"
	"log"
	"strconv"
	"strings"
)

/* This function returns the maximum output joltage which is
 * the sum of the highest joltage possible in each bank present
 * in the sequence.
 */
func SolveFirstPuzzle(batteryBanks []string) int {
	var totalOutputJoltage int
	banks := make([][]int, 0)
	for _, bank := range batteryBanks {
		fmt.Printf("Bank: %#v ( ", bank)
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
			fmt.Printf("%#v ", output)
			batteries = append(batteries, output)
		}
		fmt.Printf(")\n")
		banks = append(banks, batteries)
	}
	fmt.Println(banks)
	return totalOutputJoltage
}
