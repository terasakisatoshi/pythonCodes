"""Plotting data in basic Python lists as a line plot including zoom, pan, save and 
other tools is simple and straightforward:
"""

from bokeh.plotting import figure, output_file, show

def main():
    xs=list(range(-5,5+1,1))
    ys=list(map(lambda x:x**2,xs))
    output_file("minimum_example.html")
    p=figure()
    p.line(xs,ys)
    show(p)
if __name__ == '__main__':
    main()