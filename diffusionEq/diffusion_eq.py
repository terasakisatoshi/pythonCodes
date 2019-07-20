import time
#global variable
grid_shape=(1024,1024)
epsilon_param=(0.1,0.1,0.1)
D=1
def evolve2d(grid):
    xmax,ymax=grid_shape
    dx,dy,dt=epsilon_param
    new_grid=[[0.0,]*ymax for x in range(xmax)]

    for i in range(xmax):
        for j in range(ymax):
            #usingPeriodic boundary conditions
            #grid_xx stands for 2nd partial derivative with respect to x
            grid_xx = grid[(i+1)%xmax][j] + grid[(i-1)%xmax][j] - 2.0 *grid[i][j]
            #grid_yy stands for 2nd partial derivative with respect to y
            grid_yy = grid[i][(j+1)%ymax] + grid[i][(j-1)%ymax] - 2.0 *grid[i][j]
            new_grid[i][j] = grid[i][j] + D * (grid_xx/(dx*dx) + grid_yy/(dx*dx)) * dt
    return new_grid

def run_experiment(num_iterations):
    #set initial value
    xmax,ymax=grid_shape
    grid=[[0.0,]*ymax for x in range(xmax)]
    block_low  = int(grid_shape[0] * 0.4)
    block_high = int(grid_shape[1] * 0.5)
    for i in range(block_low,block_high):
        for j in range(block_low,block_high):
            grid[i][j]=0.005

    start = time.time()
    for i in range(num_iterations):
        grid = evolve2d(grid)
    return time.time() -start

def main():    
    print(run_experiment(10))
    print(run_experiment(10))
    print(run_experiment(10))
    print(run_experiment(10))
    print(run_experiment(10))

if __name__ == '__main__':
    main()
    """
    14.238842964172363
    13.934774398803711
    13.391046524047852
    14.556063652038574
    14.198774814605713
    [Finished in 70.5s]
    """