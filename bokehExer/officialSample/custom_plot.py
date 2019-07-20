from bokeh.plotting import figure, output_file, show 
import numpy as np 
def main():
    xs=np.linspace(-np.pi,np.pi,100)
    ys_sin=np.sin(xs)
    ys_cos=np.cos(xs)
    output_file("triangular function")
    p=figure(tools="save",
             title="triangular function",
             x_axis_label='x',y_axis_label='sin and cos',
             )
    p.circle(xs,ys_sin,legend="sin",fill_color="white",line_color="blue",size=8)
    p.line(xs,ys_cos,legend="cos",line_color="red",line_dash="4 4")
    show(p)
if __name__ == '__main__':
    main()