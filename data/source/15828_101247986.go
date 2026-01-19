package main

import (
	"bufio"
	"container/list"
	"fmt"
	"os"
)

var writer *bufio.Writer
var reader *bufio.Reader

type Queue struct {
	v *list.List
}

func NewQueue() *Queue {
	return &Queue{list.New()}
}

func (q *Queue) push(v interface{}) {
	q.v.PushBack(v)
}

func (q *Queue) pop() interface{} {
	front := q.v.Front()

	if front == nil {
		return nil
	}

	return q.v.Remove(front)
}

func (q *Queue) size() int {
	return q.v.Len()
}

func print(a ...interface{}) {
	fmt.Fprintln(writer, a...)
}

func readInt() int {
	var n int
	fmt.Fscanf(reader, "%d\n", &n)
	return n
}

func solve() {
	queue := NewQueue()
	n := readInt()

	for {
		k := readInt()

		if k == -1 {
			break
		}

		if k == 0 {
			queue.pop()
		} else {
			if queue.size() >= n {
				continue
			}
			queue.push(k)
		}
	}

	if queue.size() == 0 {
		print("empty")
	} else {
		for {
			k := queue.pop()

			if k == nil {
				break
			}
			fmt.Fprintf(writer, "%d ", k)
		}
	}
}

func main() {
	writer = bufio.NewWriter(os.Stdout)
	reader = bufio.NewReader(os.Stdin)
	defer writer.Flush()

	solve()
}
