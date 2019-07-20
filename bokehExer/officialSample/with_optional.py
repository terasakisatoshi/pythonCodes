from bokeh.plotting import figure, output_file, show
import numpy as np 
def main():
    xs=np.linspace(-5,5,num=100,endpoint=True)
    ys=xs**2
    output_file("example_with_option.html")
    p=figure(title="quadratic curve",x_axis_label="x",y_axis_label="y")
    p.line(xs,ys,legend="y=x^2")
    show(p)
if __name__ == '__main__':
    main()