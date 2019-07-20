from multiprocessing import Pool
import random
import time

def estimate_nbr_points_in_quarter_circle(nbr_estimates):
    nbr_trials_in_quarter_unit_circle=0
    for step in range(int(nbr_estimates)):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        is_in_unit_circle = x*x + y*y <=1.0
        nbr_trials_in_quarter_unit_circle+=is_in_unit_circle
    return nbr_trials_in_quarter_unit_circle

def main():
    nbr_samples_in_total=1e8
    nbr_parallel_blocks=8
    pool=Pool(processes=nbr_parallel_blocks)
    nbr_samples_per_worker=nbr_samples_in_total/nbr_parallel_blocks
    print("Making {} samples per worker".format(nbr_samples_per_worker))
    nbr_trials_per_process=[nbr_samples_per_worker] * nbr_parallel_blocks
    start=time.time()
    nbr_in_unit_circles=pool.map(estimate_nbr_points_in_quarter_circle,nbr_trials_per_process)
    pi_estimate=sum(nbr_in_unit_circles) * 4/nbr_samples_in_total
    print("estimated pi {}".format(pi_estimate))
    end=time.time()
    print("Delta: {}".format(end-start))

if __name__ == '__main__':
    main()