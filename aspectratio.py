# import required modules
from PIL import Image
from math import gcd


  
# get image
filepath = "scrambledeggs.jpg"
img = Image.open(filepath)
  
# get width and height
width = img.width
height = img.height

# display width and height
print("The height of the image is: ", height)
print("The width of the image is: ", width)

# calculate greatest common factor
# NOTE: you cannot simply just find the ratio of the width and height. That will give a answer like 0 or 3. The aspect ratio format is like 9:16.
img_gcd = (gcd(width, height)) 
print("The greatest common factor of the image is: ",img_gcd)

# calculate aspect ratio
r_width = width/img_gcd
r_height = height/img_gcd
print("The aspect ratio of the image is ", r_width, ":", r_height)
