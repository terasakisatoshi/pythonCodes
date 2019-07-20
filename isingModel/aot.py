from numba.pycc import CC 
cc=CC('pyising')

@cc.export('ising2d_sum_of_adjacent_spins','i8(i8[:,:],i8,i8,i8,i8)')
def ising2d_sum_of_adjacent_spins(s, m, n, i, j):
    i_bottom = i+1 if i+1 < m else 0
    i_top = i-1 if i-1 >= 0 else m-1
    j_right = j+1 if j+1 < n else 0
    j_left = j-1 if j-1 >= 0 else n-1
    return s[i_bottom][j]+s[i_top][j]+s[i][j_right]+s[i][j_left]

if __name__ == '__main__':
    cc.compile()