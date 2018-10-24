"""
matplotlil.pyplot is the main library for plotting.
plotting usually takes numpy arrays, lists at inputs. df.plt can also be done.
plotting multiple plots on same figure may not look good and we can define axes or do subplotting

Rather than overlaying line plots on common axes, you may prefer to plot different line plots on distinct axes.
The command plt.axes() is one way to do this. In calling plt.axes([xlo, ylo, width, height]), a set of axes is created
and made active with lower corner at coordinates (xlo, ylo) of the specified width and height. Note that these
coordinates can be passed to plt.axes() in the form of a list or a tuple.
The coordinates and lengths are values between 0 and 1 representing lengths relative to the dimensions of the figure.
After issuing a plt.axes() command, plots generated are put in that set of axes.

plt.subplot(m, n, k) to make the subplot grid of dimensions m by n and to make the kth subplot active
(subplots are numbered starting from 1 row-wise from the top left corner of the subplot grid).

plt.xlim() and plt.ylim(). These commands allow you to either zoom or expand the plot or to set the axis ranges to
include important values (such as the origin).

plt.axis((1980,1990,0,75)) would set the extent of the x-axis to the period between 1980 and 1990, and would set
the y-axis extent from 0 to 75% degrees award.

Legends are useful for distinguishing between multiple datasets displayed on common axes. The relevant data are created
using specific line colors or markers in various plot commands. Using the keyword argument label in the plotting
function associates a string to use in a legend.

# Specify the label 'Computer Science'
plt.plot(year, computer_science, color='red', label='Computer Science')

# Specify the label 'Physical Sciences'
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')

# Add a legend at the lower center
plt.legend(loc='lower center')

# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()

Annotate() To add text and arrow into the plot.

# Plot with legend as before
plt.plot(year, computer_science, color='red', label='Computer Science')
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')
plt.legend(loc='lower right')

# Compute the maximum enrollment of women in Computer Science: cs_max
cs_max = computer_science.max()

# Calculate the year in which there was maximum enrollment of women in Computer Science: yr_max
yr_max = year[computer_science.argmax()]

# Add a black arrow annotation
plt.annotate('Maximum', xy=(yr_max, cs_max), xytext=(yr_max+5, cs_max+5), arrowprops=dict(facecolor='black'))

# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()


print(plt.style.available) #to give all the plot styles available
plt.style.use('ggplot') # to use a particular style for plot

"""