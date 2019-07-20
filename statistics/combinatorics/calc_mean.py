"""
Calculating the mean
"""

def calculate_mean(numbers):
    s=sum(numbers)
    N=len(numbers)
    mean=s/N
    return mean

def main():
    donations=[100,60,70,900,100,200,500,500,503,600,1000,1200]
    mean=calculate_mean(donations)
    N=len(donations)
    print("Mean donation over the last {0} days is {1}".format(N,mean))
