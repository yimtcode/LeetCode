package main

import (
	"fmt"
)

func main() {
	board := [][]byte{
		{'5', '3', '.', '.', '7', '.', '.', '.', '.'},
		{'6', '.', '.', '1', '9', '5', '.', '.', '.'},
		{'.', '9', '8', '.', '.', '.', '.', '6', '.'},
		{'8', '.', '.', '.', '6', '.', '.', '.', '3'},
		{'4', '.', '.', '8', '.', '3', '.', '.', '1'},
		{'7', '.', '.', '.', '2', '.', '.', '.', '6'},
		{'.', '6', '.', '.', '.', '.', '2', '8', '.'},
		{'.', '.', '.', '4', '1', '9', '.', '.', '5'},
		{'.', '.', '.', '.', '8', '.', '.', '7', '9'},
	}

	b := isValidSudoku(board)
	fmt.Println(b)
}

var (
	width  = 9
	height = 9
)

// 验证数独
// 1.验证每行是否包含1-9
// 2.验证每列是否包含1-9
// 3.验证每个3x3是否包含1-9
func isValidSudoku(board [][]byte) bool {
	validator := map[byte]struct{}{}

	// 验证行
	for y := 0; y < height; y++ {
		for x := 0; x < width; x++ {
			num := board[y][x]
			if num == '.' {
				continue
			}
			_, ok := validator[num]
			if ok {
				return false
			}
			validator[num] = struct{}{}

		}
		// 清空数量
		cleanMap(validator)
	}

	// 验证列
	for x := 0; x < width; x++ {
		for y := 0; y < height; y++ {
			num := board[y][x]
			if num == '.' {
				continue
			}
			_, ok := validator[num]
			if ok {
				return false
			}
			validator[board[y][x]] = struct{}{}
		}
		// 清空数量
		cleanMap(validator)
	}

	// 验证3 * 3
	for x := 0; x < width; x += 3 {
		for y := 0; y < height; y += 3 {
			for offsetX := 0; offsetX < 3; offsetX++ {
				for offsetY := 0; offsetY < 3; offsetY++ {
					currentX := x + offsetX
					currentY := y + offsetY

					num := board[currentY][currentX]
					if num == '.' {
						continue
					}
					_, ok := validator[num]
					if ok {
						return false
					}
					validator[num] = struct{}{}
				}
			}
			// 清空数量
			cleanMap(validator)
		}
	}

	return true
}

// 清空map
func cleanMap(m map[byte]struct{}) {
	for k, _ := range m {
		delete(m, k)
	}
}
