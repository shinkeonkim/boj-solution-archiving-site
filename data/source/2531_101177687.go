package main

import (
	"bufio"
	"fmt"
	"os"
)

var writer *bufio.Writer
var reader *bufio.Reader

func solve() {
	var N, d, k, c int
	fmt.Fscanln(reader, &N, &d, &k, &c)

	var l = make([]int, N+k)

	for i := 0; i < N; i++ {
		fmt.Fscanln(reader, &l[i])
	}

	for i := N; i < N+k; i++ {
		l[i] = l[i-N]
	}

	ans := 0

	cnt := map[int]int{}
	category_count := 0

	for i := 0; i < k; i++ {
		cnt[l[i]]++

		if cnt[l[i]] == 1 {
			category_count++
		}
	}

	if cnt[c] > 0 {
		ans = max(ans, category_count)
	} else {
		ans = max(ans, category_count+1)
	}

	for i := k; i < N+k; i++ {
		current := l[i]
		deleting := l[i-k]

		cnt[deleting]--
		if cnt[deleting] == 0 {
			category_count--
		}

		cnt[current]++
		if cnt[current] == 1 {
			category_count++
		}

		if cnt[c] > 0 {
			ans = max(ans, category_count)
		} else {
			ans = max(ans, category_count+1)
		}
		// fmt.Fprintln(writer, category_count, cnt)
	}
	fmt.Fprintln(writer, ans)
}

func main() {
	writer = bufio.NewWriter(os.Stdout)
	reader = bufio.NewReader(os.Stdin)
	defer writer.Flush()

	solve()

}
