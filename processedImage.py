from matplotlib.image import imread
import numpy as np
from matplotlib.image import imsave
# Read Image
img = imread('Satwik.jpeg') # Color image

# Convert the image to grayscale
img_gray = img[:,:,1]

# Genearte noise with same shape as that of the image
noise = np.random.normal(0, 50, img_gray.shape) 

# Add the noise to the image
img_noised = img_gray + noise

# Clip the pixel values to be between 0 and 255.
img_noised = np.clip(img_noised, 0, 255).astype(np.uint8)

output_filename = 'Satwik_noised.jpeg'

# Save the noised image
imsave(output_filename, img_noised, cmap='gray')

# Display a confirmation message
print(f"Image saved as {output_filename}")