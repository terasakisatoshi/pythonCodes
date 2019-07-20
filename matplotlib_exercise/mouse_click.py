from matplotlib import pyplot as plt

class LineBuilder:
    def __init__(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_title('click to build line segments')
        #initial value for formal setting
        line, = ax.plot([0], [0])  # empty line
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)

    def __call__(self, event):
        print('click', event)
        if event.inaxes!=self.line.axes: return

        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs[1:], self.ys[1:])
        self.line.figure.canvas.draw()

linebuilder = LineBuilder()

plt.show()