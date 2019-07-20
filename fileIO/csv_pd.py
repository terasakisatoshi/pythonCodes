import pandas as pd 
import numpy as np 

def main():
    df=pd.read_csv('test_np.csv',skiprows=1)
    print(df)
    df.to_csv('test_pd.csv',header='p,q,r')
    df=pd.read_csv('test_pd.csv',skiprows=1)
    print(df)
　if __name__ == '__main__':
    main()