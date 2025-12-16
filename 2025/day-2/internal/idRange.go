package internal

import (
	"fmt"
	"strconv"
	"strings"
)

type IDRange struct {
	Start uint64
	End   uint64
}

const RANGE_SEPARATOR = ","
const RANGE_START_END_SEPARATOR = "-"

/* Returns a slice of ranges whereas ranges are separated by comma(,)
 * and their start & end IDs (both-inclusive) are separated by dashes (-).
 */
func NewIDRanges(sRange string) ([]IDRange, error) {
	const DECIMAL_BASE = 10
	const UINT_BITS = 64
	ranges := make([]IDRange, 0)
	if sRange == "" {
		return nil, fmt.Errorf("Range string cannot be empty")
	}
	sRangeGroup := strings.SplitSeq(sRange, RANGE_SEPARATOR)
	for sr := range sRangeGroup {
		start, end, _ := strings.Cut(sr, RANGE_START_END_SEPARATOR)
		startVal, err := strconv.ParseUint(start, DECIMAL_BASE, UINT_BITS)
		if err != nil {
			return nil, fmt.Errorf("Unable to convert start ID (%v) into 64-bit unsigned integer", start)
		}
		endVal, err := strconv.ParseUint(end, DECIMAL_BASE, UINT_BITS)
		if err != nil {
			return nil, fmt.Errorf("Unable to convert end ID (%v) into 64-bit unsigned integer", end)
		}
		ranges = append(
			ranges,
			IDRange{
				Start: startVal,
				End:   endVal,
			},
		)
	}
	return ranges, nil
}
