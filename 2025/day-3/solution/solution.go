package solution

import "suyashd95/aoc/2025/internal"

// import "fmt"

/* Returns an integer that represents the maximum joltage
 * possible for a given arrangement of batteries in the bank.
 *
 * NOTE: The batteries are not rearranged i.e., the order of the
 * original slice of integers is not changed.
 */
func getBankMaxOutput(batteryBank []int) int {
	var maxJoltage int
	for fstIdx, majorOut := range batteryBank {
		for sndIdx := fstIdx + 1; sndIdx < len(batteryBank); sndIdx++ {
			minorOut := batteryBank[sndIdx]
			totalOutput := (majorOut * 10) + minorOut
			if totalOutput > maxJoltage {
				maxJoltage = totalOutput
			}
		}
	}
	return maxJoltage
}

/* This function returns the maximum output joltage which is
 * the sum of the highest joltage possible in each bank present
 * in the sequence.
 */
func SolveFirstPuzzle(batteryBanks [][]int) int {
	var totalOutputJoltage int
	for _, batteries := range batteryBanks {
		// fmt.Printf("Batteries: %v = ", batteries)
		maxOutput := getBankMaxOutput(batteries)
		// fmt.Printf("%v\n", maxOutput)
		totalOutputJoltage += maxOutput
	}
	return totalOutputJoltage
}

func getBankMaxJoltage(bankList *internal.BatteryBank, startPos int, bankArr []int) int64 {
}

/* This function returns the maximum output joltage which the sum of
 * 12 largest batteries present in each bank provided in the sequence.
 */
func SolveSecondPuzzle(batteryBanks [][]int) int64 {
	var totalOutputJoltage int64
	const INITIAL_POSITION = 0
	for _, batteries := range batteryBanks {
		bank := internal.NewBatteryList(batteries[INITIAL_POSITION])
		maxOut := getBankMaxJoltage(bank, INITIAL_POSITION+1, batteries)
		totalOutputJoltage += maxOut
	}
	return totalOutputJoltage
}
