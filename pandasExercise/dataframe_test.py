import pandas as pd 

df=pd.DataFrame([[0,1],
                 [1,2],
                 [3,4],
                 [5,6],
                 [7,8]]
                 ,columns=['x','y'],index=[i for i in range(5)])
print(df)

print(df.ix[1]['y']) # 2

print(df.ix[[1,3]]['y'])