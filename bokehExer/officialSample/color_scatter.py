import numpy as np

from bokeh.plotting import figure, show, output_file

N = 100
xs = np.linspace(-np.pi, np.pi, 11)
ys = xs
Xs, Ys = np.meshgrid(xs, ys)
Xs, Ys = Xs.flatten(), Ys.flatten()

colors = [
    "#%02x%02x%02x" % (int(r), int(g), 200) for r, g in zip(500+100*(Xs+10), 300+100*(Ys+10))
]

TOOLS = "hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

p = figure(tools=TOOLS,
           x_range=(-np.pi*np.sqrt(2)-1, np.pi*np.sqrt(2)+1),
           y_range=(-np.pi*np.sqrt(2)-1, np.pi*np.sqrt(2)+1))

p.scatter(Xs, Ys,
          fill_color=colors, fill_alpha=0.6,
          line_color=None)

output_file("color_scatter.html", title="color_scatter.py example")

show(p)  # open a browser
