# Perform necessary imports
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.layouts import row
import pandas as pd

data = pd.read_csv('literacy_birth_rate.csv')
fertility = data['fertility'].values
female_literacy = data['female literacy']
population = data['population']

# Create ColumnDataSource: source
source = ColumnDataSource(data={
    'x': fertility,
    'y': female_literacy
})

# Create a new plot: plot
plot = figure()

# Add circles to the plot
plot.circle('x', 'y', source=source)


def update_plot(attr, old, new):  # Define a callback function: update_plot
    # If the new Selection is 'female_literacy', update 'y' to female_literacy
    if new == 'female_literacy':
        source.data = {
            'x': fertility,
            'y': female_literacy
        }
    # Else, update 'y' to population
    else:
        source.data = {
            'x': fertility,
            'y': population
        }


# Create a dropdown Select widget: select
select = Select(title="distribution", options=['female_literacy', 'population'], value='female_literacy')

# Attach the update_plot callback to the 'value' property of select
select.on_change('value', update_plot)

# Create layout and add to current document
layout = row(select, plot)
curdoc().add_root(layout)
