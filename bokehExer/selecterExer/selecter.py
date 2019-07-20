from bokeh.io import output_file, show, curdoc
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Select


def update_something(attr, old, new):
    print(attr, old, new)


def main():
    select = Select(title="Select me", value="foo", options=["foo", "bar", "baz", "quit"])
    select.on_change('value', update_something)
    show(widgetbox(select))
    document = curdoc()
    document.add_root(select)

main()
