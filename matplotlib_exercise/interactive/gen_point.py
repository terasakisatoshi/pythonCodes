from matplotlib import pyplot as plt


class PointGenerator:

    def __init__(self):
        fig, ax = plt.subplots()
        self.fig = fig
        self.ax = ax
        self.ax.set_xlim([0, 3])
        self.ax.set_ylim([0, 3])
        self.ax.set_title("click to build point")
        self.cid = self.fig.canvas.mpl_connect(
            "button_press_event", self.gen_pt)

    def gen_pt(self, event):
        print("click", event)
        if event.inaxes != self.ax:
            # do nothing
            return
        print('try to plot')
        self.ax.plot(event.xdata, event.ydata, 'o')
        self.ax.figure.canvas.draw()


def main():
    generator = PointGenerator()
    plt.show()
if __name__ == '__main__':
    main()
