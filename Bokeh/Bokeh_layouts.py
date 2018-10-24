from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
import pandas as pd

source = ColumnDataSource(pd.read_csv('literacy_birth_rate.csv'))

# Create the first figure: p1
p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a circle glyph to p1
p1.circle('fertility', 'female literacy', source=source)

# Create the second figure: p2
p2 = figure(x_axis_label='population', y_axis_label='female_literacy (% population)')

# Add a circle glyph to p2
p2.circle('population', 'female literacy', source=source)

# Put p1 and p2 into a horizontal row: layout
layout = row(p1, p2)

# Specify the name of the output_file and show the result
output_file('fert_row.html')
show(layout)


""" Grid Plot example. Note: here p1, p2, p3, p4 are plots pre-defined
# Import gridplot from bokeh.layouts
from bokeh.layouts import gridplot

# Create a list containing plots p1 and p2: row1
row1 = [p1, p2]

# Create a list containing plots p3 and p4: row2
row2 = [p3, p4]

# Create a gridplot using row1 and row2: layout
layout = gridplot([row1, row2])

# Specify the name of the output_file and show the result
output_file('grid.html')
show(layout)

#####Panels
# Import Panel from bokeh.models.widgets
from bokeh.models.widgets import Panel

# Create tab1 from plot p1: tab1
tab1 = Panel(child=p1, title='Latin America')

# Create tab2 from plot p2: tab2
tab2 = Panel(child=p2, title='Africa')

# Create tab3 from plot p3: tab3
tab3 = Panel(child=p3, title='Asia')

# Create tab4 from plot p4: tab4
tab4 = Panel(child=p4, title='Europe')

# Import Tabs from bokeh.models.widgets

from bokeh.models.widgets import Tabs

# Create a Tabs layout: layout
layout = Tabs(tabs=[tab1, tab2, tab3, tab4])

# Specify the name of the output_file and show the result
output_file('tabs.html')
show(layout)

"""

# Plot linking: Linked axes
# Linking axes between plots is achieved by sharing range objects. we do is by setting x_range and y_range of each plot
# equal to other
# for e.g. p1.x_range = p2. x_range = p3.x_range  p1.y_range = p2.y_range = p3.y_range

"""
Linked brushing
By sharing the same ColumnDataSource object between multiple plots, selection tools like BoxSelect and LassoSelect will 
highlight points in both plots that share a row in the ColumnDataSource.
    
# Create ColumnDataSource: source
source = ColumnDataSource(data)

# Create the first figure: p1
p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female literacy (% population)',
            tools='box_select,lasso_select')

# Add a circle glyph to p1
p1.circle('fertility', 'female literacy', source=source)

# Create the second figure: p2
p2 = figure(x_axis_label='fertility (children per woman)', y_axis_label='population (millions)',
            tools='box_select,lasso_select')

# Add a circle glyph to p2
p2.circle('fertility', 'population', source=source)

# Create row layout of figures p1 and p2: layout
layout = row(p1, p2)

# Specify the name of the output_file and show the result
output_file('linked_brush.html')
show(layout)
"""

# Legends: Legends can be defined while defining the figure for e.g. p.circle(...., legend = 'LA')
# legend properties can then be modified on p, for e.g. p.legend.position = 'bottom_left'

# Hover tooltips for exposing details
# When configuring hover tools, certain pre-defined fields such as mouse position or glyph index can be accessed with
# $-prefixed names, for example $x, $index. But tooltips can display values from arbitrary columns in a
# ColumnDataSource.
"""
# Import HoverTool from bokeh.models
from bokeh.models import HoverTool

# Create a HoverTool object: hover
hover = HoverTool(tooltips=[('Country', '@Country')])

# Add the HoverTool object to figure p
p.add_tools(hover)

# Specify the name of the output_file and show the result
output_file('hover.html')
show(p)
"""


