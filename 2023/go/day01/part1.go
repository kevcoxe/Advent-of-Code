package main

import (
	"fmt"
	"strconv"
)

func getNumbers(word string) (int, error) {
	ai := 0
	bi := len(word) - 1

	a := string(word[ai])
	b := string(word[bi])

	aFound := false
	bFound := false

	aNum := 0
	bNum := 0

	fmt.Printf("\nFinding numbers in word (%s)...\n", word)

	for {
		if !aFound {
			if newA, aErr := strconv.Atoi(a); aErr == nil {
				fmt.Printf("..found A (%q)...\n", a)
				aFound = true
				aNum = newA
				ai = ai + 1
			} else {
				ai = ai + 1
				a = string(word[ai])
			}
		}

		if !bFound {
			if newB, bErr := strconv.Atoi(b); bErr == nil {
				fmt.Printf("..found B (%q)...\n", b)
				bFound = true
				bNum = newB
				bi = bi - 1
			} else {
				bi = bi - 1
				b = string(word[bi])
			}
		}

		if ai > bi+1 || (aFound && bFound) {
			break
		}
	}

	combinedNumber := fmt.Sprintf("%d%d", aNum, bNum)
	returnNumber, err := strconv.Atoi(combinedNumber)

	return returnNumber, err
}

func part1() {
	finalCode := 0
	fmt.Println("\nStarting part 1...")

	for _, word := range Data {
		numberFromWord, err := getNumbers(word)
		if err == nil {
			finalCode = finalCode + numberFromWord
		}

	}

	fmt.Println("\nFinal code is: ", finalCode)
}
