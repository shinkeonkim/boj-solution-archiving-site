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

func StringIntCompare(s1, s2 string) int {
	if len(s1) > len(s2) {
		return 1
	} else if len(s1) < len(s2) {
		return -1
	}

	for i := 0; i < len(s1); i++ {
		if s1[i] > s2[i] {
			return 1
		} else if s1[i] < s2[i] {
			return -1
		}
	}

	return 0
}

func Solve() {
	var n int
	var s string
	var a string

	fmt.Fscan(reader, &n, &s, &a)

	for i := 0; i < n; i++ {
		if s[i] == '?' {
			s = s[:i] + "9" + s[i+1:]
		}
	}
	res := StringIntCompare(s, a)

	if res >= 0 {
		Print(s)
	} else {
		Print(-1)
	}

}

func main() {
	writer = bufio.NewWriter(os.Stdout)
	reader = bufio.NewReader(os.Stdin)
	defer writer.Flush()

	Solve()
}
