# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot
from PIL import Image
from numpy import asarray



image = image.imread('dogs.jpeg')




# display the array of pixels as an image
pyplot.imshow(image)
pyplot.show()

# convert image to numpy array
data = asarray(image)

# summarize shape
print(data.shape)

# create Pillow image
image2 = Image.fromarray(data)


# summarize image details 
print(image2.mode)
print("Numpy----")
print(data)

print("Dog's Image Width and Height are: ")
print(image2.size)



temp=asarray(Image.open('dogs.jpeg'))
x=temp.shape[0]
y=temp.shape[1]*temp.shape[2]

temp.resize((x,y)) # a 2D array
print("The two dimentional array is: ")
print(temp)

