package internal

import (
	"errors"
	"fmt"
	"strconv"
	"strings"
)

type Rotation struct {
	Direction string
	Steps     int
}

/* Returns a new `Rotation` based on the string given in the "<direction><steps>" format. */
func MakeRotation(rotation string) (*Rotation, error) {
	code := strings.TrimSpace(rotation)
	if code == "" {
		return nil, errors.New("No data in given rotation code")
	}
	var direction string
	switch {
	case strings.HasPrefix(code, "L") == true:
		direction = "L"
	case strings.HasPrefix(code, "R") == true:
		direction = "R"
	default:
		return nil, fmt.Errorf("Invalid direction: '%v'", string(code[0]))
	}
	Sstep, _ := strings.CutPrefix(code, direction)
	steps, err := strconv.Atoi(Sstep)
	if err != nil {
		return nil, fmt.Errorf("Invalid step value: %w", err)
	} else if steps < 0 {
		return nil, fmt.Errorf("`Rotation.steps` ('%d') must be integer greater than 0", steps)
	}
	return &Rotation{
		Direction: direction,
		Steps:     steps,
	}, nil
}
