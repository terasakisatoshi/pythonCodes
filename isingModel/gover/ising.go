package main

import (
	//"fmt"
	"github.com/gonum/matrix/mat64"
	"math"
	"math/rand"
)

const N int = 100

func ising2dSumOfAdjacentSpins(s *mat64.Dense, m, n, i, j int) int {
	var i_bottom, i_top int
	var j_right, j_left int
	if i+1 < m {
		i_bottom = i + 1
	} else {
		i_bottom = 0
	}
	if i-1 >= 0 {
		i_top = i - 1
	} else {
		i_top = m - 1
	}
	if j+1 < n {
		j_right = j + 1
	} else {
		j_right = 0
	}
	if j-1 >= 0 {
		j_left = j - 1
	} else {
		j_left = n - 1
	}
	return int(s.At(i_bottom, j) + s.At(i_top, j) + s.At(i, j_right) + s.At(i, j_left))
}

func ising2dSweep(s *mat64.Dense, beta float64, niter int) {
	m, n := s.Dims()
	prob := []float64{math.Exp(-2 * beta * (-4)), math.Exp(-2 * beta * (-3)), math.Exp(-2 * beta * (-2)), math.Exp(-2 * beta * (-1)), 1,
		math.Exp(-2 * beta * (1)), math.Exp(-2 * beta * (2)), math.Exp(-2 * beta * (3)), math.Exp(-2 * beta * (4))}
	for iter := 0; iter < niter; iter++ {
		for i := 0; i < m; i++ {
			for j := 0; j < n; j++ {
				s1 := s.At(i, j)
				k := int(s1) * ising2dSumOfAdjacentSpins(s, m, n, i, j)
				if rand.Float64() < prob[k+4] {
					s.Set(i, j, -s1)
				} else {
					s.Set(i, j, s1)
				}
			}
		}
	}

}

func main() {
	//initialization
	s := mat64.NewDense(N, N, nil)
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if rand.Float32() < 0.5 {
				s.Set(i, j, -1)
			} else {
				s.Set(i, j, 1)
			}
		}
	}
	var beta float64 = math.Log(1+math.Sqrt(2.0)) / 2
	ising2dSweep(s, beta, int(1e4))
	//fmt.Println(s)
}
