package main

import (
	"bufio"
	"fmt"
	"os"
)

var writer *bufio.Writer
var reader *bufio.Reader

type Axis struct {
	y int
	x int
}

func solve() {
	arr := make([][]int, 19)

	for i := range arr {
		arr[i] = make([]int, 19)
	}

	for i := 0; i < 19; i++ {
		for j := 0; j < 19; j++ {
			fmt.Fscanf(reader, "%d ", &arr[i][j])
		}
	}

	white_pos := Axis{
		y: 1e10,
		x: 1e10,
	}

	black_pos := Axis{
		y: 1e10,
		x: 1e10,
	}

	// for i := 0; i < 19; i++ {
	// 	fmt.Fprintln(writer, arr[i])
	// }

	ddy := []int{0, 1, 1, -1}
	ddx := []int{1, 0, 1, 1}

	for i := 0; i < 19; i++ {
		for j := 0; j < 19; j++ {
			for d := 0; d < 4; d++ {
				dy := ddy[d]
				dx := ddx[d]

				white_cnt := 0
				black_cnt := 0

				pre_white_cnt := 0
				pre_black_cnt := 0

				if 0 <= i-dy && i-dy < 19 && 0 <= j-dx && j-dx < 19 {
					if arr[i-dy][j-dx] == 1 {
						pre_black_cnt++
					}

					if arr[i-dy][j-dx] == 2 {
						pre_white_cnt++
					}
				}

				if 0 <= i+dy*5 && i+dy*5 < 19 && 0 <= j+dx*5 && j+dx*5 < 19 {
					if arr[i+dy*5][j+dx*5] == 1 {
						pre_black_cnt++
					}

					if arr[i+dy*5][j+dx*5] == 2 {
						pre_white_cnt++
					}
				}

				for k := 0; k < 5; k++ {
					if i+dy*k < 0 || i+dy*k >= 19 || j+dx*k < 0 || j+dx*k >= 19 {
						break
					}
					crt := arr[i+dy*k][j+dx*k]

					// fmt.Println(i+dy*k, j+dx*k, crt)

					switch crt {
					case 1:
						black_cnt++
					case 2:
						white_cnt++
					}
				}

				// fmt.Println(i, j, white_cnt, black_cnt)

				if white_cnt == 5 && pre_white_cnt == 0 {
					white_pos.y = i
					white_pos.x = j
				}

				if black_cnt == 5 && pre_black_cnt == 0 {
					black_pos.y = i
					black_pos.x = j
				}
			}
		}
	}

	if (white_pos.y == 1e10) && (black_pos.y == 1e10) {
		fmt.Fprintln(writer, 0)
		return
	}

	if black_pos.y != 1e10 {
		fmt.Fprintln(writer, 1)
		fmt.Fprintln(writer, black_pos.y+1, black_pos.x+1)
	}

	if white_pos.y != 1e10 {
		fmt.Fprintln(writer, 2)
		fmt.Fprintln(writer, white_pos.y+1, white_pos.x+1)
	}
}

func main() {
	writer = bufio.NewWriter(os.Stdout)
	reader = bufio.NewReader(os.Stdin)
	defer writer.Flush()

	solve()
}
