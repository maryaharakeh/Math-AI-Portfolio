# -*- coding: utf-8 -*-
"""Copy of Hahn Math 24 Lab 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vymmwxr024hGRQh3jSt3VhV_xY1x4rDd
"""

import numpy as np
import matplotlib.pyplot as plt

"""Label This"""

numbers= np.array([1,2,2,3,3,3,4,4,4,4])
plt.hist(numbers,100);
#The first line creates a numpy array called numbers
#The second line uses matplotlib to create a histogram plot
#based on the numbers array.

"""# PRNG

See Here!!
[PRNG Lab 2.5](https://colab.research.google.com/drive/1HUZPmRsPI6vNPKnMhgIvFpDS14AAP8w7?usp=sharing)
"""

x = 0.12345

x = x*3

x % 1

current_point = 0.12345          # seed value
points_to_save = np.zeros(50000,)  # initialize an array of zeros

for i in __builtin__.range(points_to_save.shape[0]):
    current_point = 3*current_point % 1      # update x and store the value in X
    points_to_save[i] = current_point

plt.plot(points_to_save, '.')     # plot the values in X

plt.hist(points_to_save);

def coin():
    return 2*(np.random.random() > 0.5) - 1
#When you call coin(), it generates a random number between 0 and 1
#If the number is greater than 0.5, it returns 1 (heads);
#otherwise, it returns -1 (tails)

coin()

x = 0
#This line assigns the value 0 to the variable x
x + coin()
#Since x is 0, the result of x + coin() will be the result of the coin flip
#If the coin flip result is heads, the expression evaluates to 0 + 1 = 1
#If the coin flip result is tails, the expression evaluates to 0 + (-1) = -1

x = 0

for i in range(3):
    x = x + coin()
#If the coin flip result is heads, x increases by 1.
#If the coin flip result is tails, x decreases by 1.
#After three iterations, the final value of x depends
#on the outcomes of the coin flips.

x

x = 0

for i in range(100):
    x = x + coin()
#If the coin flip result is heads, x increases by 1.
#If the coin flip result is tails, x decreases by 1.
#After 1000 iterations, the final value of x depends
#on the outcomes of the coin flips.

x

M = 10000
N = 100

X = np.zeros(M,)

for j in range(M):

    x = 0

    for i in range(N):
        x = x + coin()

    X[j] = x
#The code simulates 10,000 experiments, each involving 100 coin flips,
#and records the cumulative results in an array.
#The coin flip outcome is represented as 1 (heads) or -1 (tails).

plt.hist(X);



"""# Bonus: Explain Pascal's Triangle"""

P = np.zeros((12,18))

P[0,5]=1

for i in range(1,P.shape[0]):

    for j in range(1,P.shape[1]-1):

        P[i,j] = P[i-1,j-1]+P[i-1,j]

print(P[:,5:])
#This initializes a 12x18 array P with zeros, sets the value at row 0 and
#column 5 to 1, and then fills in the rest of the array using Pascal’s
#triangle recurrence relation. Finally, it prints the subarray from column 5+

"""# Normal Distribution"""

# Define the parameters for the normal distribution
mean = 0  # Mean (mu) of the distribution
std_dev = 0.1  # Standard deviation (sigma) of the distribution

# Generate 1000 data points following a normal distribution with the specified mean and standard deviation
sample_size = 10000
data_points = np.random.normal(mean, std_dev, sample_size)

# Plot the histogram of the data points
bins_number = 30  # Number of bins for the histogram
hist_count, x, ignored = plt.hist(data_points, bins_number, density=True)

x = np.linspace(-15,15,1000)

y = np.exp(-x**2)
#The code generates an array x with 1000 equally spaced points between -15 and
#15, and computes the corresponding array y where each value is the exponential
#function of negative x squared

plt.plot(x,y)

y2 = np.sin(10*x)

plt.plot(x,y2)

plt.plot(x,y*y2)

y3 =  np.exp(- (x - 0) ** 2 )
plt.plot(x, y3, linewidth=2, color='r')
#This computes the function and plots it in red. This function represents an
#exponential decay curve centered around the origin.

# Define the parameters for the normal distribution
mean = 0  # Mean (mu) of the distribution
std_dev = 0.1  # Standard deviation (sigma) of the distribution

# Generate 1000 data points following a normal distribution with the specified mean and standard deviation
sample_size = 10000
data_points = np.random.normal(mean, std_dev, sample_size)

# Plot the histogram of the data points
bins_number = 30  # Number of bins for the histogram
hist_count, x, ignored = plt.hist(data_points, bins_number, density=True)

# Plot the probability density function of the normal distribution
normal_dist_curve = 1 / (std_dev * np.sqrt(2 * np.pi)) * np.exp(- (x - mean) ** 2 / (2 * std_dev ** 2))
plt.plot(x, normal_dist_curve, linewidth=2, color='r')

# Set the title and labels for the plot
plt.title('Normal Distribution Visualization')
plt.xlabel('Value')
plt.ylabel('Probability Density')

# Display the plot
plt.show()



x = np.array([1,2,3,4])
#The given code creates an array named x containing the elements 1, 2, 3, and 4.

np.sum(x)
#This gives the sum.

x.shape[0]
#The expression x.shape[0] returns the number of elements in the first dimension
#of the NumPy array x.

np.sum(x)/x.shape[0]
#This calculates the average of the elements in the NumPy array.

def mean(x):
    return np.sum(x)/x.shape[0]
#The expression defines a Python function to calculate the average of elements
#in a NumPy array.

mean(x)
#This displays the mean.

x
#This displays x.

x - mean(x)
#The expression calculates the difference between each element in the NumPy
#array x and its mean

(x - mean(x))**2
#The expression calculates the squared difference between each element in
#the NumPy array x and its mean.

def var(x):
    return mean((x - mean(x))**2)
#This function calculates the variance of the elements in a NumPy array by
#squaring the difference between each element and its mean.



def std(x):
    return np.sqrt(var(x))
#The Python function std calculates the standard deviation of the elements in a
#NumPy array by taking the square root of the variance.

mean(x)
#This displays the mean.

var(x)
#This gives variance.

std(x)
#This gives standard deviation.



"""### Uniform Random Numbers"""

X = np.random.random(500000,)
#The expression generates an array of 500,000 random float values uniformly
#distributed between 0 and 1

X

plt.hist(X,100);
#plots histogram

np.random.random()
#The function generates a random float value between 0 and 1
#using a uniform distribution

r = np.random.random()

r

r = np.random.randint(1,10)
#The expression generates a random integer between 1 (inclusive)
#and 10 (exclusive)

r

np.random.randn()
#The function generates an array of specified shape and fills it with random
#values according to the standard normal distribution

numbers  = np.random.randn(2,4)
#The expression generates an array of specified shape (2 rows and 4 columns)
#filled with random values sampled from the standard normal distribution

numbers.shape
#The expression retrieves the shape (dimensions) of the NumPy array.

numbers = numbers.reshape(-1)
# The expression reshapes the NumPy array `numbers` into a 1D array.

numbers.shape
# The expression retrieves the shape (dimensions) of the NumPy array `numbers`.

numbers= np.array([1,2,2,3,3,3,4,4,4,4])
# The expression creates a NumPy array named `numbers` with the specified
#elements.

plt.hist(numbers,100);
#plots histogram

numbers = np.random.randn(100000,)
plt.hist(numbers,100);

numbers = np.random.rand(1000000,)
plt.hist(numbers,100);

np.random.seed(12345)
data = np.random.randn(2, 100)

plt.figure(1, figsize=(9, 9))

plt.subplot(2,2,1)
plt.hist(data[0])
#A histogram is plotted for the first row of the data array.
#This subplot represents the distribution of values in the first row.

plt.subplot(2,2,2)
plt.scatter(data[0], data[1])
#A scatter plot is created using the first row of data as x-values and the second row as y-values.
#Each point represents a pair of corresponding values from the two rows.

plt.subplot(2,2,3)
plt.plot(data[0], data[1],'-')
#A line plot is generated using the first row of data as x-values and the second row as y-values.
#The line connects the points in the order they appear in the arrays.

plt.subplot(2,2,4)
plt.hist2d(data[0], data[1])
#A 2D histogram (heatmap) is created using both rows of data.
#This plot shows the joint distribution of the two variables.

plt.show()

"""Normal Dist Data"""

x = 10*np.random.randn(10000)

plt.hist(x);

x = np.random.rand(1000,)

plt.hist(x);



mu = 0  # mean of distribution
sigma = 1  # standard deviation of distribution
x = mu + sigma * np.random.randn(10000)

#generates random data following a normal distribution with a specified mean and standard deviation.

n,bins,patches = plt.hist(x,bins=100)
#The line of code you provided generates a histogram of the data stored in the variable x. The histogram is divided into 100 bins.

bins

y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
plt.plot(y)
# The provided code snippet calculates the probability density function (PDF) for a normal distribution using the given parameters mu (mean) and sigma (standard deviation). The resulting PDF is then plotted using plt.plot(y)

num_bins = 50
n,bins,patches = plt.hist(x, num_bins, density=1)
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
plt.plot(bins,y)
#generates a histogram and plots the probability density function (PDF) for a normal distribution with specified mean and standard deviation.



x

def mean(x):
    return np.sum(x)/x.shape[0]
#creates a function that returns mean.

def var(x):
    return mean((x - mean(x))**2)
#function returns variance.

def std(x):
    return np.sqrt(var(x))
#returns standard deviation.

def median(x):
    n = len(x)
    sorted_x = np.sort(x)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_x[mid - 1] + sorted_x[mid]) / 2
    else:
        return sorted_x[mid]
#function returns median value.

def mode(x):
    values, counts = np.unique(x, return_counts=True)
    max_count_index = np.argmax(counts)
    return values[max_count_index]
#function returns mode or repeated value.

def range1(x):
    return np.max(x) - np.min(x)
#function returns the range difference value.

data = np.array([1, 2, 2, 3, 4, 5, 5, 5, 6])

# Testing the functions
mean_value = mean(data)
var_value = var(data)
std_value = std(data)
median_value = median(data)
mode_value = mode(data)
range_value = range1(data)

mean_value, var_value, std_value, median_value, mode_value, range_value
#This creates an array called data with the given values.
#Then, it calculates various statistical measures for this data, including the mean, variance, standard deviation, median, mode, and range.
#Finally, it displays the computed values.



"""# Homework



"""



"""# Pi from Random Numbers"""

N = 10

points = -1 + 2*np.random.random((N,2))
#This generates 10 random points in a 2D space.
#Each point’s coordinates lie between -1 and 1

points

plt.plot(points[:,0],points[:,1],'.')

plt.gca().set_aspect(1)
#This generates a scatter plot of the points in a 2D space.
#Each point’s x-coordinate is taken from the first column of the points array,
#and its y-coordinate is taken from the second column.
#The aspect ratio of the plot is set to be equal, ensuring that the units along both axes are the same.

inside_circle  = points[:,0]**2 + points[:,1]**2  <=  1
# determines whether each point lies inside the unit circle (distance from origin ≤ 1).
outside_circle = points[:,0]**2 + points[:,1]**2  > 1
# computes the complement of the inside_circle array
# and identifies points that are outside the unit circle.
plt.plot(points[inside_circle,0],points[inside_circle,1],'g.')
#plots the points inside the circle in green.
plt.plot(points[outside_circle,0],points[outside_circle,1],'r.')
#plots the points outside the circle in red.

plt.gca().set_aspect(1)
# ensures that the aspect ratio of the plot is equal (i.e., the x and y axes have the same scale).

np.sum(inside_circle),np.sum(outside_circle)
#Gives the sum of points inside the unit circle and outside the unit circle.

total_area = 4

fraction_inside = np.sum(inside_circle)/N
#represents the proportion of points that fall inside the unit circle among all the generated points.

fraction_inside*total_area
#provides an estimate of the area inside the unit circle based on the generated random points.

N = 100000000
points = -1 + 2*np.random.random((N,2))
inside_circle  = points[:,0]**2 + points[:,1]**2  <=  1
fraction_inside = np.sum(inside_circle)/N
fraction_inside*4

#the code demonstrates a simple Monte Carlo method for estimating the area of a unit circle using random points.

"""# Complete Code for Estimating π using Monte Carlo Simulation"""

# Number of random points to generate
num_points = 10000

# Generating random points
x_points = np.random.uniform(-1, 1, num_points)
y_points = np.random.uniform(-1, 1, num_points)

# Calculating the number of points inside the quarter circle
points_inside = np.sqrt(x_points**2 + y_points**2) <= 1
num_inside = np.sum(points_inside)

# Estimating π
pi_estimate = 4 * num_inside / num_points

# Plotting the points and the quarter circle
plt.figure(figsize=(6, 6))
plt.scatter(x_points[points_inside], y_points[points_inside], color='green', label='Inside')
plt.scatter(x_points[~points_inside], y_points[~points_inside], color='red', label='Outside')
circle = plt.Circle((0, 0), 1, color='blue', fill=False)
plt.gca().add_artist(circle)
plt.title('Estimating π using Monte Carlo Simulation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.axis('equal')
plt.show()

pi_estimate



"""# e from Random Numbers"""

X = np.random.random((1000000,10))
#this code creates a large matrix (X) filled with random values.
#The shape of the matrix is 1,000,000 rows by 10 columns.

Y = np.cumsum(X,1)
#the code generates random data in X and then computes the cumulative sum along the columns to create Y.

Z = np.argmax(Y > 1,1) + 1
#this  code identifies the first occurrence of a value greater than 1 in each row of Y and returns the corresponding column index (plus 1).

np.mean(Z)
#gives mean

np.mean(np.argmax(np.cumsum(np.random.random((10000000,10)),1) > 1,1) + 1)
#the entire expression calculates the average position (column index) of the first occurrence of a value greater than 1 in each row of the cumulative sum matrix Y

np.exp(1)
#The line of code np.exp(1) calculates the exponential function of the number 1
#It evaluates to approximately 2.71828, which is the value of the mathematical constant e.

"""# Further Reading:

### Quantum Random Numbers API

https://aws.amazon.com/marketplace/pp/prodview-246kyrfjo3bag
"""