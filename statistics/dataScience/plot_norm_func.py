from scipy import stats
import pandas as pd
from matplotlib import pyplot as plt
#'h28_hoken_toukei_02.xlsx' can be taken from
# https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00400002&tstat=000001011648&cycle=0&tclass1=000001098858&tclass2=000001098859


def main():
    df = pd.read_excel("h28_hoken_toukei_02.xlsx")
    df = df.iloc[61:110, [1, 14]].astype(float)
    df = df.rename(columns={"２ 身長の年齢別分布（2-1）": "height",
                            "Unnamed: 14": "permil"})
    u = [stats.norm.pdf(x=i, loc=170.7, scale=5.81) *
         1000.0 for i in df["height"]]
    df['norm'] = u

    ax = df.plot.scatter(x="height", y="permil",
                         color="black", marker='x', label="height stat")
    df.plot(x="height", y="norm", color="black",
            kind="line", ax=ax, label="N(170.7,5.81)")
    plt.show()

if __name__ == '__main__':
    main()
