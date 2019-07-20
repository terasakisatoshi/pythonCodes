import numpy as np 
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d

class PointsBrowser():
    def __init__(self,fig,ax):
        self.num_ctrl_pt=9
        self.xs=np.linspace(0,255,self.num_ctrl_pt)
        self.ys=np.linspace(0,255,self.num_ctrl_pt)
        ax.plot(np.linspace(0,255,100),np.linspace(0,255,100),'--',color='gray')


        self.lastind=0
        self.selected, =ax.plot([self.xs[0]],[self.ys[0]],'o', ms=12,alpha=0.4,
                            color='red', visible=False)
        self.moved, =ax.plot([self.xs[0]],[self.ys[0]],'o', ms=12,alpha=0.4,
                            color='green', visible=False)

        self.plotted, = ax.plot(self.xs[1:len(self.xs)-1],self.ys[1:len(self.ys)-1],'o',picker=5)
        self.curve, =ax.plot([],[],'-',visible=False)

        self.movedxy=None
        self.fig=fig
        self.ax=ax

        self.pressed_loc=None

    def onpick(self,event):
        if event.artist!=self.plotted:
            return True

        N=len(event.ind)
        if not N:
            return True

        if 0 in event.ind or self.num_ctrl_pt-1 in event.ind:
            return True

        x=event.mouseevent.xdata
        y=event.mouseevent.ydata

        distances=np.hypot(x-self.xs[event.ind],y-self.ys[event.ind])
        indmin=distances.argmin()
        dataind=event.ind[indmin]

        self.pressed_loc = x,y

        self.lastind=dataind
        self.update()


    def on_key_pressed(self,event):
        if self.lastind is None:
            return

        if event.key in ['n', 'right','up']:
            inc=1
        elif event.key in ['p','left','down']:
            inc=-1
        else:
            inc=0
            
        print(event.key)
        self.lastind+=inc
        self.lastind=self.lastind % len(self.xs)
        self.update()

    def update(self):
        if self.lastind is None:
            return 

        dataind=self.lastind
        self.selected.set_visible(True)
        self.selected.set_data(self.xs[dataind],self.ys[dataind])
        self.draw_interpolation()
        self.fig.canvas.draw()

    def on_motion(self,event):

        if self.pressed_loc is None:
            return
        if event.inaxes != self.ax:
            return

        xpress,ypress=self.pressed_loc        
        print(event,xpress,ypress)

        dx=event.xdata-xpress
        dy=event.ydata-ypress

        xnew,ynew=dx+self.xs[self.lastind],dy+self.ys[self.lastind]
        print(xnew,ynew)
        self.moved.set_visible(True)
        self.moved.set_data([xnew],[ynew])
        self.fig.canvas.draw()
        self.movedxy=(xnew,ynew)

    def on_release(self,event):

        if self.movedxy is None:
            return True

        self.pressed_loc=None
        self.moved.set_visible(False)
        self.moved.set_data([self.movedxy[0]],self.movedxy[1])

        self.xs[self.lastind]=self.movedxy[0]
        self.ys[self.lastind]=self.movedxy[1]

        self.plotted.set_data(self.xs,self.ys)

        self.fig.canvas.draw()
        self.update()
        self.movedxy=None

    def draw_interpolation(self):
        approx_func=interp1d(self.xs,self.ys)
        xs4func=np.linspace(np.min(self.xs),np.max(self.xs),num=1000)
        self.curve.set_data(xs4func,approx_func(xs4func))
        self.curve.set_visible(True)




def main():
    fig, ax=plt.subplots(figsize=(5,5))
    ax.set_xlim([0,255])
    ax.set_ylim([0,255])

    browser=PointsBrowser(fig,ax)

    fig.canvas.mpl_connect('pick_event',browser.onpick)
    fig.canvas.mpl_connect('key_press_event',browser.on_key_pressed)
    fig.canvas.mpl_connect('motion_notify_event',browser.on_motion)
    fig.canvas.mpl_connect('button_release_event',browser.on_release)

    plt.show()

if __name__ == '__main__':
    main()