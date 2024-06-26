# -*- coding: utf-8 -*-
"""Copy of Final Project Notebook Hahn Stats 24.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AHRVpHUChcmAUGzG8dx8xShnTc0z1-9g

# Final Project Notebook - Spring 2024
"""

import matplotlib.pyplot as plt
#Imports the matplotlib.pyplot module and aliases it as plt for easier usage.
import imageio
#Imports the imageio module, which provides functions for reading and writing a wide range of image data.
import torch
#Imports the PyTorch library, a popular open-source machine learning framework.
import torchvision
#Imports the torchvision library, which provides utility functions and datasets for computer vision tasks.
from torchvision import models, transforms
#mports the models and transforms modules from torchvision, which contain pre-trained models and image transformation functions, respectively.
import numpy as np
#Imports the numpy library and aliases it as np, which is commonly used for numerical computing.
from torchvision.models import *
# Imports all models from the torchvision.models module, which includes pre-trained deep learning models for various tasks.
from PIL import Image
#Imports the Image module from the Python Imaging Library (PIL), which provides functions for working with images.
import requests
# Imports the requests module, which is used for making HTTP requests.
from torchvision import models
#Imports the models module from torchvision, which contains pre-trained models for computer vision tasks.
from torchsummary import summary
#Imports the summary function from the torchsummary module, which provides a summary of PyTorch model architectures.

def plot(x):
#Defines a function named plot that takes a single argument x.
    fig, ax = plt.subplots()
#Creates a new figure and axis object using Matplotlib's subplots() function, and assigns them to fig and ax variables respectively.
    im = ax.imshow(x,cmap='gray')
#Displays the image represented by the array x on the axis ax as an image using Matplotlib's imshow() function. The colormap used is grayscale ('gray').
    ax.axis('off')
# Turns off the axis for the plot, removing ticks and labels.
    fig.set_size_inches(20, 20)
#Sets the size of the figure to be 20 inches by 20 inches.
    plt.show()
#Displays the plot with all the modifications made above.

im = imageio.imread('https://raw.githubusercontent.com/imageio/imageio-binaries/master/images/imageio_banner.png')
#This line reads an image from the specified URL using the imageio.imread() function and assigns it to the variable im. The image is loaded into memory as a NumPy array.

plot(im) #This line calls the plot() function defined earlier, passing the image loaded from the URL (im) as an argument. Inside the plot() function, the image is displayed using Matplotlib, showing it as a grayscale image with the axis turned off and a specified figure size.

net = alexnet(pretrained=True).cuda(0)
#This line loads the pre-trained AlexNet model from torchvision, setting the pretrained parameter to True to use the pre-trained weights. It then moves the model to the GPU with index 0 using the .cuda(0) method, making use of GPU acceleration for computations. The resulting model is assigned to the variable net.

"""Concepts used: Normalization, Resizing, Center Crop, Conversion to Tensor"""

normalize = transforms.Normalize(
   mean=[0.485, 0.456, 0.406],
   std=[0.229, 0.224, 0.225]
)
#Defines a normalization transformation using the transforms.Normalize function. It normalizes the input tensor with mean [0.485, 0.456, 0.406] and standard deviation [0.229, 0.224, 0.225].
preprocess = transforms.Compose([
#Creates a pipeline of transformations using transforms.Compose. This allows chaining multiple transformations together.
   transforms.Resize(256),
#Resizes the input image to have a size of 256x256 pixels.
   transforms.CenterCrop(224),
#Crops the center of the image to have a size of 224x224 pixels.
   transforms.ToTensor(),
#Converts the image to a PyTorch tensor.
   normalize
#Applies the normalization transformation defined earlier (normalize) to the tensor. This step ensures that the input data is properly normalized before being fed into the model.
])

im = imageio.imread('https://www.medicalnewstoday.com/content/images/articles/322/322868/golden-retriever-puppy.jpg')
#This line reads an image from the specified URL using the imageio.imread() function and assigns it to the variable im. The image is loaded into memory as a NumPy array.

plot(im)
#This line calls the plot() function, passing the image loaded from the URL (im) as an argument. Inside the plot() function, the image is displayed using Matplotlib, showing it as a grayscale image with the axis turned off and a specified figure size.

image = Image.fromarray(im) #convert to pil
#This line converts a NumPy array `im` representing an image into a PIL (Python Imaging Library) image object named `image`. It facilitates further image processing using PIL's functionality.

img_tensor = preprocess(image)
#This line applies a series of preprocessing transformations (`preprocess`) to the PIL image `image`, resulting in a tensor (`img_tensor`). These transformations typically include resizing, center cropping, converting to tensor format, and normalization. The tensor is then ready to be inputted into a neural network for further processing or analysis.

img_tensor = img_tensor.unsqueeze_(0)
#This line adds an extra dimension to the tensor img_tensor at the beginning, effectively changing its shape from (C, H, W) to (1, C, H, W)
#This operation is commonly done to match the expected input shape of neural network models, which often require a batch dimension even if you're processing a single image.

img_tensor.shape
#This line retrieves and displays the shape of the tensor `img_tensor`, indicating the number of dimensions and the size along each dimension.

img_variable = torch.tensor(img_tensor).cuda(0)
#This line converts the tensor `img_tensor` to a PyTorch tensor, then moves it to the GPU device with index 0 (`cuda(0)`).

out = net(img_variable)
#This line passes the input tensor `img_variable` through the neural network model `net`, producing the output tensor `out`, which contains the model's predictions or activations.

label_index = out.cpu().data.numpy().argmax()
#This line retrieves the index of the highest predicted probability from the output tensor `out` after moving it to the CPU, converting it to a NumPy array, and finding the index of the maximum value.

label_index
#This variable `label_index` stores the index corresponding to the predicted class label of the input image.

top_list = np.flip(np.argsort(out.cpu().data.numpy())[0][-10:])
#This line sorts the predicted probabilities in descending order, selects the top 10 probabilities, and stores their corresponding indices in `top_list`.

LABELS_URL = 'https://s3.amazonaws.com/mlpipes/pytorch-quick-start/labels.json'
#This line defines the URL from which a JSON file containing class labels for the model's predictions will be retrieved.

labels = {int(key):value for (key, value) in requests.get(LABELS_URL).json().items()}
#This line fetches a JSON file from the specified URL, converts it into a Python dictionary, and maps the class indices to their corresponding labels.

print(labels[label_index])
#This line prints the label corresponding to the predicted class index `label_index`.

for i in range(10):
    print(labels[top_list[i]])
#This loop prints the top 10 predicted class labels based on their respective probabilities stored in the `top_list` variable.

net #This refers to the neural network model `net` that was previously defined and initialized, such as AlexNet or any other neural network architecture used in the code.

summary(net, (3, 224, 224))
#This line generates a summary of the neural network model `net`, displaying information about its architecture, including layer types, output shapes, and the number of parameters, based on input tensor shape `(3, 224, 224)`, which represents an image with 3 channels (e.g., RGB) and size 224x224.

out = net.features[0](img_variable).cpu().detach().numpy()
#This line computes the output of the first layer (`net.features[0]`) of the neural network `net` for the input image tensor `img_variable`, converts it to a NumPy array, and moves it to the CPU.

plot(out[0,0,:,:])
#This line plots the grayscale representation of the output of the first layer (`out`) for the input image, displaying it using Matplotlib.

"""Concepts Used: Indexing and Slicing and Flattening"""

plt.plot(np.arange(4096),net.classifier[0:6](net.avgpool(net.features[0:13](img_variable)).flatten()).cpu().detach().numpy())
fig = plt.gcf()
fig.set_size_inches(10, 10)
#This code plots the output of the first six layers of the classifier part of the neural network `net`, applied to the input image `img_variable`, after passing through the corresponding layers of the feature extractor (`net.features[0:13]`).
#The output values are flattened and plotted against their corresponding indices using Matplotlib.
#Additionally, it sets the size of the figure to be 10 inches by 10 inches.

#The code uses indexing and slicing to select specific layers from the network.
#After passing through the selected layers, the output is flattened. Flattening reshapes a multidimensional array into a one-dimensional array, which is often necessary when passing data to fully connected layers.

im = imageio.imread('http://bocasurfcam.com/most_recent_image.php')
#This line reads an image from the specified URL using the imageio.imread() function and assigns it to the variable im. The image is loaded into memory as a NumPy array.

plot(im) #This line plots the image represented by the array im using Matplotlib, displaying it in a new figure.

def load_im(im):
#defines a function
    image = Image.fromarray(im) #convert to pil
#Converts the NumPy array im representing an image into a PIL (Python Imaging Library) image object named image.
    img_tensor = preprocess(image)
#Applies a series of preprocessing transformations to the PIL image image, resulting in a tensor img_tensor. These transformations may include resizing, center cropping, converting to tensor format, and normalization.
    img_tensor = img_tensor.unsqueeze_(0)
#Adds an extra dimension to the tensor img_tensor at the beginning, effectively changing its shape from (C, H, W) to (1, C, H, W), where C represents the number of channels, and H and W represent the height and width of the image, respectively. This operation is often done to match the expected input shape of neural network models.
    img_variable = torch.tensor(img_tensor).cuda(0)
#Converts the tensor img_tensor to a PyTorch tensor and moves it to the GPU device with index 0 (cuda(0)), making use of GPU acceleration for computations.
    return img_variable
#Returns the resulting PyTorch tensor img_variable, which represents the preprocessed image and is ready to be used as input to a neural network model.

out = net(load_im(im))
#This line passes the image loaded from the variable `im` through the function `load_im()`, which preprocesses the image and converts it into a format suitable for input to the neural network model `net`. The resulting preprocessed image tensor is then passed through the neural network `net`, and the output is stored in the variable `out`.

"""Concepts Used: Matrix Operations, Normalization, and Probability."""

def inference(im):
#defines a function
    out = net(load_im(im))
# Passes the image im through the load_im() function to preprocess it and then through the neural network net for inference, storing the output in the variable out.
    label_index = out.cpu().data.numpy().argmax()
#Extracts the index corresponding to the predicted class label from the output tensor out. This involves moving the tensor to the CPU (cpu()), converting it to a NumPy array (data.numpy()), and finding the index of the maximum value (argmax()).
    top_list = np.flip(np.argsort(out.cpu().data.numpy())[0][-10:])
#Sorts the predicted probabilities in descending order, selects the top 10 probabilities, and stores their corresponding indices in top_list. This involves moving the output tensor to CPU, converting it to a NumPy array, sorting it in ascending order, flipping it to descending order, and selecting the top 10 indices.
    print(labels[label_index])
#Prints the predicted class label corresponding to the label_index.
    print('____')
#Prints a separator to visually distinguish between the predicted label and the top predicted labels.
    for i in range(10):
#Initiates a loop to iterate over the top 10 predicted indices.
        print(labels[top_list[i]])
#Prints the labels corresponding to the top 10 predicted indices, indicating the top predicted classes along with their probabilities.

inference(im)
#orchestrates the mathematical computations involved in preprocessing, forward pass through the neural network, and post-processing to perform image classification.

"""# Restart Notebook (Disconnect and Delete Runtime) Before Running Next Section

# Custom Data Deck
"""

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# #This is a Jupyter notebook magic command used to suppress the output of the subsequent shell commands.
# !pip install wandb
# # Installs the Weights & Biases (wandb) library for experiment tracking and visualization.
# !apt-get install poppler-utils
# #Installs the poppler-utils package, which includes utilities for working with PDF files.
# !pip install pdf2image
# #Installs the pdf2image library, which provides functions to convert PDF files to images.
# !pip install flashtorch
# #Installs the flashtorch library, which offers utilities for visualizing and interpreting neural network models.
# import requests
# #Imports the requests module, which is used for making HTTP requests.
# from pdf2image import convert_from_path
# # Imports the convert_from_path function from the pdf2image module, which converts PDF files to images.
# import matplotlib.pyplot as plt
# # Imports the matplotlib.pyplot module and aliases it as plt for plotting purposes.
# import numpy as np
# #Imports the NumPy library and aliases it as np, commonly used for numerical computing.
# import torch
# # Imports the PyTorch library, a popular open-source machine learning framework.
# import requests
# #This line is redundant as requests module has been already imported.
# from torchvision import *
# #Imports all submodules and classes from the torchvision package, which provides utility functions and datasets for computer vision tasks.
# from torchvision.models import *
# # Imports all models from the torchvision.models module, which includes pre-trained deep learning models for various tasks.
# from flashtorch.utils import apply_transforms
# #Imports the apply_transforms function from the flashtorch.utils module, which applies transformations to images for visualization.
# import wandb as wb
# #Imports the Weights & Biases library and aliases it as wb, typically used for experiment tracking and visualization.

def GPU(data):
    return torch.tensor(data, requires_grad=True, dtype=torch.float, device=torch.device('cuda'))
#Converts input data into a PyTorch tensor allocated in GPU memory with gradients enabled for backpropagation during training.

def GPU_data(data):
    return torch.tensor(data, requires_grad=False, dtype=torch.float, device=torch.device('cuda'))
#Converts input data into a PyTorch tensor allocated in GPU memory without requiring gradients, suitable for inference or operations that don't involve training.

"""Concepts Used: Coordinates, Dimensions, and Mapping Values to Colors"""

def plot(x):
    fig, ax = plt.subplots()
# Creates a new figure (fig) and axis (ax) objects using Matplotlib's subplots() function, allowing for the creation of multiple subplots within the same figure.
    im = ax.imshow(x, cmap = 'gray')
#Displays the image represented by the array x on the axis ax as an image using Matplotlib's imshow() function. The colormap used is grayscale ('gray').
    ax.axis('off')
#Turns off the axis for the plot, removing ticks and labels.
    fig.set_size_inches(5, 5)
# Sets the size of the figure to be 5 inches by 5 inches.
    plt.show()
#Displays the plot with all the modifications made above.

def get_google_slide(url):
#Constructs the URL for fetching Google Slide presentation slides in PDF format based on the input URL.
    url_head = "https://docs.google.com/presentation/d/"
#Initializes the base URL for Google Slides.
    url_body = url.split('/')[5]
#Extracts the unique identifier of the Google Slide presentation from the input URL.
    page_id = url.split('.')[-1]
#Extracts the page identifier from the URL.
    return url_head + url_body + "/export/pdf?id=" + url_body + "&pageid=" + page_id
#Constructs and returns the URL for fetching the slides in PDF format.

def get_slides(url):
#Obtains the slides from the specified Google Slide URL and converts them into images.
    url = get_google_slide(url)
#alls get_google_slide(url) to get the URL for fetching the slides.
    r = requests.get(url, allow_redirects=True)
#Sends a GET request to the constructed URL to fetch the slides in PDF format.
    open('file.pdf', 'wb').write(r.content)
#Writes the received PDF content to a local file named 'file.pdf'.
    images = convert_from_path('file.pdf', 500)
#Converts the PDF slides into images with a specified resolution of 500 DPI.
    return images
#Returns a list of image objects representing the slides.
def load(image):
#Prepares the input image for processing with a neural network.
    return apply_transforms(image).clone().detach().requires_grad_(True).to(device)
#Applies necessary transformations to the input image, creates a copy, detaches it from the computation graph, enables gradient tracking, and moves it to the specified device (CPU or GPU).
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#Detects the available device (GPU or CPU) for running computations and sets the device variable accordingly.

labels = {int(key):value for (key, value) in requests.get('https://s3.amazonaws.com/mlpipes/pytorch-quick-start/labels.json').json().items()}
#This line fetches a JSON file from a URL, converts it into a Python dictionary, and maps the class indices to their corresponding labels.

model = alexnet(weights='DEFAULT').to(device)
model.eval();
#This line initializes an AlexNet model with pretrained weights, moves it to the specified device (CPU or GPU), and sets it to evaluation mode.

url = "https://docs.google.com/presentation/d/1lyE52a0yLCu9iUiKeFmdKayGJhu2Z6fyToXEMKeigoY/edit#slide=id.p"

images = []
# Initializes an empty list to store processed images.
for image in get_slides(url):
#Iterates through the images obtained from the get_slides() function.
    plot(image)
#isplays the current image using the plot() function.
    images.append(load(image))
#Processes the current image using the load() function, then appends the processed image to the list.
images = torch.vstack(images)
#Converts the list of processed images into a single tensor by vertically stacking them.

images.shape
#This line retrieves the shape of the tensor `images`, indicating the number of images and the dimensions of each image in the batch.

model(images)
#This line passes the batch of images through the neural network model `model`, generating predictions or activations for each image.

y = model(images)
#This line passes the batch of images through the neural network model `model`, generating predictions or activations for each image, and assigns the output to the variable `y`.

y.shape
#This line retrieves the shape of the tensor `y`, indicating the dimensions of the output generated by the neural network model for the batch of images.

guesses = torch.argmax(y, 1).cpu().numpy()
#This line calculates the index of the maximum value along the second dimension of the tensor `y`, representing the predicted class labels for each image in the batch, and converts it to a NumPy array on the CPU.

for i in list(guesses):
    print(labels[i])
#This loop iterates over the list of predicted class labels (`guesses`), converting each index into its corresponding class label using the `labels` dictionary, and prints the class label for each prediction.

Y = np.zeros(50,)
Y[25:] = 1
#This code initializes a NumPy array `Y` of size 50 with all elements set to 0. Then, it sets the elements from index 25 onwards to 1, effectively creating a binary array where the first half of the elements are 0s and the second half are 1s.

Y
#displays array

X = y.detach().cpu().numpy()
#This code retrieves the values from the PyTorch tensor `y`, detaches it from the computation graph, moves it to the CPU, and converts it into a NumPy array, assigning it to the variable `X`.

X.shape
#This line retrieves the shape of the NumPy array `X`, indicating the dimensions of the array.

"""Concepts Used: Plotting, Indexing, and Visualization"""

plt.plot(X[0],'.')
#This line plots the values of the first row of the NumPy array `X` using dots (`'.'`) as markers. Each value in the first row is plotted along the x-axis against its corresponding index.

X[0] #The expression `X[0]` selects the first row of the NumPy array `X`, returning it as a one-dimensional array.
#This operation involves basic indexing and array manipulation concepts.

np.argmax(X[0])
#This line calculates the index of the maximum value in the one-dimensional NumPy array `X[0]`, returning the index where the maximum value occurs.

labels[948]
#This line retrieves the value associated with the key `948` from the dictionary `labels`. It returns the label corresponding to the class index `948`.

top_ten = np.argsort(X[0])[::-1][0:10]
#This line sorts the elements of the one-dimensional NumPy array `X[0]` in ascending order and returns the indices that would sort the array. Then, it reverses the order of the sorted indices to obtain the indices of the top values in descending order. Finally, it selects the first 10 indices from the sorted array, representing the indices of the top 10 values in `X[0]`.

for i in top_ten:
    print(labels[i])
#This line iterates over the indices of the top 10 values in `X[0]`, printing the corresponding class labels retrieved from the `labels` dictionary for each index.

labels
#shows labels

plt.hist(X[0])
#This line creates a histogram plot of the values in the one-dimensional NumPy array `X[0]`. The histogram visualizes the distribution of values in `X[0]`, with each bin representing a range of values and the height of each bin representing the frequency of values falling within that range.

X = GPU_data(X)
Y = GPU_data(Y)
#These two lines convert the NumPy arrays `X` and `Y` into PyTorch tensors allocated in GPU memory without requiring gradients. This allows for efficient computation on GPU devices.

def softmax(x):
    s1 = torch.exp(x - torch.max(x,1)[0][:,None])
    s = s1 / s1.sum(1)[:,None]
    return s
#This function computes the softmax function for each row of the input tensor `x`, ensuring numerical stability by subtracting the maximum value from each row before exponentiation.
#Then, it normalizes the exponentiated values by dividing them by their sum along each row and returns the resulting tensor.

def cross_entropy(outputs, labels):
    return -torch.sum(softmax(outputs).log()[range(outputs.size()[0]), labels.long()])/outputs.size()[0]
#This function calculates the cross-entropy loss between the predicted outputs and the true labels, utilizing the softmax function to compute probabilities and then computing the negative log likelihood of the predicted probabilities corresponding to the true labels.

"""Concepts Used: Uniform Distribution, Inverse Transform Sampling, Truncation, Box-Muller Transform, Scaling, and Shifting."""

def Truncated_Normal(size):

    u1 = torch.rand(size)*(1-np.exp(-2)) + np.exp(-2)
#Generates random numbers from a uniform distribution between [e^-2,1).
    u2 = torch.rand(size)
#Generates random numbers from a uniform distribution between 0 and 1.
    z  = torch.sqrt(-2*torch.log(u1)) * torch.cos(2*np.pi*u2)
#Computes truncated normal samples by transforming uniformly distributed random numbers into samples from a truncated normal distribution.
    return z
#Returns the generated truncated normal samples.

def acc(out,y):
    with torch.no_grad():
        return (torch.sum(torch.max(out,1)[1] == y).item())/y.shape[0]
#This function computes the accuracy of a model's predictions by comparing the predicted labels (`out`) with the true labels (`y`). It uses the `torch.max()` function to obtain the predicted class indices, compares them with the true labels, calculates the number of correct predictions, and divides it by the total number of samples (`y.shape[0]`) to compute the accuracy. The `torch.no_grad()` context manager ensures that no gradient calculations are performed during the computation of accuracy.

X.shape #gives tensor dimensions

def get_batch(mode):
    b = c.b
#Assigns the batch size (b) from some external source (c.b).
    if mode == "train": #Checks if the mode is set to "train".
        r = np.random.randint(X.shape[0]-b)
#Generates a random integer r within the range of valid indices for training data, ensuring that the batch size b does not exceed the remaining data points.
        x = X[r:r+b,:]
#Selects a batch of input samples (x) from the training data X, starting from index r and ending at r + b, along with all features.
        y = Y[r:r+b]
#Selects the corresponding batch of target labels (y) from the training labels Y.
    elif mode == "test": #Checks if the mode is set to "test".
        r = np.random.randint(X_test.shape[0]-b)
#Generates a random integer r within the range of valid indices for test data, ensuring that the batch size b does not exceed the remaining data points.
        x = X_test[r:r+b,:]
#Selects a batch of input samples (x) from the test data X_test, starting from index r and ending at r + b, along with all features.
        y = Y_test[r:r+b]
#Selects the corresponding batch of target labels (y) from the test labels Y_test.
    return x,y
#Returns the batch of input samples and target labels.

def model(x,w):

    return x@w[0]
#This function performs matrix multiplication between the input data `x` and the weights `w[0]`, effectively implementing a linear transformation.

def make_plots():

    acc_train = acc(model(x,w),y)

    wb.log({"acc_train": acc_train})
#This function calculates the training accuracy of a model and logs it using Weights & Biases (wandb).

"""Concepts Used: Linear Model, Matrix Multiplication, Gradient Descent, Cross-Entropy Loss, Truncated Normal Distribution, Learning Rate, Bath Processing"""

wb.init(project="Linear_Model_Photo_1");
# Initializes the Weights & Biases experiment with the specified project name.
c = wb.config
#Retrieves configuration settings from Weights & Biases.
c.h = 0.001 #Sets the learning rate (h) to 0.001.
c.b = 4     #Sets the batch size (b) to 4.
c.epochs = 100000  #Sets the number of training epochs (epochs) to 100,000.

w = [GPU(Truncated_Normal((1000,2)))]
#Initializes the weight parameter w as a GPU tensor sampled from a truncated normal distribution with shape (1000, 2).
optimizer = torch.optim.Adam(w, lr=c.h)
# Initializes the Adam optimizer with the specified learning rate c.h for updating the model weights.
for i in range(c.epochs):
#Iterates over the specified number of training epochs.
    x,y = get_batch('train')
#Retrieves a batch of training data (x) and corresponding labels (y) using the get_batch function.
    loss = cross_entropy(softmax(model(x,w)),y)
#Computes the cross-entropy loss between the model predictions and true labels for the current batch.
    optimizer.zero_grad()
#Clears the gradients of all optimized tensors.
    loss.backward()
#Computes gradients of the loss with respect to model parameters.
    optimizer.step()
#Updates the model parameters based on the computed gradients and the optimizer's update rule.
    wb.log({"loss": loss})
#Logs the current loss value to the Weights & Biases dashboard.
    make_plots()
# Calls the make_plots function to update any relevant plots or visualizations for monitoring training progress.