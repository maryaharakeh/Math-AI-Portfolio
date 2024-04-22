# -*- coding: utf-8 -*-
"""Copy of Lab 8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DZkXSxS2j0FeGM7ViNhz-TUeJUJ2hoLs
"""

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# !pip install wandb
# !apt-get install poppler-utils
# !pip install pdf2image
# !pip install flashtorch
# import requests
# from pdf2image import convert_from_path
# import matplotlib.pyplot as plt
# import numpy as np
# import torch
# import requests
# from torchvision import *
# from torchvision.models import *
# import wandb as wb
# #This code cell in Python installs necessary packages using pip and apt-get,
# #imports required libraries, and sets up the environment for further processing.
# #It installs `wandb` (Weights & Biases) via pip, `poppler-utils` via apt-get
# #(for working with PDF files), `pdf2image` (for converting PDFs to images), and
# #`flashtorch` (for visualizing and interpreting deep learning models).
# #After the installations, it imports several libraries such as requests, pdf2image, matplotlib, numpy, torch, torchvision, and wandb.

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#This line checks if CUDA (GPU computing platform by NVIDIA) is available. If CUDA is available, it sets the device to use the GPU (specifically, GPU 0); otherwise, it sets the device to use the CPU.
def GPU(data):
    return torch.tensor(data, requires_grad=True, dtype=torch.float, device=device)
# This is a function that takes data and returns a PyTorch tensor. The tensor is placed on the device determined by the previous step (GPU if available, otherwise CPU). The tensor requires gradient computation and is of type float.
def GPU_data(data):
    return torch.tensor(data, requires_grad=False, dtype=torch.float, device=device)
#Similar to the previous function, this one also creates a PyTorch tensor but without requiring gradient computation. It's useful for data that doesn't need to be involved in gradient-based optimization, such as input data or labels.
def plot(x):
    fig, ax = plt.subplots()
    im = ax.imshow(x, cmap = 'gray')
    ax.axis('off')
    fig.set_size_inches(5, 5)
    plt.show()
#This function plots the given numpy array (presumably representing an image) using matplotlib. It creates a grayscale image with the specified colormap and displays it without axis ticks.
def get_google_slide(url):
    url_head = "https://docs.google.com/presentation/d/"
    url_body = url.split('/')[5]
    page_id = url.split('.')[-1]
    return url_head + url_body + "/export/pdf?id=" + url_body + "&pageid=" + page_id
#This function takes a Google Slides URL, extracts the necessary information to construct a download link for the PDF version of the slides, and returns that download link.
def get_slides(url):
    url = get_google_slide(url)
    r = requests.get(url, allow_redirects=True)
    open('file.pdf', 'wb').write(r.content)
    images = convert_from_path('file.pdf', 500)
    return images
# This function takes a Google Slides URL, gets the PDF version of the slides using the get_google_slide function, downloads the PDF file, and then converts it into a list of images using convert_from_path function from pdf2image. It returns a list of image objects representing each slide.
def load(image, size=224):
    means = [0.485, 0.456, 0.406]
    stds = [0.229, 0.224, 0.225]
    transform = transforms.Compose([
        transforms.Resize(size),
        transforms.CenterCrop(size),
        transforms.ToTensor(),
        transforms.Normalize(means, stds)
    ])
    tensor = transform(image).unsqueeze(0).to(device)
    tensor.requires_grad = True
    return tensor
#This function prepares an image for input into a neural network. It resizes
#and crops the image to the specified size, converts it to a PyTorch tensor,
#and normalizes it using pre-defined means and standard deviations.
#The resulting tensor is placed on the device determined earlier and set to require gradient computation.

labels = {int(key):value for (key, value) in requests.get('https://s3.amazonaws.com/mlpipes/pytorch-quick-start/labels.json').json().items()}

model = alexnet(weights='DEFAULT').to(device)
model.eval();
#1: It sends a GET request to a specific URL hosting a JSON file containing labels. It then converts the JSON response into a Python dictionary where keys are integers and values are the corresponding labels.
#2: It initializes an AlexNet model using pre-trained weights from the default source. The model is then transferred to the specified device (either GPU if available, otherwise CPU). Finally, it sets the model into evaluation mode, which is typically used during inference to disable operations like dropout.

url = "https://docs.google.com/presentation/d/17Nxy2Wo0erk71fp4sCDQqHrHYkxwjdExjbosjoEewuU/edit#slide=id.p"

images = []

for image in get_slides(url):

    plot(image)

    images.append(load(image))

images = torch.vstack(images)
#This code iterates through images obtained from a Google Slides URL, plots
#each image, loads and preprocesses them for a neural network input, and finally stacks them vertically into a single tensor.

images.shape #The shape of the images tensor would depend on the number of images processed and their dimensions after preprocessing.
#It includes the number of images, number of colors channels, height and width of each image.

model(images)
#This involves passing the preprocessed images through a neural network model.
#Specifically, it feeds the tensor images, which contains the preprocessed image
#data, into the neural network model (model).
#This process applies the learned weights and biases of the model to the input images, performing computations through the layers of the network, and ultimately producing output.

y = model(images) #stores output in variable

y.shape #gives number of input images and number of output classes or features

guesses = torch.argmax(y, 1).cpu().numpy()
#this line of code is getting the predicted class labels from the model output y,
#moving the predictions to the CPU, and converting them to a NumPy array.
#The result is stored in the variable guesses

for i in list(guesses):
    print(labels[i])
#This code iterates over the guesses list and prints the corresponding label for each guess from the labels list.

Y = np.zeros(50,)
Y[25:] = 1
#This code creates a NumPy array Y of length 50 filled with zeros, then sets the last 25 elements of the array to 1.

Y #displays array

# Y = np.zeros(100,)
# Y[50:] = 1

Y #displays array

X = y.detach().cpu().numpy()
#this line of code is detaching the tensor y from its computation graph,
#moving it to the CPU, and converting it to a NumPy array.
#The result is stored in the variable X.

X.shape #returns dimensions of array

plt.plot(X[0],'.')
#creates scatterplot of the first row

plt.hist(X[0])
#plots histogram of the first row

X = GPU_data(X)
Y = GPU_data(Y)
#This code moves the data in the variables `X` and `Y` to the GPU using the `GPU_data` function, presumably for faster computation in a machine learning context.
#The results are stored back in `X` and `Y`.

def softmax(x):
    s1 = torch.exp(x - torch.max(x,1)[0][:,None])
    s = s1 / s1.sum(1)[:,None]
    return s
#The `softmax` function in the provided code calculates the softmax of a tensor `x`, transforming it into a vector of real numbers in the range (0, 1) that add up to 1.
#This is commonly used in machine learning to convert raw scores into probabilities.
#The function is applied across each row of the tensor, making it particularly useful in tasks such as multi-class classification and ranking problems in neural networks.

def cross_entropy(outputs, labels):
    return -torch.sum(softmax(outputs).log()[range(outputs.size()[0]), labels.long()])/outputs.size()[0]
#this function computes the average negative log-probability of the correct class, a common measure of classification error.
#This is also known as the cross-entropy loss.

def randn_trunc(s): #Truncated Normal Random Numbers
    mu = 0
    sigma = 0.1
    R = stats.truncnorm((-2*sigma - mu) / sigma, (2*sigma - mu) / sigma, loc=mu, scale=sigma)
    return R.rvs(s)
#The function `randn_trunc(s)` generates `s` random numbers from a truncated normal distribution with mean `mu=0`, standard deviation `sigma=0.1`, and range `-2*sigma` to `2*sigma`.

def Truncated_Normal(size):

    u1 = torch.rand(size)*(1-np.exp(-2)) + np.exp(-2)
    u2 = torch.rand(size)
    z  = torch.sqrt(-2*torch.log(u1)) * torch.cos(2*np.pi*u2)

    return z
#The function `Truncated_Normal(size)` generates `size` random numbers from a truncated normal distribution
#using the Box-Muller transform method.

def acc(out,y):
    with torch.no_grad():
        return (torch.sum(torch.max(out,1)[1] == y).item())/y.shape[0]
#The function `acc(out, y)` calculates the accuracy of the model's predictions (`out`) compared to the true labels (`y`).

X.shape #gives number of input images and and output classes

def get_batch(mode):
#Defines a function named get_batch that takes a mode parameter.
    b = c.b
#Assigns the value of the variable b from the context c.
    if mode == "train":
# Checks if the mode is "train".
        r = np.random.randint(X.shape[0]-b)
#Generates a random integer r within the range of valid indices for the training data X, considering the batch size b.
        x = X[r:r+b,:]
#Slices the training data X to extract a batch of input samples starting from index r and ending at r+b
        y = Y[r:r+b]
#Slices the training labels Y to extract corresponding labels for the batch of samples.
    elif mode == "test":
#Checks if the mode is "test".
        r = np.random.randint(X_test.shape[0]-b)
#Generates a random integer r within the range of valid indices for the test data X_test, considering the batch size b.
        x = X_test[r:r+b,:]
#Slices the test data X_test to extract a batch of input samples starting from index r and ending at r+b.
        y = Y_test[r:r+b]
#Slices the test labels Y_test to extract corresponding labels for the batch of samples.
    return x,y
#Returns the batch of input samples x and their corresponding labels y.

def model(x,w):

    return x@w[0]
#This function performs matrix multiplication between input `x` and the first element of weight tensor `w` and returns the result.

def make_plots():

    acc_train = acc(model(x,w),y)

    # xt,yt = get_batch('test')

    # acc_test = acc(model(xt,w),yt)

    wb.log({"acc_train": acc_train})
#Defines a function `make_plots()` that calculates the training accuracy of a
#model on a given dataset `x` with labels `y` using `acc()` function and logs the training accuracy to Weights & Biases (W&B) platform using `wb.log()`.

wb.init(project="Linear_Model_Photo_1");
#Initializes a new W&B run associated with the project "Linear_Model_Photo_1".
c = wb.config #Retrieves the configuration for the run.

c.h = 0.001 # Sets the learning rate (h).
c.b = 32   #Sets the batch size (b).
c.epochs = 100000  #Sets the number of training epochs (epochs).

w = [GPU(Truncated_Normal((1000,2)))]
#Initializes the weight parameters (w) as a GPU tensor of shape (1000, 2) sampled from a truncated normal distribution.
optimizer = torch.optim.Adam(w, lr=c.h)
#Initializes the Adam optimizer with the provided learning rate c.h for the weights w.
for i in range(c.epochs):
#Iterates over the specified number of epochs.
    x,y = get_batch('train')
#Obtains a batch of training data (x) and labels (y).
    loss = cross_entropy(softmax(model(x,w)),y)
# Calculates the cross-entropy loss between the model predictions and the true labels.
    optimizer.zero_grad() #Resets the gradients of the model parameters.
    loss.backward() #Computes gradients of the loss with respect to the model parameters.
    optimizer.step() #Updates the model parameters using the computed gradients.

    wb.log({"loss": loss}) #Logs the current loss value to W&B.

    make_plots() # function to calculate and log training accuracy.


