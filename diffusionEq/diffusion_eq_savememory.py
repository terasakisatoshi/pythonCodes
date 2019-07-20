import time
#global variable
grid_shape=(1024,1024)
epsilon_param=(0.1,0.1,0.1)
D=1
def evolve2d(grid,out):
    xmax,ymax=grid_shape
    dx,dy,dt=epsilon_param
    for i in range(xmax):
        for j in range(ymax):
            #usingPeriodic boundary conditions
            #grid_xx stands for 2nd partial derivative with respect to x
            grid_xx = grid[(i+1)%xmax][j] + grid[(i-1)%xmax][j] - 2.0 *grid[i][j]
            #grid_yy stands for 2nd partial derivative with respect to y
            grid_yy = grid[i][(j+1)%ymax] + grid[i][(j-1)%ymax] - 2.0 *grid[i][j]
            out[i][j] = grid[i][j] + D * (grid_xx/(dx*dx) + grid_yy/(dx*dx)) * dt

def run_experiment(num_iterations):
    #set initial value
    xmax,ymax=grid_shape
    grid    =[[0.0,]*ymax for x in range(xmax)]
    next_grid=[[0.0,]*ymax for x in range(xmax)]
    block_low  = int(grid_shape[0] * 0.4)
    block_high = int(grid_shape[1] * 0.5)
    for i in range(block_low,block_high):
        for j in range(block_low,block_high):
            grid[i][j]=0.005

    start = time.time()
    for i in range(num_iterations):
        evolve2d(grid,next_grid)
        #recycle grid to save memory
        grid,next_grid=next_grid,grid
    return time.time() -start

def main():
    print(run_experiment(10))
    print(run_experiment(10))
    print(run_experiment(10))
    print(run_experiment(10))
    print(run_experiment(10))
    """
    13.424503087997437
    13.549596309661865
    13.273629665374756
    13.345857620239258
    13.912915706634521
    [Finished in 67.9s]
    """

if __name__ == '__main__':
    main()