from matplotlib import pyplot as plt 
import csv

def no_with():
    f=open("test.txt",'r')
    lines=f.readlines()
    header=lines[0]
    xs=[]
    ys=[]
    for line in lines[1:]:
        x,y=line.split(",")
        xs.append(int(x))
        ys.append(int(y))
    assert not f.closed
    f.close()
    assert f.closed
    plt.plot(xs,ys)
    plt.show()

def using_with():
    with open("test.txt","r") as f:
        lines=f.readlines()
        header=lines[0]
        xs,ys=[],[]
        for line in lines[1:]:
            x,y=line.split(",")
            xs.append(int(x))
            ys.append(int(y))
    assert f.closed
    plt.plot(xs,ys)
    plt.show()

def write_result():
    xs=[x for x in range(10)]
    ys=[]
    for x in xs:
        ys.append(x**2)
    print(ys)
    with open("output.txt","w") as f:
        f.write("x,y\n")
        for x,y in zip(xs,ys):
            f.writelines(",".join([str(x),str(y)]))
            f.write("\n")
def main():
    pass
if __name__ == '__main__':
    main()