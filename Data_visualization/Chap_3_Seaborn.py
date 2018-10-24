"""
sns.lmplot() - to fit and visualize a simple linear regression between two variables using

## One difference between seaborn and regular matplotlib plotting is that you can pass pandas DataFrames directly to the
plot and refer to each column by name

## Often, you don't just want to see the regression itself but also see the residuals to get a better idea how well the
regression captured the data. Seaborn provides sns.residplot() for that purpose, visualizing how far datapoints diverge
from the regression line

* both sum and mean of residuals is always Zero.
e.g.
    sns.residplot(x='hp', y='mpg', data=auto, color='green', order =2)
Here order controls the order of regression

## When there are more complex relationships between two variables, a simple first order regression is often not
sufficient to accurately capture the relationship between the variables. Seaborn makes it simple to compute and
visualize regressions of varying orders.

For 2nd order regression we can use regplot() function. (sns.lmplot() is a higher-level interface to sns.regplot())
- A principal difference between sns.lmplot() and sns.regplot() is the way in which matplotlib options are passed
(sns.regplot() is more permissive).
- For both sns.lmplot() and sns.regplot(), the keyword order is used to control the order of polynomial regression.
- The function sns.regplot() uses the argument scatter=None to prevent plotting the scatter plot points
e.g.
    sns.regplot(x='weight', y='mpg', data=auto,order=2, scatter=None, color='green', label='order 2')

## Grouping Linear regressions
Often it is useful to compare and contrast trends between different groups. Seaborn makes it possible to apply linear
regressions separately for subsets of the data by applying a groupby operation. Using the hue argument, you can specify
a categorical variable by which to group data observations. The distinct groups of points are used to produce distinct
regressions with different hues in the plot. e.g.
    sns.lmplot('weight', 'hp', data=auto, hue = 'origin', palette='Set1')

## Grouping linear regressions by row or column
Rather than overlaying linear regressions of grouped data in the same plot, we may want to use a grid of subplots.
The sns.lmplot() accepts the arguments row and/or col to arrangements of subplots for regressions.

## Constructing strip plots
Often we want to explore how the distribution of a single continuous variable is affected by a second categorical
variable. Seaborn provides a variety of plot types to perform these types of comparisons between univariate
distributions.
- Strip plot e.g. - sns.stripplot(x='cyl', y='hp', data=auto, jitter=True, size=3)
- Swarm plot e.g. - sns.swarmplot( 'hp','cyl', data = auto, orient = 'h', hue = 'origin')
- Box plot e.g. -
- Violin plot e.g. - sns.violinplot(x='cyl', y='hp',data=auto, orient='h', inner= None, color='lightgray')

## Joint distributions
There are numerous strategies to visualize how pairs of continuous random variables vary jointly. Regression and
residual plots are one strategy. Another is to visualize a bivariate distribution.
- jointplot  e.g. - sns.jointplot('hp', 'mpg', auto)
    The seaborn function sns.jointplot() has a parameter kind to specify how to visualize the joint variation of two
    continuous random variables (i.e., two columns of a DataFrame)
        - kind='scatter' uses a scatter plot of the data points
        - kind='reg' uses a regression plot (default order 1)
        - kind='resid' uses a residual plot
        - kind='kde' uses a kernel density estimate of the joint distribution
        - kind='hex' uses a hexbin plot of the joint distribution

- pairplot e.g. sns.pairplot(auto, hue='origin', kind='reg')
    The function sns.pairplot() constructs a grid of all joint plots pairwise from all pairs of (non-categorical)
    columns in a DataFrame. The syntax is very simple: sns.pairplot(df), where df is a DataFrame. The non-categorical
    columns are identified and the corresponding joint plots are plotted in a square grid of subplots. The diagonal of
    the subplot grid shows the univariate histograms of the individual columns.
"""
# Slice aapl from Nov. 2007 to Apr. 2008 inclusive: view
view = aapl['2007-11':'2008-04']

# Plot the entire series
plt.plot(aapl)
plt.xticks(rotation=45)
plt.title('AAPL: 2001-2011')

# Specify the axes
plt.axes([0.25, 0.5, 0.35, 0.35])

# Plot the sliced series in red using the current axes
plt.plot(view, color='red')
plt.xticks(rotation=45)
plt.title('2007/11-2008/04')
plt.show()

# Load the image into an array: image
image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')

# Display image in top subplot using color map 'gray'
plt.subplot(2,1,1)
plt.title('Original image')
plt.axis('off')
plt.imshow(image, cmap='gray')

# Flatten the image into 1 dimension: pixels
pixels = image.flatten()

# Display a histogram of the pixels in the bottom subplot
plt.subplot(2,1,2)
plt.xlim((0,255))
plt.title('Normalized histogram')
plt.hist(pixels, bins=64, range=(0,256), normed=True, color='red', alpha=0.4)

# Display the plot
plt.show()

"""
A histogram of a continuous random variable is sometimes called a Probability Distribution Function (or PDF). 
The area under a PDF (a definite integral) is called a Cumulative Distribution Function (or CDF). The CDF quantifies 
the probability of observing certain pixel intensities.

Equalizing an image histogram: 
Histogram equalization is an image processing procedure that reassigns image pixel intensities. The basic idea is to 
use interpolation to map the original CDF of pixel intensities to a CDF that is almost a straight line. In essence, 
the pixel intensities are spread out and this has the practical effect of making a sharper, contrast-enhanced image. 
This is particularly useful in astronomy and medical imaging to help us see more features.
"""