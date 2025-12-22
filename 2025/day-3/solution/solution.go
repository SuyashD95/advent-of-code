package solution

import (
	"fmt"
	"suyashd95/aoc/2025/internal"
)

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

/* Returns the max joltage from the sequence of batteries which starts from the given position. */
func getBankMaxJoltage(batSeq *internal.BatteryBank, startPos int, bankArr []int, globalMax int64, resultStore map[string]int64) int64 {
	// fmt.Printf("getBankMaxJoltage [Beginning]: %s, %d, %v, %d\n", batSeq.ToString(), startPos, bankArr, globalMax)
	seqSummary := batSeq.ToString()
	if output, ok := resultStore[seqSummary]; ok {
		fmt.Printf("Retrieving output from cache: %#s = %d\n", seqSummary output)
		if output > globalMax {
			fmt.Println("Global max has been changed...")
			globalMax = output
		}
		return output
	}
	if batSeq.Count() >= internal.MAX_BATTERIES_IN_PACK {
		// fmt.Printf("getBankMaxJoltage [Max Count Reached]: %d\n", batSeq.Count())
		return batSeq.CalculateOutput()
	} else if startPos >= len(bankArr) {
		// fmt.Printf("getBankMaxJoltage [End of Array]: %d, %d\n", startPos, len(bankArr))
		return batSeq.CalculateOutput()
	}
	// fmt.Printf("getBankMaxJoltage [Initial Max Jolts]: %d\n", globalMax)
	for currentPos := startPos; currentPos < len(bankArr); currentPos++ {
		batSeq.Append(bankArr[currentPos])
		// fmt.Printf("getBankMaxJoltage [After adding %d present at %d index]: %s\n", bankArr[currentPos], currentPos, batSeq.ToString())
		seqJolts := getBankMaxJoltage(batSeq, currentPos+1, bankArr, globalMax)
		// fmt.Printf("getBankMaxJoltage [Sequence Jolts]: %d\n", seqJolts)
		batSeq.Remove()
		// fmt.Printf("getBankMaxJoltage [After removing %d present at %d index]: %s\n", bankArr[currentPos], currentPos, batSeq.ToString())
		if seqJolts > globalMax {
			globalMax = seqJolts
			// fmt.Printf("getBankMaxJoltage [New Max Jolts]: %d\n", globalMax)
		} else {
			// fmt.Printf("getBankMaxJoltage [Max Jolts Remain Unchanged]: %d / %d \n", seqJolts, globalMax)
		}
	}
	// fmt.Printf("getBankMaxJoltage [Reached End]\n")
	return globalMax
}

/* This function returns the maximum output joltage which the sum of
 * 12 largest batteries present in each bank provided in the sequence.
 */
func SolveSecondPuzzle(batteryBanks [][]int) int64 {
	var totalOutputJoltage int64
	outputCache := make(map[string]int64)
	for index, batteries := range batteryBanks {
		fmt.Printf("Output of %d: %v = ", index, batteries)
		maxInitialPosition := len(batteries) - internal.MAX_BATTERIES_IN_PACK
		// fmt.Printf("Batteries: %v ; Length: %d\n", batteries, len(batteries))
		// fmt.Printf("Max Initial Position: %d\n", maxInitialPosition)
		var bankMax int64
		for initialPosition := range batteries {
			if initialPosition > maxInitialPosition {
				break
			}
			batterySeq := internal.NewBatteryList(batteries[initialPosition])
			// fmt.Println("New battery sequence:", batterySeq.ToString())
			localMax := getBankMaxJoltage(batterySeq, initialPosition+1, batteries, bankMax)
			// fmt.Printf("Local bank output: = %d\n", localMax)
			if localMax > bankMax {
				bankMax = localMax
				// fmt.Printf("New maximum output: %d\n", bankMax)
			}
		}
		fmt.Printf("%d\n", bankMax)
		totalOutputJoltage += bankMax
	}
	return totalOutputJoltage
}
