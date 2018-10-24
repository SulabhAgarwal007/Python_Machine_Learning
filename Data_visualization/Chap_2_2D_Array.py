import  numpy as np
import matplotlib.pyplot as plt

a = np.array([1,2,3,4,5,5,67,7,88,9])

#Slicing of a numpy array a[start:stop:slice interval]
print(a[1::2])

a = np.linspace(-2,2,3)
b = np.linspace(-1,1,5)

""" MeshGrid from Matlab Documentation
[X,Y] = meshgrid(x,y) returns 2-D grid coordinates based on the coordinates contained in vectors x and y. 
X is a matrix where each row is a copy of x, and Y is a matrix where each column is a copy of y. 
The grid represented by the coordinates X and Y has length(y) rows and length(x) columns.
"""

X,Y = np.meshgrid(a, b)
print(Y)

# another way to create mesh grid
Y,X = np.meshgrid(range(10),range(20))

# Array orientation
A = np.array([[1, 0, -1], [2, 0, 1], [1, 1, 1]])
print("\n {}".format(A))
plt.pcolor(A, cmap='Blues')
plt.colorbar()
plt.title("Check the orientation of array and the pixels")
plt.show()

"""
plt.imshow()
plt.pcolor()
plt.contour()
plt.contourf()

Some matplotlib colormaps have unique names such as 'jet', 'coolwarm', 'magma' and 'viridis'.
Others have a naming scheme based on overall color such as 'Greens', 'Blues', 'Reds', and 'Purples'.
Another four colormaps are based on the seasons, namely 'summer', 'autumn', 'winter' and 'spring'.
You can insert the option cmap=<name> into most matplotlib functions to change the color map of the resulting plot.

Example:
# Create a filled contour plot with a color map of 'winter'
plt.subplot(2,2,4)
plt.contourf(X,Y,Z,20, cmap='winter')
plt.colorbar()
plt.title('Winter')
"""

""" 2D Array's
Function to visualize 2-D histograms is plt.hist2d().
- You specify the coordinates of the points using plt.hist2d(x,y) assuming x and y are two vectors of the same length.
- You can specify the number of bins with the argument bins=(nx, ny) where nx is the number of bins to use in the 
horizontal direction and ny is the number of bins to use in the vertical direction.
- You can specify the rectangular region in which the samples are counted in constructing the 2D histogram. 
The optional parameter required is range=((xmin, xmax), (ymin, ymax)) where
xmin and xmax are the respective lower and upper limits for the variables on the x-axis and
ymin and ymax are the respective lower and upper limits for the variables on the y-axis. 
Notice that the optional range argument can use nested tuples or lists.
e.g.
plt.hist2d(hp,mpg, bins=(20, 20), range=((40, 200),(15, 40)))

##Hexagonal Bins
As an alternative, the function plt.hexbin() uses hexagonal bins.
- The optional gridsize argument (default 100) gives the number of hexagons across the x-direction used in the hexagonal 
tiling. If specified as a list or a tuple of length two, gridsize fixes the number of hexagon in the x- and y-directions
respectively in the tiling.
- The optional parameter extent=(xmin, xmax, ymin, ymax) specifies rectangular region covered by the hexagonal tiling. 
In that case, xmin and xmax are the respective lower and upper limits for the variables on the x-axis and ymin and ymax 
are the respective lower and upper limits for the variables on the y-axis.
e.g.
 plt.hexbin(hp, mpg, gridsize=(15, 12), extent=(40, 235, 8, 48))
"""

"""Color Images
Color images such as photographs contain the intensity of the red, green and blue color channels.
- To read an image from file, use plt.imread() by passing the path to a file, such as a PNG or JPG file.
-  The color image can be plotted as usual using plt.imshow().
The resulting image loaded is a NumPy array of three dimensions. The array typically has dimensions M x N x 3, where 
M x N is the dimensions of the image. The third dimensions are referred to as color channels (typically red, green, and 
blue). The color channels can be extracted by Numpy array slicing.

# Load the image into an array: img
img = plt.imread('480px-Astronaut-EVA.jpg')

# Print the shape of the image
print(img.shape)

# Compute the sum of the red, green and blue channels: intensity
intensity = img.sum(axis=2)

# Print the shape of the intensity
print(intensity.shape)

# Display the intensity with a colormap of 'gray'
plt.imshow(intensity, cmap='gray')

# Add a colorbar
plt.colorbar()

# Hide the axes and show the figure
plt.axis('off')
plt.show()

The ratio of the displayed width to height is known as the image aspect and the range used to label the x- and y-axes is
known as the image extent. The default aspect value of 'auto' keeps the pixels square and the extents are automatically
computed from the shape of the array if not specified otherwise.
"""
