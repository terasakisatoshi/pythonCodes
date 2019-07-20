import pandas as pd  
import numpy as np 

import matplotlib as mlp 
from matplotlib import pyplot as plt 
import datetime

def main():
    s=pd.Series([i for i in range(10)],dtype=int)
    word='abcdefghijklmnopqrstuvwxyz'
    s.index=[word[i] for i in range(10)]
    s.name="alphabet index"
    print(s)
    print(s.describe())

if __name__ == '__main__':
    main()