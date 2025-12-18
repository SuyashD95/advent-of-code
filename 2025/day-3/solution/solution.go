package solution

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
