package main

import (
	"bufio"
	"fmt"
	"os"
)

var writer *bufio.Writer
var reader *bufio.Reader

func print(a ...interface{}) {
	fmt.Fprintln(writer, a...)
}

func readInt() int {
	var n int
	fmt.Fscanf(reader, "%d\n", &n)
	return n
}

func readTwoInt() []int {
	var a int
	var b int

	fmt.Fscanf(reader, "%d %d\n", &a, &b)
	return []int{a, b}
}

func solve() {
	n := readInt()
	position := readInt()

	m := readInt()

	ar := make([]int, n+1)

	ar[position] = 1

	for i := 0; i < m; i++ {
		l := readTwoInt()
		a, b := l[0], l[1]

		ar[a], ar[b] = ar[b], ar[a]
	}

	for i := 1; i <= n; i++ {
		if ar[i] == 1 {
			print(i)
			break
		}
	}
}

func main() {
	writer = bufio.NewWriter(os.Stdout)
	reader = bufio.NewReader(os.Stdin)
	defer writer.Flush()

	solve()
}
