import numpy as np
from matplotlib import pyplot as p
from matplotlib.widgets import Slider

p.subplot(111)
x = np.arange(0, 500, 1)
f = np.sin(x / 100.0)
l11, = p.plot(f)

ax = p.axes([0.25, 0.05, 0.7, 0.03], axisbg='lightgoldenrodyellow')
slider1 = Slider(ax, 'amplitude', -1.0, 1.5, valinit=0)

# the text on the figure
fig_text = p.figtext(0.5, 0.65,  str(slider1.val))


def update(val):
    f = slider1.val * np.sin(x / 100.0)
    l11.set_ydata(f)
    np.set_printoptions(precision=2)

    # update the value of the Text object
    fig_text.set_text(str(slider1.val))

    p.draw()

slider1.on_changed(update)
p.show()
