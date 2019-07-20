import matplotlib.pyplot as plt 
import numpy as np 

def linear_form(A,xy):
    print(xy)
    return np.array(xy).dot(A.T)

def plot_vector(ax,uv,x=0,y=0,color='black'):
    ax.quiver(x,y,uv[:,0],uv[:,1],c=color,angles='xy',scale_units='xy',scale=1)

phi=np.pi*22.5/180

def main():
    fig,ax=plt.subplots()
    ax.set_xlim([-0.5,1.5])
    ax.set_ylim([-0.5,1.5])
    plot_vector(ax,np.array([[0,1]]))
    plot_vector(ax,np.array([[1,0]]))
    A=np.array([[np.cos(phi),-np.sin(phi)],
                [np.sin(phi), np.cos(phi)]])
    uv1=linear_form(A,np.array([[1,0]]))
    uv2=linear_form(np.linalg.inv(A),np.array([[0,1]]))
    plot_vector(ax,uv1)
    plot_vector(ax,uv2)
    uvs=np.array([[0,0.3] for _ in range(1,11)])
    xs=[u/10.0 for u in range(1,11)]
    plot_vector(ax,uvs,x=xs)
    xx=linear_form(A,[[x,0] for x in xs])
    print(xx)
    plot_vector(ax,uvs,x=xx)
    ax.grid()
    plt.show()


if __name__ == '__main__':
    main()

