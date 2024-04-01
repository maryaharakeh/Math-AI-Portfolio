# -*- coding: utf-8 -*-
"""Copy of Hahn Math 24 Lab 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S-aeBUpnQkWgV2dTHO4xjZtxfD25ywWa
"""

import matplotlib.pyplot as plt
#Matplotlib is a powerful Python library for creating visualizations, charts, and plots. It provides a flexible and customizable interface for generating 2D graphics.
from PIL import Image
#The Python Imaging Library (PIL) is a library for opening, manipulating, and saving various image file formats. It provides functions for basic image processing tasks, such as resizing, cropping, rotating, and applying filters.
import imageio.v2 as imageio
#Imageio is a Python library for reading and writing image data. It supports various image formats and provides a simple interface for working with images.

def plot(x):
    fig, ax = plt.subplots()
    im = ax.imshow(x,cmap='gray')
    ax.axis('off')
    fig.set_size_inches(20, 20)
    plt.show()
#the plot() function takes an image represented by a 2D array (x),
#displays it without axis ticks or labels, and sets the figure size before showing the plot.

im = imageio.imread('https://lospec.com/palette-list/st-64-natural-1x.png')
# reads an image using the imageio library
#The resulting array represents the pixel values of the image, which can be further processed or displayed.

plot(im)
#plots the image

im.shape
#the shape of an image array represents its dimensions
#it indicates the number of rows (height) and columns (width) in the image
#the shape includes an additional dimension for the color channels (usually red, green, and blue), so it is represented as (height, width, channels).

plot(im[:,40:41,:])
#This displays a vertical line extracted from an image, spanning from row 0 to the last row and covering only column 40.
#The line’s appearance depends on the pixel values in that column.

im[:,40:41,:]
#gives the array without plotting

im = imageio.imread('https://lospec.com/palette-list/waverator-1x.png')
#reads another image

plot(im)
#plots image

im
#shows image array

import numpy as np
import matplotlib.pyplot as plt

# Binary image
binary_image = np.array([
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
])
#The provided code snippet defines a binary image represented by a 3x3 NumPy array,
#where the value 1 indicates the presence of an object (foreground), and 0 represents the background.

binary_image
#displays array

plt.imshow(binary_image, cmap='gray')
# The provided code snippet displays a binary image using a grayscale colormap. In the image, the value 1 represents the presence of an object (foreground), and 0 represents the background.

# Grayscale image
grayscale_image = np.array([
    [50, 100, 150],
    [200, 255, 200],
    [150, 100, 50]
])
plt.imshow(grayscale_image, cmap='gray', vmin=0, vmax=255)
#The provided code snippet displays a grayscale image using a grayscale colormap.
#In the image, pixel values ranging from 0 to 255 are represented by different shades of gray.

# Grayscale image
grayscale_image = np.array([
    [0.2, 0.4, 0.6],
    [0.8, 1.0, 0.8],
    [0.6, 0.4, 0.2]
])
plt.imshow(grayscale_image, cmap='gray')
#This displays a grayscale image using a grayscale colormap.
#In the image, pixel values ranging from 0 to 1 are represented by different shades of gray.

# RGB image
rgb_image = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 255, 0], [0, 255, 255], [255, 0, 255]],
    [[128, 128, 128], [255, 255, 255], [0, 0, 0]]
])
#This defines an RGB image represented by a 3x3x3 NumPy array.
#Each element in the array corresponds to the red, green, and blue color channels of a pixel.
#For example, the first pixel has RGB values (255, 0, 0) representing pure red.

rgb_image
#displays array

plt.imshow(rgb_image)
#plots image

# RGB image
rgb_image = np.array([
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1], [1, 0, 1]],
    [[0.5, 0.5, 0.5], [1, 1, 1], [0, 0, 0]]
])
#defines an RGB image represented by a 3x3x3 NumPy array.
#Each element in the array corresponds to the red, green, and blue color channels of a pixel. For example, the first pixel has RGB values (1, 0, 0), representing pure red.

# RGB image
rgb_image = np.array([
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1], [1, 0, 1]],

])
#defines an RGB image represented by a 3x3x3 NumPy array. Each element in the array corresponds to the red, green, and blue color channels of a pixel. For example, the first pixel has RGB values (1, 0, 0), representing pure red.

rgb_image
#displays array

plt.imshow(rgb_image*255)
#displays an RGB image (represented by the rgb_image array) after scaling its
#pixel values by 255.
#This scaling effectively maps the original pixel values (ranging from 0 to 1) to the full 8-bit range (0 to 255) for display.



x = np.zeros((2,2,3))
x[:,:,0] = 1
plt.imshow(x)
#The provided code snippet creates a 2x2 RGB image where the red channel (first channel) is set to 1 for all pixels, resulting in a red square.

x = np.zeros((2,2,3))
x[:,:,1] = 1
plt.imshow(x)
# creates a 2x2 RGB image where the green channel (second channel) is set to 1 for all pixels, resulting in a green square.

x = np.zeros((2,2,3))
x[:,:,2] = 1
plt.imshow(x)
#creates a 2x2 RGB image where the blue channel (third channel) is set to 1 for all pixels, resulting in a blue square.

x = np.zeros((2,2,3))
x[:,:,0] = 1
x[:,:,1] = 1
plt.imshow(x)
#creates a 2x2 RGB image where the first and second channels (red and green) are set to 1 for all pixels, resulting in a yellow square.

x = np.zeros((2,2,3))
x[:,:,1] = 1
x[:,:,2] = 1
plt.imshow(x)
#creates a 2x2 RGB image where the green and blue channels are set to 1 for all pixels, resulting in a cyan color.

x = np.zeros((2,2,3))
x[:,:,0] = 1
x[:,:,2] = 1
plt.imshow(x)
#creates a 2x2 RGB image where the red and blue channels are set to 1 for all pixels, resulting in a purple square.

x = np.zeros((2,2,3))
x[:,:,0] = 0.5
x[:,:,1] = 0.5
x[:,:,2] = 0.5
plt.imshow(x)
#The provided code snippet creates a 2x2 gray RGB image where all color channels have a value of 0.5 (gray), resulting in a uniform gray square.

x = np.zeros((2,2,3))
x[:,:,0] = 1
x[:,:,1] = 1
x[:,:,2] = 1
plt.imshow(x)
#creates a 2x2 white RGB image where all color channels (red, green, and blue) are set to 1, resulting in a white square.

x = np.zeros((2,2,3))
x[:,:,0] = 0
x[:,:,1] = 0
x[:,:,2] = 0
plt.imshow(x)
#creates a 2x2 black RGB image where all color channels (red, green, and blue) are set to 0, resulting in a black square.



r = np.random.rand()
#generates a random number between 0 and 1 and assigns it to r

r



r = np.random.rand()
g = np.random.rand()
b = np.random.rand()


x = np.zeros((2,2,3))

x[:,:,0] = r
x[:,:,1] = g
x[:,:,2] = b


plt.imshow(x)
#generates a 2x2 RGB image with random colors for each pixel.
#The red, green, and blue channels are assigned random values between 0 and 1, resulting in a colorful display.

for i in range(5):

    z = np.ones((10,10,3))

    r = np.random.rand()
    g = np.random.rand()
    b = np.random.rand()

    print(r,g,b)

    z[:,:,0] = r
    z[:,:,1] = g
    z[:,:,2] = b

    plt.imshow(z);
    plt.show()
#This generates five random RGB images, each with a different color.
#The red, green, and blue channels are assigned random values between 0 and 1 for each image.
#The images are displayed one after the other.



for i in range(5):

    z1 = np.ones((10,10,3))
    z2 = np.ones((10,10,3))

    r = np.random.rand()
    g = np.random.rand()
    b = np.random.rand()

    z1[:,:,0] = r
    z1[:,:,1] = g
    z1[:,:,2] = b

    z2[:,:,0] = 1-r
    z2[:,:,1] = 1-g
    z2[:,:,2] = 1-b

    z3 = np.hstack((z1,z2))

    plt.imshow(z3);
    plt.show()
#This generates five pairs of random RGB images, each with complementary colors.
#The left image in each pair has random RGB values, while the right image has inverted RGB values (1 minus the original value).
#The resulting images are displayed side by side.



z1 = np.ones((10,10,3))
z1[:,:,0] = np.random.rand()
z1[:,:,1] = np.random.rand()
z1[:,:,2] = np.random.rand()

z2 = np.ones((10,10,3))
z2[:,:,0] = np.random.rand()
z2[:,:,1] = np.random.rand()
z2[:,:,2] = np.random.rand()

zavg = (z1+z2)/2

z3 = np.hstack((z1,zavg,z2))

plt.imshow(z3);
plt.show()
# It creates two 10x10x3 arrays, z1 and z2, filled with ones.
#It then assigns random values to each channel of z1 and z2.
#The average of z1 and z2 is calculated and stored in zavg.
#Finally, the three arrays are horizontally stacked to create a new array z3, which is displayed as an image



z1 = np.ones((10,10,3))
z1[:,:,0] = np.random.rand()
z1[:,:,1] = np.random.rand()
z1[:,:,2] = np.random.rand()

z2 = np.ones((10,10,3))
z2[:,:,0] = np.random.rand()
z2[:,:,1] = np.random.rand()
z2[:,:,2] = np.random.rand()

zavg = (z1+z2)/2

z1a = (z1+zavg)/2
z2a = (z2+zavg)/2

z3 = np.hstack((z1,z1a,zavg,z2a,z2))

plt.imshow(z3);
plt.show()
#The code snippet creates and manipulates arrays z1, z2, and zavg,
#and then horizontally stacks them to form a new array z3, which is displayed as an image



for i in range(100):

    z1 = np.ones((10,10,3))
    z1[:,:,0] = np.random.rand()
    z1[:,:,1] = np.random.rand()
    z1[:,:,2] = np.random.rand()

    z2 = np.ones((10,10,3))
    z2[:,:,0] = np.random.rand()
    z2[:,:,1] = np.random.rand()
    z2[:,:,2] = np.random.rand()

    zavg = (z1+z2)/2

    z1a = (z1+zavg)/2
    z2a = (z2+zavg)/2

    z3 = np.hstack((z1,z1a,zavg,z2a,z2))

    plt.imshow(z3);
    plt.show()
#generates a 10x50 image with random color patterns
#and displays it using matplotlib.



import numpy as np
import matplotlib.pyplot as plt
#This line imports the NumPy library, which provides support for numerical operations and array manipulation.
#This line imports the pyplot module from the Matplotlib library, which is used for creating visualizations and plots.
def recursive_average(colors):
#defines a function that computes the recursive average of a given list of colors.
    """
    Compute the recursive average of the given list of colors.

    Parameters:
    - colors: List of color arrays

    Returns:
    - A new list of color arrays containing the recursive averages.
    """
#A list of color arrays (each representing an RGB color).
#A new list of color arrays containing the recursive averages.

    new_colors = [colors[0]]
    for i in range(1, len(colors)):
        avg_color = (colors[i] + new_colors[-1]) / 2.0
        new_colors.extend([avg_color, colors[i]])
    return new_colors

def generate_recursive_colors_v2(passes):
#This function generates a visualization of two random colors and their recursive averages for a specified number of passes.
    """
    Generate a visualization of 2 random colors and their recursive averages for a number of passes.

    Parameters:
    - passes: Number of times to apply the recursive averaging process

    Returns:
    - An image showing the 2 endpoint colors and their recursive averages.
    """
    # Start with 2 random colors (each with dimensions 10x10x3)
    colors = [np.ones((10,10,3)) for _ in range(2)]
    for color in colors:
        color[:,:,0] = np.random.rand()
        color[:,:,1] = np.random.rand()
        color[:,:,2] = np.random.rand()

    # Apply the recursive averaging for the specified number of passes
    for _ in range(passes):
        colors = recursive_average(colors)

    # Horizontally stack the colors
    result = np.hstack(colors)

    return result
#creates an image that visually demonstrates the recursive averaging process
#for two random colors. The resulting image will show the original colors, their intermediate averages, and the final average color.

for i in range(5):
    img = generate_recursive_colors_v2(i)
    plt.imshow(img)
    plt.axis('off')
    plt.tight_layout()
    plt.show()
#generates and displays a series of images showing the recursive averages of two random colors for different numbers of passes.

import numpy as np
import matplotlib.pyplot as plt

def recursive_average(colors):
#This function computes the recursive average of a given list of colors.
    new_colors = [colors[0]]
#The function initializes a new list called new_colors with the first color from the input list.
    for i in range(1, len(colors)):
        avg_color = (colors[i] + new_colors[-1]) / 2.0
#It then iterates through the remaining colors and computes the average color between each consecutive pair of colors.
        new_colors.extend([avg_color, colors[i]])
#The computed average color is added to new_colors, along with the original color.
    return new_colors

def generate_recursive_colors_v2(passes, initial_colors):
#This function generates a visualization of two random colors and their recursive averages for a specified number of passes.
    colors = initial_colors.copy()

    for _ in range(passes):
        colors = recursive_average(colors)

    result = np.hstack(colors)

    return result
#An image (represented as an array) showing the two endpoint colors and their recursive averages.

initial_colors = [np.ones((10, 10, 3)) for _ in range(2)]
for color in initial_colors:
    color[:,:,0] = np.random.rand()
    color[:,:,1] = np.random.rand()
    color[:,:,2] = np.random.rand()
#Each color array in initial_colors is initialized with random RGB values.

passes_values = [0,1,2,3,4]
imgs = [generate_recursive_colors_v2(p, initial_colors) for p in passes_values]
#The recursive averaging process is then applied passes times using the recursive_average function.

fig, axs = plt.subplots(1, len(passes_values), figsize=(15, 5))
#Finally, the resulting colors are horizontally stacked to create the final image.

for ax, img, p in zip(axs, imgs, passes_values):
    ax.imshow(img)
    ax.axis('off')
    ax.set_title(f'Passes={p}')
#The code initializes initial_colors with two random color arrays.
#It defines a list of passes_values representing the number of passes for the recursive averaging process.
#For each value of passes, it generates an image using generate_recursive_colors_v2.

plt.tight_layout()
plt.show()
#The resulting images are displayed side by side in a row using Matplotlib.
#The purpose of this code is to create a visual representation of the recursive averaging process for two random colors, showcasing how the colors evolve over multiple passes.

"""https://lospec.com/palette-list"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib
import imageio.v2 as imageio
from PIL import Image
#imports libraries

def get_colors_lospec(url):
    im = imageio.imread(url)
    rgb_list = (im/255)[0,:,0:3]
    float_list = list(np.linspace(0,1,len(rgb_list)))
    cdict = dict()
    for num, col in enumerate(['red', 'green', 'blue']):
        col_list = [[float_list[i], rgb_list[i][num], rgb_list[i][num]] for i in range(len(float_list))]
        cdict[col] = col_list
    cmp = mcolors.LinearSegmentedColormap('my_cmp', segmentdata=cdict, N=256)
    return cmp
#code defines a function called get_colors_lospec that retrieves a custom
#colormap (color map) from a specified URL using Lospec image data.
#The colormap is created based on the RGB values extracted from the image,
#and it can be used for visualizations.

url = 'https://lospec.com/palette-list/agb-32x.png'
im = imageio.imread(url)
plt.imshow(im);
#reads, loads, and stores image

url = 'https://lospec.com/palette-list/agb-1x.png'
im = imageio.imread(url)
plt.imshow(im);
#reads, loads, and stores image

url = 'https://lospec.com/palette-list/moondrom-1x.png'
im = imageio.imread(url)
plt.imshow(im);
#reads, loads, and stores image

z = np.random.randint(0,255,size=(10,10))
#generates a 10x10 array filled with random integers between 0 and 255.
#Each element in the array represents a random value within this range.

z
#displays array

plt.imshow(z,cmap='jet')
# displays the 10x10 array z as an image using the ‘jet’ colormap.
# The resulting image will show variations in color intensity based on the values in the array.

plt.imshow(z, cmap=get_colors_lospec(url))
plt.colorbar();
#displays an image using a custom colormap obtained from Lospec image data.
#The color intensity in the image corresponds to the values in the 10x10 array z.
#Additionally, a colorbar is included to indicate the mapping of colors to values.

x, y = np.mgrid[-5:5:0.05, -5:5:0.05]
z = np.sqrt(x**2 + y**2)
#creates a grid of points in the x-y plane with coordinates ranging from -5 to 5 (with a step size of 0.05).
#It then calculates the value of z for each point using the formula
#The resulting z values form a surface that represents the distance from the origin (0,0) to each point in the grid.
#This surface resembles a circular pattern centered at the origin.

x
#displays array

y
#displays array

z = np.sqrt(x**2 + y**2)
#calculates the Euclidean distance from the origin (0,0) to each point in a grid defined by the variables x and y.
# The resulting z values form a circular pattern centered at the origin.

z.shape
#gives array dimensions

plt.imshow(x)
#displays array as an image

plt.imshow(y)
#displays array as an image

z
#displays array

plt.imshow(z, cmap=get_colors_lospec(url));
plt.show()
#display an image using a custom colormap obtained from Lospec image data.
#The color intensity in the image corresponds to the values in the 10x10 array z.
#Additionally, a colorbar is included to indicate the mapping of colors to values.



x, y = np.mgrid[-5:5:0.05, -5:5:0.05]

z = np.sin(3*y)

plt.imshow(z, cmap=get_colors_lospec(url));
plt.show()
#generates a 2D grid of points in the x-y plane with coordinates ranging from -5 to 5 (with a step size of 0.05).
#It then calculates the value of z for each point using the function
#The resulting z values create a pattern that oscillates along the y-axis.
#When visualized using the custom colormap obtained from Lospec image data, the image will exhibit color variations corresponding to these values.

x, y = np.mgrid[-5:5:0.05, -5:5:0.05]

z = np.sin(3*x)
#calculates z in terms of x instead of y

plt.imshow(z, cmap=get_colors_lospec(url));
plt.show()
#In both cases, the resulting z values exhibit oscillations,
#but the orientation of the pattern differs based on whether it is along the x-axis or y-axis.

x, y = np.mgrid[-5:5:0.05, -5:5:0.05]

z = np.sin(3*y)*np.sin(3*x)

plt.imshow(z, cmap=get_colors_lospec(url));
plt.show()
#it multiplies the sine values of both x and y.
#The resulting pattern will exhibit more complex variations due to the multiplication of sine functions.



import matplotlib.pyplot as plt
import imageio
from PIL import Image
from skimage.io import imread
#imports libraries

def plot(x):
    fig, ax = plt.subplots()
    im = ax.imshow(x,cmap='gray')
    ax.axis('off')
    fig.set_size_inches(20, 20)
    plt.show()
#Creates a figure and an axis using plt.subplots().
#Displays the image represented by the input array x using a grayscale colormap.
#Removes the axis labels using ax.axis('off').
#Sets the figure size to 20x20 inches using fig.set_size_inches(20, 20).
#Displays the plot

im = imread('https://raw.githubusercontent.com/imageio/imageio-binaries/master/images/imageio_banner.png')
#assigns image to variable

plot(im)
#displays image

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Octopus2.jpg/800px-Octopus2.jpg"
#assigns image to variable

im = imread(url)
#reads and stores image

plot(im)
#displays image

im.shape
#gives image dimensions with channels

plt.imshow(im[:,:,0],cmap="gray")
#This attempts to display the red channel of the image using a grayscale colormap.
#The resulting image will show variations in shades of gray based on the intensity of the red channel values.

plt.imshow(im[:,:,1],cmap="gray")
##This attempts to display the green channel of the image using a grayscale colormap.
#The resulting image will show variations in shades of gray based on the intensity of the green channel values.

plt.imshow(im[:,:,2],cmap="gray")
##This attempts to display the blue channel of the image using a grayscale colormap.
#The resulting image will show variations in shades of gray based on the intensity of the blue channel values.

r = im[:,:,0] #The resulting array r contains the intensity of red color for each pixel in the image.
g = im[:,:,1] #The array g represents the intensity of green color for each pixel.
b = im[:,:,2] #The array b contains the intensity of blue color for each pixel.

combo = np.hstack([r,g,b])
#horizontally stacks three arrays r, g, and b into a single array called combo.

plt.imshow(combo,cmap="gray")
#displays an image using the grayscale colormap.
#The image is represented by the array combo, which likely contains the combined red, green, and blue color channels.
#When visualized with the grayscale colormap, the resulting image will show variations in shades of gray based on the intensity of the color channels.