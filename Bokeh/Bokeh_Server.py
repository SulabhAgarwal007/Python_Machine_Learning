"""
Understanding Bokeh apps
The main purpose of the Bokeh server is to synchronize python objects with web applications in a browser, so that rich,
interactive data applications can be connected to powerful PyData libraries such as NumPy, SciPy, Pandas,
and scikit-learn.


"""

# Perform necessary imports
from bokeh.io import curdoc # current document
from bokeh.plotting import figure

# Create a new plot: plot
plot = figure()

# Add a line to the plot
plot.line([1,2,3,4,5], [2,5,4,6,7])

# Add the plot to the current document
curdoc().add_root(plot)

"""How to run it:
goto cmd prompt, navigate to the file path, then type
bokeh serve --show filename.py
"""

# Adding callbacks to sliders
# Callbacks are functions that a user can define, like def callback(attr, old, new), that can be called automatically
# when some property of a Bokeh object (e.g., the value of a Slider) changes.

"""
# Create ColumnDataSource: source
source = ColumnDataSource(data={'x': x, 'y': y})

# Add a line to the plot
plot.line('x', 'y', source=source)

# Define a callback function: callback
def callback(attr, old, new):

    # Read the current value of the slider: scale
    scale = slider.value

    # Compute the updated y using np.sin(scale/x): new_y
    new_y = np.sin(scale/x)

    # Update source with the new data values
    source.data = {'x': x, 'y': new_y}

# Attach the callback to the 'value' property of slider
slider.on_change('value', callback)

# Create layout and add to current document
layout = column(widgetbox(slider), plot)
curdoc().add_root(layout)
"""

"""Buttons
# Create a Button with label 'Update Data'
button = Button(label='Update Data')

# Define an update callback with no arguments: update
def update():

    # Compute new y values: y
    y = np.sin(x) + np.random.random(N)

    # Update the ColumnDataSource data dictionary
    source.data = {'x': x, 'y': y}

# Add the update callback to the button
button.on_click(update)

# Create layout and add to current document
layout = column(widgetbox(button), plot)
curdoc().add_root(layout)
"""