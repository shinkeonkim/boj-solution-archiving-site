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

func Solve() {
	var a, b, c, d int

	fmt.Fscan(reader, &a, &b, &c, &d)

	ret1 := (a+b <= d)
	ret2 := (c <= d)

	if ret1 && ret2 {
		Print("~.~")
	} else if !ret1 && !ret2 {
		Print("T.T")
	} else if ret1 && !ret2 {
		Print("Shuttle")
	} else {
		Print("Walk")
	}
}

func main() {
	writer = bufio.NewWriter(os.Stdout)
	reader = bufio.NewReader(os.Stdin)
	defer writer.Flush()

	Solve()
}
