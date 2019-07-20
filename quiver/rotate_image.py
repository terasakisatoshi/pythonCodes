import numpy as np 
from matplotlib import pyplot as plt 
import matplotlib.cm as cm
def plot_vector(ax,uv,x=0,y=0,color=0):
    return ax.quiver(x,y,uv[0],uv[1],cm.hot(color,1),angles='xy',scale_units='xy',scale=1)

def trans(A,xy):
    return xy.dot(A.T)
def rot(deg):
    phi=np.pi*deg/180
    return np.array([[np.cos(phi),-np.sin(phi)],
                    [np.sin(phi), np.cos(phi)]])
phi=np.pi*22.5/180
Phi=np.array([[np.cos(-phi),-np.sin(phi)],
                    [np.sin(-phi), np.cos(phi)]])
def main():
    fig,ax=plt.subplots()
    ax.set_xlim([-0.5,2.5])
    ax.set_ylim([-0.5,2.5])
    deg=0
    A=rot(-deg)@Phi@np.array([[np.sqrt(2),0],[0,1]])@rot(deg)
    xy1=np.array([1,0])
    transxy1=trans(A,xy1)
    xy2=np.array([0,1])
    transxy2=trans(A,xy2)
    xy3=np.array([1,1])
    transxy3=trans(A,xy3)
    xy4=trans(rot(30),np.array([1,0]))
    transxy4=trans(A,xy4)

    plot_vector(ax,xy1,color=0.1)
    plot_vector(ax,transxy1,color=0.1)
    plot_vector(ax,xy2,color=0.2)
    plot_vector(ax,transxy2,color=0.2)
    plot_vector(ax,xy3,color=0.3)
    plot_vector(ax,transxy3,color=0.3)
    plot_vector(ax,xy4,color=0.4)
    plot_vector(ax,transxy4,color=0.4)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
if __name__ == '__main__':
    main()