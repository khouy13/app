import imageio
import glob
import os
from PIL import Image
import numpy as np
# Set the desired width and height for the images
desired_width = 300
desired_height = 200

filenames = glob.glob('test/h*.png')
filenames = sorted(filenames)
images = []

for filename in filenames:
    img = Image.open(filename)
    # Resize the image to the desired width and height
    resized_img = np.array(img.resize((desired_width, desired_height), Image.ANTIALIAS))
    resized_array =np.array(imageio.core.util.Array(resized_img))
    images.append(resized_array)

output_file = 'output.gif'
imageio.mimsave(output_file, images, 'GIF', fps=100)

# Open the generated GIF file
if os.name == 'nt':  # Check if the system is Windows
    os.startfile(output_file)
elif os.name == 'posix':  # Check if the system is Linux or MacOS
    os.system('open ' + output_file)
