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

func solve() {
	var N, L int

	fmt.Fscanf(reader, "%d %d\n", &N, &L)

	D := make([]int, N+1)
	R := make([]int, N+1)
	G := make([]int, N+1)

	for i := 0; i < N; i++ {
		fmt.Fscanf(reader, "%d %d %d\n", &D[i], &R[i], &G[i])
	}

	// for i := 0; i < N; i++ {
	// 	print(D[i], " ", R[i], " ", G[i], "\n")
	// }

	D[N] = L

	var lastDestinationTime = 0
	var prevPosition = 0
	var currentTime = 0

	for i := 0; i <= N; i++ {
		currentTime += D[i] - prevPosition
		lastDestinationTime = currentTime

		if i == N {
			break
		}

		k := currentTime % (R[i] + G[i])

		if k < R[i] {
			currentTime += R[i] - k
		}

		prevPosition = D[i]
	}

	Print(lastDestinationTime)
}

func main() {
	writer = bufio.NewWriter(os.Stdout)
	reader = bufio.NewReader(os.Stdin)
	defer writer.Flush()

	solve()
}
