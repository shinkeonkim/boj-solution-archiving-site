package main

import (
	"bufio"
	"fmt"
	"os"
)

var writer *bufio.Writer
var reader *bufio.Reader

func Print(a ...interface{}) {
	fmt.Fprintln(writer, a...)
}

func Abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func diff(a []int, b []int) int {
	return Abs(a[0]-b[0]) + Abs(a[1]-b[1])
}

func solve() {
	var pos1 = map[string][]int{
		"q": {0, 0},
		"w": {0, 1},
		"e": {0, 2},
		"r": {0, 3},
		"t": {0, 4},
		"a": {1, 0},
		"s": {1, 1},
		"d": {1, 2},
		"f": {1, 3},
		"g": {1, 4},
		"z": {2, 0},
		"x": {2, 1},
		"c": {2, 2},
		"v": {2, 3},
	}

	var pos2 = map[string][]int{
		"y": {0, 5},
		"u": {0, 6},
		"i": {0, 7},
		"o": {0, 8},
		"p": {0, 9},
		"h": {1, 5},
		"j": {1, 6},
		"k": {1, 7},
		"l": {1, 8},
		"b": {2, 4},
		"n": {2, 5},
		"m": {2, 6},
	}

	var a, b, s string

	fmt.Fscanf(reader, "%s %s\n%s", &a, &b, &s)

	left := pos1[a]
	right := pos2[b]
	ans := len(s)

	for i := 0; i < len(s); i++ {
		current := string(s[i])

		pos, ok := pos1[current]

		if ok {
			ans += diff(left, pos)
			left = pos
		}

		pos, ok = pos2[current]

		if ok {
			ans += diff(right, pos)
			right = pos
		}
	}

	Print(ans)

}

func main() {
	writer = bufio.NewWriter(os.Stdout)
	reader = bufio.NewReader(os.Stdin)
	defer writer.Flush()

	solve()
}
