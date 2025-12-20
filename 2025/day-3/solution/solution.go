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
func getBankMaxJoltage(batSeq *internal.BatteryBank, startPos int, bankArr []int) int64 {
	fmt.Printf("getBankMaxJoltage [Beginning]: %s, %d, %v\n", batSeq.ToString(), startPos, bankArr)
	if batSeq.Count() >= internal.MAX_BATTERIES_IN_PACK {
		fmt.Printf("getBankMaxJoltage [Max Count Reached]: %d\n", batSeq.Count())
		return batSeq.CalculateOutput()
	} else if startPos >= len(bankArr) {
		fmt.Printf("getBankMaxJoltage [End of Array]: %d, %d\n", startPos, len(bankArr))
		return batSeq.CalculateOutput()
	}
	var maxJolts int64
	fmt.Printf("getBankMaxJoltage [Initial Max Jolts]: %d\n", maxJolts)
	for currentPos := startPos; currentPos < len(bankArr); currentPos++ {
		batSeq.Append(bankArr[currentPos])
		fmt.Printf("getBankMaxJoltage [After adding %d present at %d index]: %s\n", bankArr[currentPos], currentPos, batSeq.ToString())
		seqJolts := getBankMaxJoltage(batSeq, currentPos+1, bankArr)
		fmt.Printf("getBankMaxJoltage [Sequence Jolts]: %d\n", seqJolts)
		fmt.Printf("getBankMaxJoltage [After removing %d present at %d index]: %s\n", bankArr[currentPos], currentPos, batSeq.ToString())
		if seqJolts > maxJolts {
			maxJolts = seqJolts
			fmt.Printf("getBankMaxJoltage [New Max Jolts]: %d\n", maxJolts)
		}
	}
	fmt.Printf("getBankMaxJoltage [Reached End]\n")
	return maxJolts
}

/* This function returns the maximum output joltage which the sum of
 * 12 largest batteries present in each bank provided in the sequence.
 */
func SolveSecondPuzzle(batteryBanks [][]int) int64 {
	var totalOutputJoltage int64
	for _, batteries := range batteryBanks {
		maxInitialPosition := len(batteries) - internal.MAX_BATTERIES_IN_PACK
		fmt.Printf("Batteries: %v ; Length: %d\n", batteries, len(batteries))
		fmt.Printf("Max Initial Position: %d\n", maxInitialPosition)
		var bankMax int64
		for initialPosition := range batteries {
			if initialPosition > maxInitialPosition {
				break
			}
			batterySeq := internal.NewBatteryList(batteries[initialPosition])
			fmt.Println("New battery sequence:", batterySeq.ToString())
			localMax := getBankMaxJoltage(batterySeq, initialPosition+1, batteries)
			fmt.Printf("Local bank output: = %d\n", localMax)
			if localMax > bankMax {
				bankMax = localMax
				fmt.Printf("New maximum output: %d\n", bankMax)
			}
		}
		totalOutputJoltage += bankMax
	}
	return totalOutputJoltage
}
