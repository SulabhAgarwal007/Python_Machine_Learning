"""
Glyphs:
In Bokeh, visual properties of shapes are called glyphs. The visual properties of these glyphs such as position or
color can be assigned single values, for example x=10 or fill_color='red'. Other kind of values tht glyph properties
can be set to normal usage are Sequences (lists, arrays)

"""

# Import figure from bokeh.plotting
from bokeh.plotting import figure
import pandas as pd

# Import output_file and show from bokeh.io
from bokeh.io import output_file, show

# Import ColumnDataSource
from bokeh.plotting import ColumnDataSource

data = pd.read_csv('literacy_birth_rate.csv')
data.dropna()
print(data.head())
fertility = data['fertility']
female_literacy = data['female literacy']
print(type(fertility), type(female_literacy))

fertility = list(fertility)
female_literacy = list(female_literacy)
print(type(fertility), type(female_literacy))

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a circle glyph to the figure p
p.circle(fertility, female_literacy, color='red', size=10, alpha=0.5)

# Call the output_file() function and specify the name of the file
output_file('fert_lit.html')

# Display the plot
show(p)

# print(fertility[1:10])
# print(female_literacy[1:10])
# print(data.info())

"""
Patches
In Bokeh, extended geometrical shapes can be plotted by using the patches() glyph function. The patches glyph takes as 
input a list-of-lists collection of numeric values specifying the vertices in x and y directions of each distinct 
patch to plot.
"""
# Plotting data from numpy
# Import numpy as np
import numpy as np

# Create array using np.linspace: x
x = np.linspace(0, 5, 100)

# Create array using np.cos: y
y = np.cos(x)

plot = figure()
# Add circles at x and y
plot.circle(x, y)

# Specify the name of the output file and show the result
output_file('numpy.html')
show(plot)

# Pandas plotting via Bokeh

df = pd.read_csv('auto-mpg.csv')


# Create the figure: p
plot2 = figure(x_axis_label='HP', y_axis_label='MPG')

# Plot mpg vs hp by color
plot2.circle(df['hp'], df['mpg'], color=df['color'], size=10 )

# Specify the name of the output file and show the result
output_file('auto-df.html')
show(plot2)

"""
The ColumnDataSource is a table-like data object that maps string column names to sequences (columns) of data. 
It is the central and most common data structure in Bokeh.
You can create a ColumnDataSource object directly from a Pandas DataFrame by passing the DataFrame to the class 
initializer.
"""

source = ColumnDataSource(df)
plot3 = figure(x_axis_label='HP_col_data', y_axis_label='MPG_col_data')
plot3.circle(x='hp', y='mpg', source=source, size=8, color='color')

output_file('col_data.html')
show(plot3)

# Selection and non-selection Glyphs

src = ColumnDataSource(pd.read_csv('sprint.csv'))

# Create a figure with the "box_select" tool: p
plot4 = figure(x_axis_label='Year', y_axis_label='Time', tools='box_select')

# Add circle glyphs to the figure p with the selected and non-selected properties
plot4.circle(x='Year', y='Time', source=src, selection_color='red', nonselection_alpha=0.1)

# Specify the name of the output file and show the result
output_file('selection_glyph.html')
show(plot4)

"""
# import the HoverTool
from bokeh.models import HoverTool

# Add circle glyphs to figure p
p.circle(x, y, size=10,
         fill_color='grey', alpha=0.1, line_color=None,
         hover_fill_color='firebrick', hover_alpha=0.5,
         hover_line_color='white')

# Create a HoverTool: hover
hover = HoverTool(tooltips=None, mode='vline')

# Add the hover tool to the figure p
p.add_tools(hover)

# Specify the name of the output file and show the result
output_file('hover_glyph.html')
show(p)

"""

# Categorical color mapper
# Import CategoricalColorMapper from bokeh.models
from bokeh.models import CategoricalColorMapper

# Convert df to a ColumnDataSource: source
src1 = ColumnDataSource(pd.read_csv('auto-mpg.csv'))

# Make a CategoricalColorMapper object: color_mapper
color_mapper = CategoricalColorMapper(factors=['Europe', 'Asia', 'US'],
                                      palette=['red', 'green', 'blue'])
plot5 = figure()
# Add a circle glyph to the figure p
plot5.circle('weight', 'mpg', source=src1,
            color=dict(field='origin', transform=color_mapper),
            legend='origin')

# Specify the name of the output file and show the result
output_file('colormap.html')
show(plot5)
